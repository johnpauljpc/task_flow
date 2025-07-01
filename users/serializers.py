from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

from django.contrib.auth import get_user_model
User = get_user_model()
# Making email field to be case insensitive
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Lowercase the email before authentication
        attrs['email'] = attrs['email'].lower()
        return super().validate(attrs)

# serializer for user registration
class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only = True, style={'input_type':"password"})
    password = serializers.CharField(write_only = True, style={'input_type':"password"})
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Passwords does not match!")
        attrs['email'] = (attrs["email"]).lower()
        return super().validate(attrs)
    
 
    def create(self, validated_data):
        validated_data.pop("confirm_password") #removes the confirm password from the data
        user = User.objects.create_user(**validated_data)
        return user