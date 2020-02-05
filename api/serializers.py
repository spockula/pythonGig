from rest_framework import serializers
from .models import Users, GENDER_CHOICES

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    amount = serializers.CharField(max_length=100)
    gender = serializers.CharField(max_length = 150)
    
    password = serializers.CharField(max_length=255) 
    # is called if we save serializer if it do not have an instance
    def create(self, validated_data):
       password = validated_data.pop("password")
       user = Users.objects.create(**validated_data)
       if password:
           user.set_password(password)
           user.save()
       return user
    # is called if we save serializer if it have an instance
    def update(self, instance, validated_data):
       password = validated_data.pop("password")
       instance.__dict__.update(validated_data)
       if password:
           instance.set_password(password)
       instance.save()
       return instance

# model serializer [similar to forms.ModelForm]
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ("first_name", "last_name", "email", "amount", "gender", "userId", "is_active", "is_staff")