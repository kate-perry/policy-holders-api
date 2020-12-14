from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from policyholders.models import PolicyHolder, InsuredEvent
from policyholders.serializers import PolicyHolderSerializer, InsuredEventSerializer
from rest_framework.decorators import api_view

# Policy Holders
@api_view(['GET', 'POST', 'DELETE'])
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

    elif request.method == 'DELETE':
        count = PolicyHolder.objects.all().delete()
        return JsonResponse({'message': '{} Policy Holders were deleted successfully.'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def policyholder_detail(request, pk):
    try: 
        policyholder = PolicyHolder.objects.get(pk=pk) 
    except PolicyHolder.DoesNotExist: 
        return JsonResponse({'message': 'The policy does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        policyholder_serializer = PolicyHolderSerializer(policyholder)
        return JsonResponse(policyholder_serializer.data)

    elif request.method == 'PUT':
        policyholder_data = JSONParser().parse(request)
        policyholder_serializer = PolicyHolderSerializer(policyholder, data=policyholder_data)
        if policyholder_serializer.is_valid():
            policyholder_serializer.save()
            return JsonResponse(policyholder_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(policyholder_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        policyholder.delete()
        return JsonResponse({'message': 'Policy Holder was deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
 

 # Insured Events
@api_view(['GET', 'POST', 'DELETE'])
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

    elif request.method == 'DELETE':
        count = InsuredEvent.objects.all().delete()
        return JsonResponse({'message': '{} Policy Holders were deleted successfully.'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def insuredevent_detail(request, pk):
    # find insured event by id (pk)
    try: 
        insuredEvent = InsuredEvent.objects.get(pk=pk) 
    except InsuredEvent.DoesNotExist: 
        return JsonResponse({'message': 'The event does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        insuredEvent_serializer = InsuredEventSerializer(insuredEvent)
        return JsonResponse(insuredEvent_serializer.data)

    elif request.method == 'PUT':
        insuredEvent_data = JSONParser().parse(request)
        insuredEvent_serializer = InsuredEventSerializer(insuredEvent, data=insuredEvent_data)
        if insuredEvent_serializer.is_valid():
            insuredEvent_serializer.save()
            return JsonResponse(insuredEvent_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(insuredEvent_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        insuredEvent.delete()
        return JsonResponse({'message': 'Policy Holder was deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET'])
def insuredevent_list_by_policyholder(request, fk):
    # find insured event by policy holder id (fk)
    insuredEvents = InsuredEvent.objects.filter(policyHolderId=fk)
    if request.method == 'GET':
        insuredEvent_serializer = InsuredEventSerializer(insuredEvents, many=True)
        return JsonResponse(insuredEvent_serializer.data, safe=False)