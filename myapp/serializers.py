from rest_framework import serializers
from .models import ConsUserGroup, MaintWorkOrderCheckList, MaintWorkOrderHeader, EqupEquipment

class ConsUserGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsUserGroup
        fields = '__all__'


class MaintWorkOrderCheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintWorkOrderCheckList
        fields = '__all__'


class MaintWorkOrderHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintWorkOrderHeader
        fields = '__all__'


class EqupEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EqupEquipment
        fields = '__all__'
