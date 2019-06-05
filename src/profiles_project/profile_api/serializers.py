from rest_framework import serializers

class HelloViewSerializer(serializers.Serializer):
    email = serializers.EmailField()
    name = serializers.CharField(max_length = 10)
