from master.models import *
from rest_framework import serializers

class MASSlmSerializer(serializers.ModelSerializer):

    class Meta:
        model = MASSlm
        fields = "__all__"
