from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,  # "What": คลาสฐานสำหรับการสร้างโมเดลผู้ใช้ที่กำหนดเอง แทนโมเดลผู้ใช้มาตรฐานของ Django. "Why": ให้ความยืดหยุ่นในการกำหนดคุณสมบัติและการจัดการสิทธิ์ของผู้ใช้.
    BaseUserManager,   # "What": ช่วยในการสร้างผู้ใช้หรือผู้ใช้ที่มีสิทธิพิเศษจากบรรทัดคำสั่งหรือผ่าน Django admin. "Why": ให้วิธีการที่มาตรฐานและตรวจสอบได้ในการจัดการผู้ใช้.
    PermissionsMixin   # "What": เพิ่มความสามารถในการจัดการสิทธิ์และกลุ่มให้กับโมเดลผู้ใช้. "Why": ให้โมเดลผู้ใช้สามารถเข้าถึงและจัดการสิทธิ์ตามกฎของ Django.
)
from django.conf import settings



class UserManager(BaseUserManager):
    """
    "What": จัดการสร้างผู้ใช้และผู้ดูแลระบบในระบบ Django.
    "Why": ให้การสร้างผู้ใช้และผู้ดูแลมีความยืดหยุ่นและตรงตามข้อกำหนดของแอปพลิเคชัน.
    "How": ผ่านการเรียกใช้เมธอด `create_user` และ `create_superuser` ที่มีการตั้งค่าพารามิเตอร์สำคัญ.
    "Where": ใช้ในระบบที่ต้องการการยืนยันตัวตนของผู้ใช้.
    "When": ทุกครั้งที่ต้องการเพิ่มผู้ใช้ใหม่หรือผู้ดูแลระบบ.
    """
    
    def create_user(self, email, password=None, **extra_fields):
        """
        "What": สร้างและบันทึกผู้ใช้ปกติด้วยอีเมลและรหัสผ่านที่ระบุ.
        "Why": อีเมลเป็นตัวระบุที่ไม่ซ้ำและเป็นมาตรฐานในการเข้าถึงระบบ.
        "How": ตรวจสอบอีเมล, ตั้งรหัสผ่าน, และบันทึกข้อมูลในฐานข้อมูล.
        "Where": ใช้ในฟังก์ชันการลงทะเบียนผู้ใช้.
        "When": เมื่อผู้ใช้ใหม่สมัครเข้ามาในระบบ.
        """
        if not email:
            raise ValueError('ผู้ใช้ต้องมีที่อยู่อีเมล')  # ตรวจสอบว่าอีเมลถูกให้มาหรือไม่
        user = self.model(email=self.normalize_email(email), **extra_fields)  # สร้างผู้ใช้ใหม่ด้วยข้อมูลที่ได้รับ
        user.set_password(password)  # ตั้งค่ารหัสผ่านที่ผ่านการเข้ารหัสแล้ว
        user.save(using=self._db)  # บันทึกผู้ใช้ลงในฐานข้อมูลที่เลือก
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        "What": สร้างและบันทึกผู้ดูแลระบบพร้อมสิทธิพิเศษ.
        "Why": ผู้ดูแลระบบจำเป็นต้องมีสิทธิ์เข้าถึงการจัดการและควบคุมระบบทั้งหมด.
        "How": ตั้งค่า 'is_staff' และ 'is_superuser' เป็นจริง, ตรวจสอบความถูกต้อง, และบันทึก.
        "Where": ใช้ในระบบการจัดการผู้ดูแลระบบ.
        "When": เมื่อต้องการสร้างบัญชีผู้ดูแลระบบ.
        """
        extra_fields.setdefault('is_staff', True)  # กำหนดให้ผู้ใช้นี้เป็นเจ้าหน้าที่
        extra_fields.setdefault('is_superuser', True)  # กำหนดให้ผู้ใช้นี้มีสิทธิ์สูงสุด

        if extra_fields.get('is_staff') is not True or extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser ต้องมี is_staff=True และ is_superuser=True.')  # ตรวจสอบค่าที่สำคัญเหล่านี้

        return self.create_user(email, password, **extra_fields)  # ใช้งานเมธอด create_user เพื่อสร้าง superuser

class User(AbstractBaseUser, PermissionsMixin):
    """
    "What": โมเดลผู้ใช้ในระบบที่ใช้อีเมลเป็นตัวระบุผู้ใช้หลักแทนชื่อผู้ใช้แบบเดิม.
    "Why": การใช้อีเมลเป็นตัวระบุช่วยให้ระบุตัวตนได้อย่างชัดเจนและเป็นสากล.
    "How": ใช้อีเมลในการเข้าสู่ระบบ, จัดการการตรวจสอบความถูกต้องของผู้ใช้.
    "Where": ใช้ในทุกส่วนของระบบที่ต้องการการยืนยันตัวตนผู้ใช้.
    "When": ทุกครั้งที่ผู้ใช้ทำการล็อกอินหรือต้องการยืนยันตัวตน.
    """
    email = models.EmailField(max_length=255, unique=True)  # ฟิลด์อีเมล, ใช้เป็นตัวระบุผู้ใช้หลัก
    name = models.CharField(max_length=255)  # ฟิลด์สำหรับชื่อของผู้ใช้
    is_active = models.BooleanField(default=True)  # บ่งบอกว่าผู้ใช้นี้ยังใช้งานอยู่หรือไม่
    is_staff = models.BooleanField(default=False)  # บ่งบอกว่าผู้ใช้นี้เป็นเจ้าหน้าที่หรือไม่

    objects = UserManager()  # ผูก UserManager กับโมเดล User

    USERNAME_FIELD = 'email'  # ใช้อีเมลเป็นชื่อผู้ใช้หลักในการเข้าสู่ระบบ

class Recipe(models.Model):
    """ Recipe Model object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=255
    )
    description = models.TextField(blank=True)
    time_miuntes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title