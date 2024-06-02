from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext_lazy as _

class UserAdmin(BaseUserAdmin):
    """
    Define the admin pages for users.
    กำหนดการตั้งค่าหน้าผู้ใช้ในแดชบอร์ด admin ของ Django.
    
    "What": คลาสนี้กำหนดการจัดการและการแสดงผลผู้ใช้ในหน้า admin.
    "Where": ใช้ภายใน Django admin backend.
    "When": โหลดทุกครั้งที่เข้าถึงหน้า admin ของผู้ใช้.
    "Why": เพื่อให้ผู้ดูแลระบบสามารถจัดการข้อมูลผู้ใช้ได้ง่ายดายและมีประสิทธิภาพ.
    "How": ผ่านการกำหนดค่าต่างๆ เช่น list_display, fieldsets และ add_fieldsets ซึ่งช่วยในการจัดโครงสร้างและการเข้าถึงข้อมูลของผู้ใช้.
    """
    ordering = ['id']  # "Why": จัดเรียงข้อมูลผู้ใช้ตาม ID เพื่อง่ายต่อการค้นหา.
    list_display = ['email', 'name']  # "Why": แสดง email และ name ในหน้ารายการผู้ใช้เพื่อความชัดเจนในการตรวจสอบ.

    # "What": กำหนด fieldsets สำหรับการแสดงและการแก้ไขผู้ใช้.
    fieldsets = (
        (None, {'fields': ('email', 'password')}),  # ข้อมูลพื้นฐาน
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),  # การจัดการสิทธิ์
        (_('Important dates'), {'fields': ('last_login',)})  # วันที่สำคัญ เช่น วันที่เข้าใช้งานล่าสุด
    )
    readonly_fields = ['last_login']  # "Why": ตั้งค่านี้เป็น readonly เพื่อป้องกันการแก้ไขโดยไม่ตั้งใจ.

    # "What": กำหนดการตั้งค่าสำหรับหน้าเพิ่มผู้ใช้ใหม่.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),  # การตั้งค่า layout เพื่อการแสดงผลที่ชัดเจน
            'fields': ('email', 'password1', 'password2', 'name', 'is_active', 'is_staff', 'is_superuser')
        }),
    )

admin.site.register(models.User, UserAdmin)  # ลงทะเบียน User model และ UserAdmin ใน Django admin.
admin.site.register(models.Recipe)