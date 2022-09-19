from .models import Taxi, TaxiRequest
from .serializers import TaxiSerializer, TaxiRequestSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from geopy.distance import geodesic


@api_view(['GET', 'PUT', 'DELETE'])
def taxi_detail(request, pk, format=None):
    try:
        taxi = Taxi.objects.get(pk=pk)
    except Taxi.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaxiSerializer(taxi)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaxiSerializer(taxi, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        taxi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def request_list(request, tid, format=None):
    if request.method == 'GET':
        taxis = TaxiRequest.objects.filter(taxi=tid).order_by('requestTime')
        serializer = TaxiRequestSerializer(taxis, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = TaxiRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def request_detail(request, pk, format=None):
    try:
        req = TaxiRequest.objects.get(pk=pk)
    except TaxiRequest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaxiRequestSerializer(req)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TaxiRequestSerializer(req, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        req.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_request(request, format=None):
    x, y = request.data.get('coordX'), request.data.get('coordY')

    if not (x and y):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    taxi = Taxi.objects.filter(pk=request.data.get('taxi'))[0]

    point1 = (x, y)
    point2 = (taxi.coordX, taxi.coordY)
    distance = geodesic(point1, point2).kilometers

    request.data['distance'] = round(distance, 4)
    serializer = TaxiRequestSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
