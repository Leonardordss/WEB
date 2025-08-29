from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__al__'
        many = True


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__al__'
        many = True

class AccountTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountToken
        fields = '__al__'
        many = True

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = '__al__'
        many = True


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__al__'
        many = True


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = '__al__'
        many = True