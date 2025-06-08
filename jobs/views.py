# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import WalkInDrive
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    drives = WalkInDrive.objects.all().order_by('-date')
    return render(request, "jobs/home.html", {"drives": drives})


