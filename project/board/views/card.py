#
#   Standard imports
#
from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

#
#   Local imports
#
from board.models import Card
from board.serializers import CreateCardRequestSerializer


#
#   Classes
#
class CreateCaredAPIView(GenericAPIView):
    def post(self, request):
        serializer = CreateCardRequestSerializer(data=request.data)
        if not serializer.is_valid():
            response_dict = {'message': f'request payload is invalid,{serializer.errors}'}
            return Response(data=response_dict, status=status.HTTP_400_BAD_REQUEST)
        validated_data = serializer.validated_data

        try:
            author = User.objects.get(username=request.user)
        except ObjectDoesNotExist:
            response_dict = {'message': 'User not found.'}
            return Response(data=response_dict, status=status.HTTP_400_BAD_REQUEST)

        card = Card.objects.create(title=validated_data['title'], description=validated_data['description'],
                                   category=validated_data['category'], author=author)
        response_dict = {
            'id': card.id,
            'title': card.title,
            'description': card.description,
            'category': card.category,
            'author': card.author.username,
            'created_at': card.created_at
        }
        return Response(data=response_dict, status=status.HTTP_200_OK)


class GetCardDetailAPIView(GenericAPIView):
    def get(self, request, *args, **kwargs):
        card_id = kwargs.get('card_id')
        try:
            card = Card.objects.get(id=card_id)
        except ObjectDoesNotExist:
            response_dict = {'message': 'Card not found.'}
            return Response(data=response_dict, status=status.HTTP_400_BAD_REQUEST)
        response_dict = {
            'title': card.title,
            'description': card.description,
            'category': card.category,
            'author': card.author.username,
            'created_at': card.created_at
        }
        return Response(data=response_dict, status=status.HTTP_200_OK)


class DeleteCardAPIView(GenericAPIView):
    def post(self, request):
        try:
            author = User.objects.get(username=request.user)
        except ObjectDoesNotExist:
            response_dict = {'message': 'User not found.'}
            return Response(data=response_dict, status=status.HTTP_400_BAD_REQUEST)

        card_id = request.data.get('card_id')
        try:
            card = Card.objects.get(id=card_id)
        except ObjectDoesNotExist:
            response_dict = {'message': 'Card not found.'}
            return Response(data=response_dict, status=status.HTTP_400_BAD_REQUEST)

        if not card.author == author:
            response_dict = {'message': 'The author not has permission.'}
            return Response(data=response_dict, status=status.HTTP_400_BAD_REQUEST)

        card.delete()
        return Response(data={}, status=status.HTTP_200_OK)
