from django.urls import path
from pugapi.views.newsletter import AllNewsletterView, DetaillNewsletterView

app_name = 'pugapi'


urlpatterns = [
    path('newsletter', AllNewsletterView.as_view(), name="all_newsletter"),
    path('newsletter/1', DetaillNewsletterView.as_view(), name="detail_newsletter"),

]