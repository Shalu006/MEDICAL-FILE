from rest_framework import serializers
from .models import MedicalLead

class MedicalLeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalLead
        fields = '__all__' 