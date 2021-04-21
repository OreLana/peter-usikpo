from django.urls import path
from pugapi.views.newsletter import AllNewsletterView

app_name = 'pugapi'


urlpatterns = [
    path('newsletter', AllNewsletterView.as_view(), name="all_newsletter"),

]