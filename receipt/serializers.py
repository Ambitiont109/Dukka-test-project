from rest_framework import serializers


class ReceiptSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()
    phone_number = serializers.CharField()
    total_amount = serializers.FloatField()
