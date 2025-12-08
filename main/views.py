from django.shortcuts import render
from .models import *

def home(req):
    context = {
        'skills': Skill.objects.all()[:20],
        'projects': Project.objects.all()[:10],
        'experience': Experience.objects.all()[:5],
        'education': Education.objects.all()[:5],
        'certifications': Certification.objects.all()[:5],
        'personal_info': PersonalInfo.objects.first(),
    }
    return render(req, 'home.html', context)
# Create your views here.
