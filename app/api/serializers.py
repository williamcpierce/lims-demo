from rest_framework.serializers import ModelSerializer

from registry.models import Sample, Type
from inventory.models import Container, Location


# Serializers for ForeignKey and ManyToManyField
class TypeRefSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = ("id", "name", "prefix")


class SampleRefSerializer(ModelSerializer):
    class Meta:
        model = Sample
        fields = ("id", "name")


class LocationRefSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "name", "hierarchy")


# Model serializers
class SampleSerializer(ModelSerializer):
    type = TypeRefSerializer()
    related = SampleRefSerializer()

    class Meta:
        model = Sample
        fields = (
            "id",
            "type",
            "related",
            "alias",
            "name",
            "sequence",
        )


class TypeSerializer(ModelSerializer):
    class Meta:
        model = Type
        fields = "__all__"
        depth = 1


class ContainerSerializer(ModelSerializer):
    location = LocationRefSerializer()
    contents = SampleRefSerializer(many=True)

    class Meta:
        model = Container
        fields = "__all__"


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = ("id", "name", "hierarchy")
