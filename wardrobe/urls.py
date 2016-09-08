"""wardrobe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from outfit_organizer.views import (SeasonListView, SeasonOutfitListView,
                                    ClothingTypeListView, ClothingTypeSetView,
                                    PieceListView, PieceDetailView)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^seasons/$', SeasonListView.as_view()),
    url(r'^seasons/(?P<pk>[0-9]+)/$', SeasonOutfitListView.as_view()),
    url(r'^pieces/$', PieceListView.as_view()),
    url(r'^pieces/(?P<pk>[0-9]+)/$', PieceDetailView.as_view()),
    url(r'^clothing_type$', ClothingTypeListView.as_view()),
    url(r'^clothing_type/(?P<piece_type>[0-9A-Za-z]+)/$', ClothingTypeSetView.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
