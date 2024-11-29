from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from transactions.constants import DEPOSIT, WITHDRAWAL, LOAN, LOAN_PAID, TRANSFER
from datetime import datetime
from django.db.models import Sum
from django.shortcuts import render

from .models import UserBankAccount
from transactions.forms import (
    DepositForm,
    WithdrawForm,
    LoanRequestForm,
)
from transactions.models import Transaction

class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transactions/transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })

        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields=[
                'balance'
            ]
        )

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )

        return super().form_valid(form)


class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'

    def get_initial(self):
        initial = {'transaction_type': WITHDRAWAL}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account

        # Check if the bank is bankrupt
        if account.is_bankrupt:
            messages.error(
                self.request,
                "The bank is bankrupt, and withdrawals are not possible at this time."
            )
            return redirect('transaction_report')  # Redirect if the bank is bankrupt

        # Check if the user has enough balance for withdrawal
        if account.balance >= amount:
            account.balance -= amount
            account.save(update_fields=['balance'])

            messages.success(
                self.request,
                f"Successfully withdrawn {'{:,.2f}'.format(float(amount))}$ from your account."
            )
            return redirect('transaction_report')  # Redirect to transaction report after success
        else:
            # Insufficient funds: mark the bank as bankrupt
            account.is_bankrupt = True
            account.save(update_fields=['is_bankrupt'])

            messages.error(
                self.request,
                "The bank is now bankrupt, and no further withdrawals can be processed."
            )
            return redirect('transaction_report')  # Redirect to transaction report after failure
        
        return super().form_valid(form)  # This line can be removed as it's not necessary anymore

class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Request For Loan'

    def get_initial(self):
        initial = {'transaction_type': LOAN}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        current_loan_count = Transaction.objects.filter(
            account=self.request.user.account, transaction_type=3, loan_approve=True).count()
        if current_loan_count >= 3:
            return HttpResponse("You have crossed the loan limit")
        messages.success(
            self.request,
            f'Loan request for {"{:,.2f}".format(float(amount))}$ submitted successfully'
        )

        return super().form_valid(form)
    
class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = 'transactions/transaction_report.html'
    model = Transaction
    balance = 0

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.account
        )
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')
        
        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
            
            queryset = queryset.filter(timestamp__date__gte=start_date, timestamp__date__lte=end_date)
            self.balance = Transaction.objects.filter(
                timestamp__date__gte=start_date, timestamp__date__lte=end_date
            ).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance
       
        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })

        return context
    
class PayLoanView(LoginRequiredMixin, View):
    def get(self, request, loan_id):
        loan = get_object_or_404(Transaction, id=loan_id)
        if loan.loan_approve:
            user_account = loan.account
            if loan.amount < user_account.balance:
                user_account.balance -= loan.amount
                loan.balance_after_transaction = user_account.balance
                user_account.save()
                loan.loan_approved = True
                loan.transaction_type = LOAN_PAID
                loan.save()
                return redirect('transactions:loan_list')
            else:
                messages.error(
                    self.request,
                    f'Loan amount is greater than available balance'
                )

        return redirect('loan_list')


class LoanListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/loan_request.html'
    context_object_name = 'loans'
    
    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transaction.objects.filter(account=user_account, transaction_type=3)
        return queryset
    
from decimal import Decimal

class TransferMoneyView(LoginRequiredMixin, View):
    template_name = 'transactions/transfer.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        sender_account = request.user.account
        recipient_account_number = request.POST.get("recipient_account")
        transfer_amount = request.POST.get("amount")

        try:
            if not transfer_amount:
                raise ValueError("Transfer amount is required.")
            transfer_amount = Decimal(transfer_amount)
            if transfer_amount <= 0:
                raise ValueError("Transfer amount must be positive.")

            recipient_account = UserBankAccount.objects.get(account_no=recipient_account_number)

            if sender_account == recipient_account:
                messages.error(request, "You cannot transfer to your own account.")
                return render(request, self.template_name)

            if sender_account.balance >= transfer_amount:
                sender_account.balance -= transfer_amount
                sender_account.save()

                recipient_account.balance += transfer_amount
                recipient_account.save()

                Transaction.objects.create(
                    account=sender_account,
                    amount=transfer_amount,
                    balance_after_transaction=sender_account.balance,
                    transaction_type=TRANSFER,
                )
                Transaction.objects.create(
                    account=recipient_account,
                    amount=transfer_amount,
                    balance_after_transaction=recipient_account.balance,
                    transaction_type=DEPOSIT,
                )

                messages.success(request, f'Transferred ${transfer_amount:,.2f} successfully.')
                return redirect('transaction_report')

            else:
                messages.error(request, "Insufficient funds to complete the transfer.")

        except UserBankAccount.DoesNotExist:
            messages.error(request, "Recipient account not found.")
        except ValueError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, f"An unexpected error occurred: {str(e)}")

        return render(request, self.template_name)
