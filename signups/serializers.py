from rest_framework import serializers
from signups.models import Usersignup


class UsersignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usersignup
        fields = ['username','useremail','phone','userimage']
