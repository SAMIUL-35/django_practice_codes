from django.shortcuts import render
from datetime import datetime
def home(request):
   data={
      'name':'samiul',
      'roll':'45',
      'salary':'120000',
      'lst':['s','a','d','k'],
      'num':5023,
      'value':'I’m Jai',
      'datetime':datetime.now(),
      'empty':'',
     'name_list':[
    {'name': 'zed', 'age': 19},
    {'name': 'amy', 'age': 22},
    {'name': 'joe', 'age': 31},
],
   }
   return  render (request,'home.html',data)
