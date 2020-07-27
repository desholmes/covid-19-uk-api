from rest_framework import serializers


class TotalSerializer(serializers.Serializer):
    date = serializers.DateField()
    tests = serializers.IntegerField()
    confirmed_cases = serializers.IntegerField()
    deaths = serializers.IntegerField()
    deaths_daily = serializers.IntegerField()
    deaths_daily_sma_7 = serializers.IntegerField()
