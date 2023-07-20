from rest_framework import viewsets, mixins

from registry.models import Sample, Type
from inventory.models import Container, Location

from api import serializers


class ReadOnlyViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    pass


class SampleViewSet(ReadOnlyViewSet):
    queryset = Sample.objects.all()
    serializer_class = serializers.SampleSerializer


class TypeViewSet(ReadOnlyViewSet):
    queryset = Type.objects.all()
    serializer_class = serializers.TypeSerializer


class ContainerViewSet(ReadOnlyViewSet):
    queryset = Container.objects.all()
    serializer_class = serializers.ContainerSerializer


class LocationViewSet(ReadOnlyViewSet):
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer
