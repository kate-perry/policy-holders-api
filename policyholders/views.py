from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from policyholders.models import PolicyHolder, InsuredEvent
from policyholders.serializers import PolicyHolderSerializer, InsuredEventSerializer
from rest_framework.decorators import api_view

### Policy Holders
# GET and POST one-to-multiple policy holders
@api_view(['GET', 'POST'])
def policyholder_list(request):
    if request.method == 'GET':
        policyholders = PolicyHolder.objects.all()

        id = request.GET.get('id', None)
        if id is not None:
            policyholders = policyholders.filter(id__icontains=id)

        policyholders_serializer = PolicyHolderSerializer(policyholders, many=True)
        return JsonResponse(policyholders_serializer.data, safe=False)

    elif request.method == 'POST':
        policyholder_data = JSONParser().parse(request)
        policyholder_serializer = PolicyHolderSerializer(data=policyholder_data)
        if policyholder_serializer.is_valid():
            policyholder_serializer.save()
            return JsonResponse(policyholder_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(policyholder_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# GET a policy holder based on ID
@api_view(['GET'])
def policyholder_detail(request, pk):
    try: 
        policyholder = PolicyHolder.objects.get(pk=pk) 
    except PolicyHolder.DoesNotExist: 
        return JsonResponse({'message': 'The policy does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        policyholder_serializer = PolicyHolderSerializer(policyholder)
        return JsonResponse(policyholder_serializer.data)


### Insured Events
# GET and POST one-to-multiple insured events
@api_view(['GET', 'POST'])
def insuredevent_list(request):
    if request.method == 'GET':
        insuredEvents = InsuredEvent.objects.all()

        id = request.GET.get('id', None)
        if id is not None:
            insuredEvents = insuredEvents.filter(id__icontains=id)

        insuredEvents_serializer = InsuredEventsSerializer(insuredEvents, many=True)
        return JsonResponse(insuredEvents_serializer.data, safe=False)

    elif request.method == 'POST':
        insuredEvents_data = JSONParser().parse(request)
        insuredEvents_serializer = InsuredEventsSerializer(data=insuredEvents_data)
        if insuredEvents_serializer.is_valid():
            insuredEvents_serializer.save()
            return JsonResponse(insuredEvents_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(insuredEvents_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET an insured event based on ID
@api_view(['GET'])
def insuredevent_detail(request, pk):
    try: 
        insuredEvent = InsuredEvent.objects.get(pk=pk) 
    except InsuredEvent.DoesNotExist: 
        return JsonResponse({'message': 'The event does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        insuredEvent_serializer = InsuredEventSerializer(insuredEvent)
        return JsonResponse(insuredEvent_serializer.data)

# GET a list of insured events based on PolicyHolderId
@api_view(['GET'])
def insuredevent_by_policy_holder_list(request, fk):
    try: 
        insuredEvent = InsuredEvent.objects.get(fk=fk) 
    except InsuredEvent.DoesNotExist: 
        return JsonResponse({'message': 'The event does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        insuredEvent_serializer = InsuredEventSerializer(insuredEvent)
        return JsonResponse(insuredEvent_serializer.data)