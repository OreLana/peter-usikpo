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
        


