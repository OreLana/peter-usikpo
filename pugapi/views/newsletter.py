from rest_framework.views import APIView
from rest_framework.response import Response
from pugapi.models.newsletter import Newsletter
from pugapi.serializers.newsletter import NewsletterSerializer


class AllNewsletterView(APIView):

    def get(self, request):
        """Returns a list of all the newsletters"""
        newsletters = Newsletter.objects.all()
        serializer = NewsletterSerializer(newsletters, many=True)
        return Response(serializer.data)
        
class DetaillNewsletterView(APIView):

    def get(self, request, id):
        """Returns a newsletter with the id passed"""
        newsletter = Newsletter.objects.filter(pk=id)
        serializer = NewsletterSerializer(newsletter)
        return Response(serializer.data)

