from rest_framework import serializers
from profiles.models import Projects,Rated,Userbio


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class RatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rated
        fields = '__all__'

class UserbioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userbio
        fields = '__all__'