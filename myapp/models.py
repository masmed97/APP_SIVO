from django.db import models
from django.utils import timezone

class ConsUserGroup(models.Model): #affichage
    id_user = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    sec_group = models.CharField(max_length=50)
    f_read_only = models.SmallIntegerField()
    f_active = models.SmallIntegerField()
    f_locked = models.SmallIntegerField()
    f_bit_status = models.IntegerField()
    user_created = models.CharField(max_length=50, default='suser_sname()')
    user_modif = models.CharField(max_length=50, default='suser_sname()')
    date_created = models.DateTimeField()
    date_modif = models.DateTimeField()
    user_verify = models.CharField(max_length=50, null=True, blank=True)
    date_verify = models.DateTimeField(null=True, blank=True)
    iso_rev = models.IntegerField()

    class Meta:
        db_table = "CONS_USER_GROUP"
        unique_together = (("sec_group", "username"),)
        verbose_name_plural = "Cons User Groups"

    def __str__(self):
        return f"User {self.id_user}"



class MaintWorkOrderCheckList(models.Model): #affichage
    id_work_order_check_list = models.AutoField(primary_key=True)
    id_work_order_header = models.IntegerField()
    id_wo_check_list = models.IntegerField()
    line_no = models.IntegerField()
    f_done = models.BooleanField(default=False)
    note = models.CharField(max_length=6000, null=True, blank=True)
    f_read_only = models.SmallIntegerField()
    f_locked = models.SmallIntegerField()
    f_active = models.SmallIntegerField()
    f_bit_status = models.IntegerField()
    user_created = models.CharField(max_length=50)
    user_modif = models.CharField(max_length=50)
    user_verify = models.CharField(max_length=50, null=True, blank=True)
    date_created = models.DateTimeField()
    date_modif = models.DateTimeField()
    date_verify = models.DateTimeField(null=True, blank=True)
    iso_rev = models.IntegerField()
    minimal_limit = models.DecimalField(max_digits=18, decimal_places=6, null=True, blank=True)
    maximal_limit = models.DecimalField(max_digits=18, decimal_places=6, null=True, blank=True)
    nominal_value = models.DecimalField(max_digits=18, decimal_places=6, null=True, blank=True)
    input_value = models.DecimalField(max_digits=18, decimal_places=6, null=True, blank=True)
    f_non_compliant = models.BooleanField(default=False)
    id_equipment = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "MAINT_WORK_ORDER_CHECK_LIST"
        verbose_name_plural = "Maint Work Order Check Lists"

    def __str__(self):
        return f"Work Order Check List {self.id_work_order_check_list}"


class MaintWorkOrderHeader(models.Model): #create
    id_work_order_header = models.AutoField(primary_key=True)
    no_work_order_header = models.CharField(max_length=40)
    f_read_only = models.SmallIntegerField()
    f_locked = models.SmallIntegerField()
    f_active = models.SmallIntegerField()
    f_bit_status = models.IntegerField()
    user_created = models.CharField(max_length=30)
    user_modif = models.CharField(max_length=30)
    user_verify = models.CharField(max_length=30, null=True, blank=True)
    date_created = models.DateTimeField()
    date_modif = models.DateTimeField()
    date_verify = models.DateTimeField(null=True, blank=True)
    iso_rev = models.IntegerField()
    f_wo_corrective = models.BooleanField()
    f_wo_preventive = models.BooleanField()
    f_wo_service_call = models.BooleanField()
    id_equipment = models.IntegerField(null=True, blank=True)
    id_employee_receiver = models.IntegerField(null=True, blank=True)
    id_employee_sender = models.IntegerField(null=True, blank=True)
    id_wo_status = models.IntegerField(null=True, blank=True)
    id_expense_account = models.IntegerField(null=True, blank=True)
    id_wo_priority = models.IntegerField(null=True, blank=True)
    date_open = models.DateTimeField(null=True, blank=True)
    date_start = models.DateTimeField(null=True, blank=True)
    date_close = models.DateTimeField(null=True, blank=True)
    date_realisation = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    id_wo_repair_class = models.IntegerField(null=True, blank=True)
    other_took_action = models.CharField(max_length=2000, null=True, blank=True)
    id_work_order_header_parent = models.IntegerField(null=True, blank=True)
    id_work_order_header_preventive = models.IntegerField(null=True, blank=True)
    id_employee_responsible = models.IntegerField(null=True, blank=True)
    id_wo_request = models.IntegerField(null=True, blank=True)
    failure_time = models.DecimalField(max_digits=18, decimal_places=6)
    id_equipment_meter = models.IntegerField(null=True, blank=True)
    life_meter_estimate = models.IntegerField()
    diagnosis = models.CharField(max_length=500, null=True, blank=True)
    solution = models.CharField(max_length=500, null=True, blank=True)
    id_execution_mode = models.IntegerField(null=True, blank=True)
    f_archived = models.BooleanField()
    note = models.CharField(max_length=2000, null=True, blank=True)
    remark_request_code = models.CharField(max_length=2000, null=True, blank=True)
    small_remark = models.CharField(max_length=100, null=True, blank=True)
    remark = models.CharField(max_length=500, null=True, blank=True)
    id_section_tag = models.IntegerField(null=True, blank=True)
    f_wo_preventive_cfg = models.BooleanField()
    f_wo_work_request = models.BooleanField()
    work_request_state = models.CharField(max_length=8, null=True, blank=True)
    id_employee_approbation_wr = models.IntegerField(null=True, blank=True)
    date_approbation_wr = models.DateTimeField(null=True, blank=True)
    no_work_order_header_wr = models.CharField(max_length=40, null=True, blank=True)
    id_plant = models.IntegerField(null=True, blank=True)
    f_read = models.BooleanField()
    id_locking_procedure_header = models.IntegerField(null=True, blank=True)
    id_inspection_road = models.IntegerField(null=True, blank=True)
    id_calibration_sheet = models.IntegerField(null=True, blank=True)
    note_extra = models.TextField(null=True, blank=True)
    material_status = models.CharField(max_length=20, null=True, blank=True)
    total_time_plan = models.DecimalField(max_digits=18, decimal_places=6)
    f_wo_standard_task = models.BooleanField()
    id_wo_standard_task_type = models.IntegerField(null=True, blank=True)
    no_work_order_task_parent = models.CharField(max_length=40, null=True, blank=True)
    f_wo_anticipated = models.BooleanField()
    f_awaiting_approval = models.BooleanField()
    f_wo_prev_service_call = models.BooleanField()
    meter_emission_value = models.BigIntegerField()
    meter_closing_value = models.BigIntegerField()
    id_wo_standard_task_group = models.IntegerField(null=True, blank=True)
    id_wo_standard_task_category = models.IntegerField(null=True, blank=True)
    id_wo_standard_task_subcategory = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "MAINT_WORK_ORDER_HEADER"
        verbose_name_plural = "Maint Work Order Headers"

    def __str__(self):
        return f"Work Order Header {self.id_work_order_header}"



class EqupEquipment(models.Model): #affichage
    id_equipment = models.AutoField(primary_key=True)
    no_equipment = models.CharField(max_length=40)
    f_read_only = models.SmallIntegerField()
    f_locked = models.SmallIntegerField()
    f_active = models.SmallIntegerField()
    f_bit_status = models.IntegerField()
    user_created = models.CharField(max_length=30)
    user_modif = models.CharField(max_length=30)
    user_verify = models.CharField(max_length=30, null=True, blank=True)
    date_created = models.DateTimeField()
    date_modif = models.DateTimeField()
    date_verify = models.DateTimeField(null=True, blank=True)
    iso_rev = models.IntegerField()
    id_expense_account = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=120, null=True, blank=True)
    hour_rate = models.DecimalField(max_digits=18, decimal_places=6, null=True, blank=True)
    id_tool_group = models.IntegerField(null=True, blank=True)
    id_plant = models.IntegerField(null=True, blank=True)
    equipment_division = models.CharField(max_length=80, null=True, blank=True)
    equipment_location = models.CharField(max_length=80, null=True, blank=True)
    equipment_group = models.CharField(max_length=40, null=True, blank=True)
    guarantee_ending = models.DateTimeField(null=True, blank=True)
    drawing = models.CharField(max_length=255, null=True, blank=True)
    note = models.CharField(max_length=5000, null=True, blank=True)
    f_equipment_lock = models.BooleanField()
    id_equipment_meter = models.IntegerField(null=True, blank=True)
    meter_life_value = models.BigIntegerField(null=True, blank=True)
    equipment_photo = models.ImageField(null=True, blank=True)
    f_suite = models.BooleanField()
    area = models.CharField(max_length=60, null=True, blank=True)
    remark_equip_mechanism = models.CharField(max_length=2000, null=True, blank=True)
    id_equipment_group = models.IntegerField(null=True, blank=True)
    id_equipment_division = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    id_equipment_status = models.IntegerField(null=True, blank=True)
    id_equipment_criticality = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "EQUP_EQUIPMENT"
        verbose_name_plural = "Equp Equipment"

    def __str__(self):
        return f"Equipment {self.id_equipment}"

