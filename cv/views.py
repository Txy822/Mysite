from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cv_section_list(request):
    return render(request, 'cv/cv_sections_list.html')
