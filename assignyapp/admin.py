from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# Register your models here.

# admin.site.register(COM121Lecturer)
# admin.site.register(COM211Lecturer)
# admin.site.register(GNS127Lecturer)
# admin.site.register(COM216Lecturer)
# admin.site.register(ICT211Lecturer)

# admin.site.register(COM216Student)
admin.site.register(Student)
admin.site.register(Lecturer)
# admin.site.register(Score)





class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['pk', 'email', 'username', 'first_name', 'last_name', 'status', 'mat_no', 'course_code']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('email', 'first_name', 'last_name', 'status', 'mat_no', 'course_code')}),
    )

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('status',)}),
        )

admin.site.register(CustomUser, CustomUserAdmin)