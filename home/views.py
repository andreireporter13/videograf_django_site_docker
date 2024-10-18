#
#
#
#
#
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect


class HomePageView(TemplateView):
    template_name = 'home/home.html'


class ToateVideoclipurilePageView(TemplateView):
    template_name = 'home/evenimente-constanta-nunta-botez-majorat-si-altele.html'


# class PortofoliuNuntaPageView(TemplateView):
#     template_name = 'general_site_pages/portofoliu-nunta-Constanta.html'


# class PortofoliuBotezPageView(TemplateView):
#     template_name = 'general_site_pages/portofoliu-botez.html'


# class PortofoliuAlteEvenimentePageView(TemplateView):
#     template_name = 'general_site_pages/portofoliu-alte-evenimente-Constanta.html'


class DespreMinePageView(TemplateView):
    template_name = 'home/despre-mine.html'


class ContactPageView(TemplateView):
    template_name = 'home/contact.html'
