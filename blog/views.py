from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def starting_page(request):
  return render(request, 'index.html')

def posts(request):
  return HttpResponse("Start")

def individual_post(request):
  return HttpResponse("Start")