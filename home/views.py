#
#
#
#
#
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from .models import Event, Review
from django.core.paginator import Paginator
from .forms import ReviewForm


class HomePageView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_list = Review.objects.filter(status=Review.APPROVED)
        context['review_list'] = review_list
        context['form'] = ReviewForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.status = Review.PENDING
            review.save()
            return redirect('home')

        return self.get(request, *args, **kwargs)


class ToateVideoclipurilePageView(TemplateView):
    template_name = 'home/evenimente-constanta-nunta-botez-majorat-si-altele.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event_list = Event.objects.all().order_by('-id')
        print(event_list)

        paginator = Paginator(event_list, 12)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        return context


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
