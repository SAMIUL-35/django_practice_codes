from django.shortcuts import render
def home(request):
   data={
      'name':'samiul',
      'roll':'45',
      'salary':'120000'
   }
   return  render (request,'home.html',data)
