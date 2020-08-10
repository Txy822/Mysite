from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cv_section_list(request):
    cv_sections = Cv_section.objects.all()
    return render(request, 'cv/cv_section_list.html', {'cv_sections': cv_sections})
