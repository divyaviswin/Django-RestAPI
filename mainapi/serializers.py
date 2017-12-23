from rest_framework import serializers
from .models import Pet
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    pets = serializers.PrimaryKeyRelatedField(many=True, queryset=Pet.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'user')
class PetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    #user = serializers.CharField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Pet
        fields =('pk','type','name','birthday','owner')

