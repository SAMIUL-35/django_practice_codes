from django.shortcuts import render
from datetime import datetime

def practice(request):
    data={
        'name':'nafi',
        'des':['my','name','is','samiul'],
        'curdat':datetime.now(),
        'defa':'',
        'num':50,
        'lst1':[1,2,3,4],
        'lst2':[5,6,7,8],
        'fun':"python is fun",
        'd':[
    {'name': 'Josh', 'age': 19},
    {'name': 'Dave', 'age': 22},
    {'name': 'Joe', 'age': 31},
],
    }
    return render(request, 'filter/practice.html',data)  

