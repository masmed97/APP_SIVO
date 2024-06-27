from django.urls import path
from .views import (
    ConsUserGroupListCreateAPIView,
    ConsUserGroupRetrieveUpdateDestroyAPIView,
    MaintWorkOrderCheckListListCreateAPIView,
    MaintWorkOrderCheckListRetrieveUpdateDestroyAPIView,
    MaintWorkOrderHeaderListCreateAPIView,
    MaintWorkOrderHeaderRetrieveUpdateDestroyAPIView,
    EqupEquipmentListCreateAPIView,
    EqupEquipmentRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # ConsUserGroup URLs
    path('cons-user-groups/', ConsUserGroupListCreateAPIView.as_view(), name='cons-user-group-list-create'),
    path('cons-user-groups/<int:pk>/', ConsUserGroupRetrieveUpdateDestroyAPIView.as_view(), name='cons-user-group-detail'),

    # MaintWorkOrderCheckList URLs
    path('maint-work-order-check-lists/', MaintWorkOrderCheckListListCreateAPIView.as_view(), name='maint-work-order-check-list-list-create'),
    path('maint-work-order-check-lists/<int:pk>/', MaintWorkOrderCheckListRetrieveUpdateDestroyAPIView.as_view(), name='maint-work-order-check-list-detail'),

    # MaintWorkOrderHeader URLs
    path('maint-work-order-headers/', MaintWorkOrderHeaderListCreateAPIView.as_view(), name='maint-work-order-header-list-create'),
    path('maint-work-order-headers/<int:pk>/', MaintWorkOrderHeaderRetrieveUpdateDestroyAPIView.as_view(), name='maint-work-order-header-detail'),

    # EqupEquipment URLs
    path('equp-equipments/', EqupEquipmentListCreateAPIView.as_view(), name='equp-equipment-list-create'),
    path('equp-equipments/<int:pk>/', EqupEquipmentRetrieveUpdateDestroyAPIView.as_view(), name='equp-equipment-detail'),
]
