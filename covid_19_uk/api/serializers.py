from rest_framework import serializers


class UkTotalSerializer(serializers.Serializer):
    date = serializers.DateField()
    tests = serializers.IntegerField()
    confirmed_cases = serializers.IntegerField()
    deaths = serializers.IntegerField()
