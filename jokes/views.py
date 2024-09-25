import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from jokes.models import Joke
from jokes.serializers import JokeSerializer


class JokeApiView(APIView):
    """This class handles differents
    HTTP methods as GET, POST
    for Joke entity"""

    def get(self, request):
        """This method retrieve a random joke from 
        external API if received Chuck as query param.
        Else, return a list of jokes that exists in DB"""
        query_param = request.GET.get('query')

        if query_param and query_param.lower() == "chuck":
            res = requests.get('https://api.chucknorris.io/jokes/random', timeout=30)

            if res.status_code != 200:
                return Response(
                    {'error': 'Failed to fetch joke from external API.'},
                    status=status.HTTP_503_SERVICE_UNAVAILABLE
                )

            joke_description = res.json().get('value', 'Not joke found')

            return Response({'joke': joke_description}, status=status.HTTP_200_OK)

        joke = Joke.objects.order_by('?').first()

        if not joke:
            return Response(
                {'error': 'No jokes available in the database.'},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = JokeSerializer(joke)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """This method register new joke in DB"""
        serializer = JokeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    'message': "Joke saved successfully",
                    'joke': serializer.data
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """This method update an specific
        joke resource"""

        joke_id = request.data.get('id', None)
        if not joke_id:
            return Response(
                {'error': 'Joke ID is required for update.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            joke = Joke.objects.get(id=joke_id)
        except Joke.DoesNotExist:
            return Response({'error': 'Joke not found.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = JokeSerializer(joke, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {'message': 'Joke updated successfully.', 'joke': serializer.data},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """This method delete a specific
        joke by a given number id"""

        joke_id = request.query_params.get('number', None)

        if not joke_id:
            return Response(
                {'error': 'Joke ID (number) is required for deletion.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            joke = Joke.objects.get(id=joke_id)
            joke.delete()
            return Response({'message': 'Joke deleted successfully.'}, status=status.HTTP_200_OK)
        except Joke.DoesNotExist:
            return Response({'error': 'Joke not found.'}, status=status.HTTP_404_NOT_FOUND)
