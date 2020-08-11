from django.shortcuts import render
from django.utils import timezone
from .models import Cv_section
from django.shortcuts import render, get_object_or_404
# from .forms import Cv_section_form
from django.shortcuts import redirect


# Create your views here.

def cv_section_list(request):
    # cv_sections = Cv_section.objects.all()
    return render(request, 'cv/cv_sections_list.html', {})
