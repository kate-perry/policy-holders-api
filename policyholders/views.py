from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from policyholders.models import PolicyHolder, InsuredEvent
from policyholders.serializers import PolicyHolderSerializer, InsuredEventSerializer
from rest_framework.decorators import api_view


# GET list of policy holders, POST a new policy holder, DELETE all policy holders
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
    # find policy holder by id (pk)
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
 