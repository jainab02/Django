from rest_framework import serializers

from sampleApp.models import *

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model= Sample
        fields = '__all__'
class EmpSerializer(serializers.ModelSerializer):
    
    # company = SampleSerializer(read_only=True,many= True)
    # company_name = SampleSerializer()
    # company_name = serializers.StringRelatedField(source='company_name.name')
    # company = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model= Employee
        fields = '__all__'