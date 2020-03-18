from rest_framework import serializers


class CaseSerializer(serializers.Serializer):
    date = serializers.DateField()
    country = serializers.CharField(max_length=10)
    area_code = serializers.CharField(max_length=15)
    area = serializers.CharField(max_length=50)
    total_cases = serializers.IntegerField()
