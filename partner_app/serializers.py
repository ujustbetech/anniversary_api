from rest_framework import serializers
from . models import partner,postimage

class partnerSerializer(serializers.ModelSerializer):
    class Meta:
        model=partner
        fields="__all__"
class postimageSerializer(serializers.ModelSerializer):
    class Meta:
        model=postimage
        fields="__all__"