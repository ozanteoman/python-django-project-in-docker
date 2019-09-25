"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from public_api.views import index, DocumentCreateView, PrivateDocumentCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('amazon-image-upload', DocumentCreateView.as_view(), name='amazon-image-upload'),
    path('private-amazon-image-upload', PrivateDocumentCreateView.as_view(), name='private-amazon-image-upload')
]
