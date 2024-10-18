from django import forms
import datetime

BIRTH_YEAR_CHOICES = [x for x in range(1900, datetime.datetime.now().year + 1)]
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
class ApForm(forms.Form):  
    name = forms.CharField(max_length=20, label='Enter Your Name')
    email = forms.EmailField(max_length=30, label='Enter Your Email')
    password = forms.CharField(widget=forms.PasswordInput(), max_length=50)
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Enter Your Birthday', initial=datetime.date.today)
    value = forms.DecimalField(max_digits=10, decimal_places=2)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 1}), label='Enter Your Comment')
    agree = forms.BooleanField()
    roll_number = forms.IntegerField( 
                     help_text = "Enter 6 digit roll number"
                     ) 
    
    first_name = forms.CharField(initial='Your name')
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
