from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all(), message='Email Already Registered',)]
            )
    username = serializers.CharField(
            max_length=32,
            validators=[UniqueValidator(queryset=User.objects.all(), message='Username Already Taken')]
            )
    password = serializers.CharField(min_length=6, max_length=100, style={"input_type": "password"}, 
            write_only=True)

    def create(self, validated_data):
        user = User(email=validated_data['email'],
                username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email', 
            'password'
        )


class UserDetailSerializer(serializers.ModelSerializer):
        class Meta:
                model = User
                fields = [  
                        'id',
                        'username',
                        'email'
                ]

