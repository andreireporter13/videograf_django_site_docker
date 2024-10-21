#
#
#
#
#
from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from .models import Event
from django.core.paginator import Paginator


# get reviews from google ->
#
def fetch_google_reviews(api_key, place_id):
    client = Client(api_key)
    fields = ["rating", "reviews"]

    try:
        place_details = client.place(place_id=place_id, fields=fields)
        average_rating = place_details.get("result", {}).get("rating")
        reviews = place_details.get("result", {}).get("reviews", [])

        structured_reviews = [
            {
                'author_name': review.get('author_name'),
                'text': review.get('text'),
                'rating': review.get('rating'),
                'profile_photo_url': review.get('profile_photo_url'),
            }
            for review in reviews
        ]
        
        return {
            'average_rating': average_rating,
            'reviews': structured_reviews,
            'error': None
        }
    except googlemaps.exceptions.ApiError as e:
        return {
            'average_rating': None,
            'reviews': [],
            'error': f"Google Maps API error: {e}"
        }
    except Exception as e:
        return {
            'average_rating': None,
            'reviews': [],
            'error': f"Unexpected error occurred: {e}"
        }


class HomePageView(TemplateView):
    template_name = 'home/home.html'

# class HomePageView(TemplateView):
#     template_name = 'home/home.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # Replace with your actual API key and Place ID
#         api_key = "YOUR_API_KEY"  
#         place_id = "ChIJoZqnday3lzMR9WJ8w09DCn0"

#         # Fetch reviews using the function
#         reviews_data = fetch_google_reviews(api_key, place_id)

#         # Add data to context
#         context['average_rating'] = reviews_data['average_rating']
#         context['reviews'] = reviews_data['reviews']
#         context['error'] = reviews_data['error']

#         return context

################################

# <h1>Welcome to Our Home Page</h1>

# {% if error %}
#     <p style="color: red;">{{ error }}</p>
# {% else %}
#     {% if average_rating %}
#         <p>Average Rating: {{ average_rating }}</p>
#     {% else %}
#         <p>No ratings available.</p>
#     {% endif %}

#     {% if reviews %}
#         <h2>Customer Reviews:</h2>
#         <ul>
#             {% for review in reviews %}
#                 <li>
#                     {% if review.profile_photo_url %}
#                         <img src="{{ review.profile_photo_url }}" alt="{{ review.author_name }}" style="width: 50px; height: 50px; border-radius: 50%;">
#                     {% endif %}
#                     <strong>{{ review.author_name }}:</strong> {{ review.text }} (Rating: {{ review.rating }})
#                 </li>
#             {% endfor %}
#         </ul>
#     {% else %}
#         <p>No reviews available.</p>
#     {% endif %}
# {% endif %}


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
