from django.contrib import admin
from .models import Profile, s_RepairRequest, h_RepairRequest

# Register your models here.
admin.site.register(Profile)
admin.site.register(s_RepairRequest)
admin.site.register(h_RepairRequest)