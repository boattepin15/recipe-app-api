from rest_framework import viewsets  # "What": นำเข้าโมดูล viewsets จาก Django REST framework. "Why": ใช้ในการสร้าง ViewSet สำหรับจัดการ API. "How": ใช้คลาส viewsets.ModelViewSet ในการสร้าง ViewSet class. "Where": ใช้ในทุกฟังก์ชันการจัดการ API. "When": เมื่อมีการรับหรือส่งข้อมูลผ่าน API.
from rest_framework.authentication import TokenAuthentication  # "What": นำเข้าโมดูล TokenAuthentication จาก Django REST framework. "Why": ใช้ในการตรวจสอบสิทธิ์ด้วย Token. "How": ใช้ authentication_classes ในการกำหนดวิธีการตรวจสอบสิทธิ์. "Where": ใช้ใน ViewSet class. "When": เมื่อมีการเรียกใช้ API ที่ต้องการการตรวจสอบสิทธิ์.
from rest_framework.permissions import IsAuthenticated  # "What": นำเข้าโมดูล IsAuthenticated จาก Django REST framework. "Why": ใช้ในการตรวจสอบสิทธิ์ว่าผู้ใช้เข้าสู่ระบบแล้ว. "How": ใช้ permission_classes ในการกำหนดสิทธิ์. "Where": ใช้ใน ViewSet class. "When": เมื่อมีการเรียกใช้ API ที่ต้องการการตรวจสอบสิทธิ์.

from core.models import Recipe  # "What": นำเข้าโมเดล Recipe จากแอปพลิเคชัน core. "Why": ใช้ในการเชื่อมโยงกับ ViewSet. "How": ใช้โมเดล Recipe ในการกำหนดข้อมูลที่จะจัดการ. "Where": ใช้ใน ViewSet class. "When": เมื่อมีการจัดการข้อมูลของ Recipe.
from recipe import serializers  # "What": นำเข้า serializers จากแอปพลิเคชัน recipe. "Why": ใช้ในการแปลงข้อมูลของ Recipe ให้เป็นรูปแบบที่สามารถส่งผ่าน API ได้. "How": ใช้คลาส serializers ในการสร้าง Serializer class. "Where": ใช้ใน ViewSet class. "When": เมื่อมีการรับหรือส่งข้อมูลผ่าน API.

class RecipeViewSet(viewsets.ModelViewSet):
    """
    "What": View สำหรับจัดการ Recipe API.
    "Why": เพื่อให้สามารถจัดการข้อมูล Recipe ผ่าน API ได้.
    "How": ใช้คลาส ModelViewSet จาก Django REST framework ในการสร้าง ViewSet.
    "Where": ใช้ในแอปพลิเคชันที่ต้องการจัดการข้อมูล Recipe ผ่าน API.
    "When": เมื่อมีการเรียกใช้ API เพื่อจัดการข้อมูล Recipe.
    """
    serializer_class = serializers.RecipeDeailSerializer  # "What": กำหนด Serializer class สำหรับ ViewSet. "Why": เพื่อแปลงข้อมูล Recipe ให้เป็นรูปแบบที่สามารถส่งผ่าน API ได้. "How": ใช้ serializer_class ในการกำหนดคลาส Serializer. "Where": ใช้ใน ViewSet class. "When": เมื่อมีการรับหรือส่งข้อมูลผ่าน API.
    queryset = Recipe.objects.all()  # "What": กำหนด QuerySet สำหรับ ViewSet. "Why": เพื่อระบุข้อมูล Recipe ที่จะจัดการ. "How": ใช้ queryset ในการกำหนด QuerySet. "Where": ใช้ใน ViewSet class. "When": เมื่อมีการเรียกใช้ API เพื่อจัดการข้อมูล Recipe.
    authentication_classes = [TokenAuthentication]  # "What": กำหนดวิธีการตรวจสอบสิทธิ์. "Why": เพื่อให้ผู้ใช้ที่เรียกใช้ API ต้องผ่านการตรวจสอบสิทธิ์ด้วย Token. "How": ใช้ authentication_classes ในการกำหนดวิธีการตรวจสอบสิทธิ์. "Where": ใช้ใน ViewSet class. "When": เมื่อมีการเรียกใช้ API ที่ต้องการการตรวจสอบสิทธิ์.
    permission_classes = [IsAuthenticated]  # "What": กำหนดสิทธิ์ในการเข้าถึง API. "Why": เพื่อให้เฉพาะผู้ใช้ที่เข้าสู่ระบบแล้วเท่านั้นที่สามารถเรียกใช้ API ได้. "How": ใช้ permission_classes ในการกำหนดสิทธิ์. "Where": ใช้ใน ViewSet class. "When": เมื่อมีการเรียกใช้ API ที่ต้องการการตรวจสอบสิทธิ์.

    def get_queryset(self):
        """
        "What": ดึงข้อมูล Recipe สำหรับผู้ใช้ที่เข้าสู่ระบบแล้ว.
        "Why": เพื่อให้แน่ใจว่าผู้ใช้สามารถดึงข้อมูล Recipe ของตนเองเท่านั้น.
        "How": ตรวจสอบว่าผู้ใช้เป็น Anonymous หรือไม่ และกรองข้อมูล Recipe ตามผู้ใช้.
        "Where": ใช้ใน ViewSet class.
        "When": เมื่อมีการเรียกใช้ API เพื่อดึงข้อมูล Recipe.
        """
        if self.request.user.is_anonymous:
            return Recipe.objects.none()  # "What": คืนค่า QuerySet ว่างถ้าผู้ใช้เป็น Anonymous. "Why": เพื่อป้องกันการเข้าถึงข้อมูล Recipe โดยผู้ใช้ที่ไม่เข้าสู่ระบบ. "How": ใช้ Recipe.objects.none() เพื่อคืนค่า QuerySet ว่าง. "Where": ใช้ใน get_queryset method. "When": เมื่อมีการเรียกใช้ API โดยผู้ใช้ที่ไม่เข้าสู่ระบบ.
        return self.queryset.filter(user=self.request.user).order_by('-id')  # "What": กรองข้อมูล Recipe ตามผู้ใช้. "Why": เพื่อให้แน่ใจว่าผู้ใช้สามารถดึงข้อมูล Recipe ของตนเองเท่านั้น. "How": ใช้ self.queryset.filter(user=self.request.user).order_by('-id). "Where": ใช้ใน get_queryset method. "When": เมื่อมีการเรียกใช้ API เพื่อดึงข้อมูล Recipe.

    def get_serializer_class(self):
        """
        "What": คืนค่า Serializer class สำหรับการร้องขอ.
        "Why": เพื่อใช้ Serializer ที่แตกต่างกันตามการกระทำที่ร้องขอ (เช่น list หรือ detail).
        "How": ตรวจสอบการกระทำที่ร้องขอและคืนค่า Serializer class ที่เหมาะสม.
        "Where": ใช้ใน ViewSet class.
        "When": เมื่อมีการเรียกใช้ API ที่ต้องการการแปลงข้อมูล Recipe.
        """
        if self.action == "list":
            return serializers.RecipeDeailSerializer  # "What": คืนค่า Serializer class สำหรับการแสดงรายการ Recipe. "Why": เพื่อแสดงข้อมูล Recipe ในรูปแบบที่เหมาะสม. "How": ใช้ self.action ในการตรวจสอบการกระทำที่ร้องขอ. "Where": ใช้ใน get_serializer_class method. "When": เมื่อมีการเรียกใช้ API เพื่อแสดงรายการ Recipe.
        
        return self.serializer_class  # "What": คืนค่า Serializer class เริ่มต้น. "Why": เพื่อแปลงข้อมูล Recipe ให้เป็นรูปแบบที่สามารถส่งผ่าน API ได้. "How": ใช้ self.serializer_class. "Where": ใช้ใน get_serializer_class method. "When": เมื่อมีการเรียกใช้ API เพื่อแปลงข้อมูล Recipe.

    def perform_create(self, serializer):
        """
        "What": สร้าง Recipe ใหม่.
        "Why": เพื่อบันทึกข้อมูล Recipe ใหม่ลงในฐานข้อมูล.
        "How": ใช้ serializer ในการบันทึกข้อมูล Recipe ใหม่.
        "Where": ใช้ใน ViewSet class.
        "When": เมื่อมีการเรียกใช้ API เพื่อสร้าง Recipe ใหม่.
        """
        serializer.save(user=self.request.user)  # "What": บันทึกข้อมูล Recipe ใหม่พร้อมกับผู้ใช้. "Why": เพื่อระบุเจ้าของของ Recipe. "How": ใช้ serializer.save(user=self.request.user). "Where": ใช้ใน perform_create method. "When": เมื่อมีการสร้าง Recipe ใหม่.
