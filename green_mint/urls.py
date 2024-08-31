"""
URL configuration for green_mint project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('gallery/', views.gallery, name="gallery"),
    path('facilities/', views.facilities, name="facilities"),
    path('reservation/', views.reservation, name="reservation"),
    path('faqs/', views.faqs, name="faqs"),
    path('destination/', views.destination, name="destination"),
    path('property-policies/', views.prop_policy, name="prop_policy"),
    path('rules-and-cancellation-policies/', views.rnc_policy, name="rnc_policy"),
    path('rooms/', views.rooms, name="rooms"),
    path('room/<slug>/', views.room_detail, name="room_detail"),
    path('thanks/', views.thanks, name="thanks"),

    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
