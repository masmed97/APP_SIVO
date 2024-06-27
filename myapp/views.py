from rest_framework import generics
from .models import ConsUserGroup, MaintWorkOrderCheckList, MaintWorkOrderHeader, EqupEquipment
from .serializers import ConsUserGroupSerializer, MaintWorkOrderCheckListSerializer, MaintWorkOrderHeaderSerializer, EqupEquipmentSerializer

# ConsUserGroup API Views
class ConsUserGroupListCreateAPIView(generics.ListCreateAPIView): 
    #ListCreateAPIView: Provides GET (list) and POST (create) methods
    queryset = ConsUserGroup.objects.all()
    serializer_class = ConsUserGroupSerializer

class ConsUserGroupRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView): 
    #RetrieveUpdateDestroyAPIView: Provides GET (retrieve), PUT (update), PATCH (partial update), and DELETE (destroy) methods.
    queryset = ConsUserGroup.objects.all()
    serializer_class = ConsUserGroupSerializer

# MaintWorkOrderCheckList API Views
class MaintWorkOrderCheckListListCreateAPIView(generics.ListCreateAPIView):
    queryset = MaintWorkOrderCheckList.objects.all()
    serializer_class = MaintWorkOrderCheckListSerializer

class MaintWorkOrderCheckListRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintWorkOrderCheckList.objects.all()
    serializer_class = MaintWorkOrderCheckListSerializer

# MaintWorkOrderHeader API Views
class MaintWorkOrderHeaderListCreateAPIView(generics.ListCreateAPIView):
    queryset = MaintWorkOrderHeader.objects.all()
    serializer_class = MaintWorkOrderHeaderSerializer

class MaintWorkOrderHeaderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaintWorkOrderHeader.objects.all()
    serializer_class = MaintWorkOrderHeaderSerializer

# EqupEquipment API Views
class EqupEquipmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = EqupEquipment.objects.all()
    serializer_class = EqupEquipmentSerializer

class EqupEquipmentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EqupEquipment.objects.all()
    serializer_class = EqupEquipmentSerializer
