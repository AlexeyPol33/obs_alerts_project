from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import Token
from .models import User, Configurations, DonationBar, MessageAlert


class UserSerializer(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ['id', 'username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.is_active=True
        user.save()
        return user
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)


class ObtainTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user) -> Token:
        token = super().get_token(user)
        token['username'] = user.username
        return token


class DonationBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationBar
        fields = ['id', 'image', 'display_url', 'description', 'target_value']
        extra_kwargs = {
            'id': {'read_only': True},
            'display_url': {'read_only': True},
            'current_value': {'read_only': True},
        }

    def create(self, validated_data:dict) -> DonationBar:
        donation_bar = DonationBar.objects.create(
            image = validated_data.get('image'),
            description = validated_data.get('description'),
            target_value = validated_data.get('target_value')
        )
        return donation_bar

    def update(self, instance: DonationBar, validated_data: dict) -> DonationBar:
        instance.image = validated_data.get('image')
        instance.description = validated_data.get('description'),
        instance.target_value = validated_data.get('target_value')
        instance.save()
        return instance



class MessageAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageAlert
        fields = ['id', 'image', 'display_url', 'sound']
        extra_kwargs = {
            'id': {'read_only': True},
            'display_url': {'read_only': True},
            'sended_money': {'read_only': True}
        }

    def create(self, validated_data: dict) -> MessageAlert:
        message_alert = MessageAlert.objects.create(
            image = validated_data.get('image'),
            sound = validated_data.get('sound')
        )
        return message_alert

    def update(self, instance: MessageAlert, validated_data: dict) -> MessageAlert:
        instance.image = validated_data.get('image')
        instance.sound = validated_data.get('sound')
        instance.save()
        return instance