from django.contrib import admin
from .models import ConsUserGroup, MaintWorkOrderCheckList, MaintWorkOrderHeader, EqupEquipment

admin.site.register(ConsUserGroup)
admin.site.register(MaintWorkOrderCheckList)
admin.site.register(MaintWorkOrderHeader)
admin.site.register(EqupEquipment)
