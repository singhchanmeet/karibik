from django.contrib import admin
from . models import Enrollment
# Register your models here.
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'programme_to_apply', 'candidate_name', 'photograph_preview']
    
admin.site.register(Enrollment, EnrollmentAdmin)