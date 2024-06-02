from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTests(TestCase):
    """
    "What": การทดสอบหน้าแอดมิน Django สำหรับการจัดการผู้ใช้.
    "Why": เพื่อตรวจสอบว่าหน้าจัดการแอดมินทำงานตามที่คาดหวังสำหรับการดำเนินการต่างๆ ของผู้ใช้ เช่น การแสดงรายการ, การแก้ไข, และการสร้างผู้ใช้.
    "How": โดยใช้ไคลเอนต์ทดสอบของ Django เพื่อจำลองการโต้ตอบกับอินเตอร์เฟซแอดมิน.
    "Where": การทดสอบนี้นำไปใช้กับอินเตอร์เฟซแอดมินที่ตั้งค่าไว้สำหรับโมเดลผู้ใช้.
    "When": รันการทดสอบเหล่านี้เป็นส่วนหนึ่งของกระบวนการ integration ต่อเนื่องหรือหลังจากมีการเปลี่ยนแปลงการตั้งค่าแอดมิน.
    """
    def setUp(self):
        """
        "What": ตั้งค่าวัตถุที่จำเป็นสำหรับการทดสอบ.
        "Why": เตรียมสภาพแวดล้อมทดสอบด้วยผู้ใช้แอดมินและผู้ใช้ปกติเพื่อจำลองการโต้ตอบแอดมิน.
        "How": สร้างตัวอย่างผู้ใช้ superuser และผู้ใช้ปกติและใช้ไคลเอนต์ Django เพื่อจำลองการเข้าสู่ระบบแอดมิน.
        "Where": การตั้งค่านี้ดำเนินการก่อนทุกเมธอดทดสอบเพื่อให้มั่นใจว่าสภาพแวดล้อมทดสอบมีความสอดคล้อง.
        "When": เรียกใช้อัตโนมัติก่อนแต่ละเมธอดทดสอบ.
        """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password='testpass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password='testpass123',
            name="Test User"
        )

    def test_users_list(self):
        """
        "What": ทดสอบว่าผู้ใช้ถูกระบุในหน้าแอดมิน.
        "Why": ตรวจสอบว่าหน้ารายการผู้ใช้แสดงรายละเอียดของผู้ใช้ได้อย่างถูกต้อง.
        "How": เข้าถึงหน้ารายการผู้ใช้และยืนยันการมีข้อมูลของผู้ใช้.
        "Where": ดำเนินการตรวจสอบกับ URL ของหน้ารายการผู้ใช้แอดมิน.
        "When": ควรรันเพื่อตรวจสอบความสมบูรณ์ของหน้ารายการผู้ใช้แอดมินหลังจากมีการเปลี่ยนแปลง.
        """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """
        "What": ทดสอบว่าหน้าแก้ไขผู้ใช้ในแอดมินทำงานได้อย่างถูกต้อง.
        "Why": ตรวจสอบว่าหน้าแก้ไขรายละเอียดผู้ใช้สามารถเข้าถึงและทำงานได้.
        "How": เข้าถึง URL หน้าแก้ไขผู้ใช้และตรวจสอบรหัสสถานะ HTTP.
        "Where": ดำเนินการตรวจสอบกับ URL ของหน้าแก้ไขผู้ใช้แอดมิน.
        "When: ควรรันเพื่อยืนยันการจัดการการแก้ไขผู้ใช้แอดมิน.
        """
        url = reverse("admin:core_user_change", args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """
        "What": ทดสอบว่าหน้าเพิ่มผู้ใช้ใหม่ในแอดมินสามารถเข้าถึงได้.
        "Why": เพื่อยืนยันว่าอินเตอร์เฟซแอดมินอนุญาตให้เพิ่มผู้ใช้ใหม่ได้อย่างถูกต้อง.
        "How": เข้าถึงหน้าเพิ่มผู้ใช้และตรวจสอบสถานะการตอบสนอง.
        "Where": การทดสอบนี้ดำเนินการตรวจสอบกับ URL ของหน้าเพิ่มผู้ใช้แอดมิน.
        "When": มีประโยชน์สำหรับการทดสอบการเปลี่ยนแปลงกระบวนการหรือแบบฟอร์มการสร้างผู้ใช้.
        """
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
