from rest_framework import serializers


class TestSerializer(serializers.Serializer):
    date = serializers.CharField(max_length=10)
    tests = serializers.IntegerField()
    confirmed_cases = serializers.IntegerField()
    deaths = serializers.IntegerField()
