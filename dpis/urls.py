from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("about/", views.about),
    path("faq/", views.faqPage),
    path("admission/", views.admissionPage),
    path("location/", views.locationPage),
    path("event/", views.eventPage),
    path("event-single/<int:id>/", views.eventSinglePage),
    path("blog/", views.blogPage),
    path("blog-single/<int:id>/", views.blogSinglePage),
    path("contact/", views.contactPage),
    path("student/", views.studentPage),
    path("schoollogin/", views.schoolloginPage),
    path("paynow/", views.paynowPage),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
