from django.shortcuts import render
from django.utils import timezone
from .models import Cv_section
from django.shortcuts import render, get_object_or_404
# from .forms import Cv_section_form
from django.shortcuts import redirect


# Create your views here.


def cv_section_list(request):
    cv_sections = Cv_section.objects.all()
    return render(request, 'cv/cv_sections_list.html', {'cv_sections': cv_sections})

def cv_section_detail(request, pk):
    cv_section = get_object_or_404(Cv_section, pk=pk)
    return render(request, 'cv/cv_section_detail.html', {'cv_section': cv_section})
