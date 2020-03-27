from django.shortcuts import render
from django.http import HttpResponse

Config = {
  'apiKey': "AIzaSyD3eoC2havSFjPcBam86tHN6QPKrXyiX3I",
  'authDomain': "books-shelf-502d1.firebaseapp.com",
  'databaseURL': "https://books-shelf-502d1.firebaseio.com",
  'projectId': "books-shelf-502d1",
  'storageBucket': "books-shelf-502d1.appspot.com",
  'messagingSenderId': "297948301021",
  'appId': "1:297948301021:web:85cfbf36fdffbb790efd34",
  'measurementId': "G-M4GZE2ZVPT"
}


# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'register.html')
           
def subpage(request):
    return render(request,'subpage.html')