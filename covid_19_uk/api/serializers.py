from rest_framework import serializers


class EnglandTotalSerializer(serializers.Serializer):
    date = serializers.DateField()
    tests = serializers.IntegerField()
    confirmed_cases = serializers.IntegerField()
    deaths = serializers.IntegerField()
