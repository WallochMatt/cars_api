from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dealership
from .serializers import DealershipSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def dealership_list(request):
    if request.method == 'GET':
        dealers = Dealership.objects.all()
        serializer = DealershipSerializer(dealers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DealershipSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def dealer_detail(request, pk):
    dealer  = get_object_or_404(Dealership, pk=pk)
    if request.method == 'GET':
        serializer = DealershipSerializer(dealer)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DealershipSerializer(dealer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        dealer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)