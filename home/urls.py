from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name="home"),
    path('evenimente-constanta-nunta-botez-majorat-si-altele', views.ToateVideoclipurilePageView.as_view(), name="evenimente-constanta-nunta-botez-majorat-si-altele"),
    path('despre-mine', views.DespreMinePageView.as_view(), name="despre-mine"),
    path('contact-constanta', views.ContactPageView.as_view(), name="contact-constanta"),
]
