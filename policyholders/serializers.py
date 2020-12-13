from rest_framework import serializers
from policyholders.models import PolicyHolder, InsuredEvent


class PolicyHolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PolicyHolder
        fields = ('id',
                  'gender', 
                  'dob', 
                  'ssn', 
                  'smoking', 
                  'allergies', 
                  'conditions')

class InsuredEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuredEvent
        fields = ('id',
                  'policyHolderId', 
                  'doi', 
                  'type', 
                  'billedAmount', 
                  'coveredAmount',)