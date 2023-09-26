from crm.models import *
from rest_framework import serializers

class CrmLedSerializer(serializers.ModelSerializer):

    class Meta:
        model = CRMLed
        fields = "__all__"
