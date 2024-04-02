from django.shortcuts import render
from .models import *

def home(Request):
    blogdata = Blog.objects.all().order_by("id").reverse()[:3]
    eventdata = Event.objects.all().order_by("id").reverse()[:3]
    return render(Request,"index.html",{"blogdata":blogdata,"eventdata":eventdata})

def about(Request):
    teamdata = Team.objects.all()
    return render(Request,"about.html",{"teamdata":teamdata})

def faqPage(Request):
    return render(Request,"faq.html")

def admissionPage(Request):
    return render(Request,"admission.html")

def locationPage(Request):
    return render(Request,"location.html")

def eventPage(Request):
    eventdata = Event.objects.all().order_by("id").reverse()
    return render(Request,"event.html",{"eventdata":eventdata})

def eventSinglePage(Request,id):
    eventdataSingle = Event.objects.get(id=id)
    return render(Request,"blog.html",{"eventdataSingle":eventdataSingle})

def blogPage(Request):
    blogdata = Blog.objects.all().order_by("id").reverse()
    return render(Request,"blog.html",{"blogdata":blogdata})

def blogSinglePage(Request,id):
    blogdataSingle = Blog.objects.get(id=id)
    return render(Request,"blog.html",{"blogdataSingle":blogdataSingle})

def contactPage(Request):
    return render(Request,"contact.html")

def studentPage(Request):
    return render(Request,"student.html")

def schoolloginPage(Request):
    return render(Request,"schoollogin.html")

def paynowPage(Request):
    return render(Request,"paynow.html")