from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.HyperlinkedModelSerializer):
	#user = serializers.CharField(default=serializers.CurrentUserDefault())
	class Meta:
		model = Pet
		fields =('pk','type','name','birthday')

