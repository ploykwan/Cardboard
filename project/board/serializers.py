#
#   Standard imports
#
from rest_framework import serializers


#
#   Classes
#


class CreateCardRequestSerializer(serializers.Serializer):
    CATEGORY_CHOICES = ['Do first', 'Schedule', 'Delegate', "Don't do"]

    title = serializers.CharField()
    description = serializers.CharField()
    category = serializers.ChoiceField(choices=CATEGORY_CHOICES)
