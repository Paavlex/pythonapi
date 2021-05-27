from rest_framework import serializers
from .models import Vulnerability

#Vytvoreni serializatoru

class VulnerabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vulnerability
        #urceni poli
        fields = ('id', 'name', 'cvss_score', 'cvss_vector', 'owasp_score', 'date')