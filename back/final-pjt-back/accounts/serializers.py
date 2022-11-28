from rest_framework import serializers
from .models import User
from community.serializers import ReviewSerializer

class UserSerializer(serializers.ModelSerializer):

  class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('followings', 'password')

class UserProfileSerializer(serializers.ModelSerializer):
    followers = UserSerializer(many=True)
    review = ReviewSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('followings', 'password', 'followers', 'review')
        

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        
class UserDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('is_active', )
        