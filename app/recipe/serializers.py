"""
Serializer for Recipe APIs
"""
from rest_framework import serializers  # "What": นำเข้าโมดูล serializers จาก Django REST framework. "Why": ใช้ในการสร้างและจัดการข้อมูลที่ผ่าน API. "How": ใช้คลาส serializers ในการสร้าง Serializer class. "Where": ใช้ในทุกฟังก์ชันการจัดการข้อมูลผ่าน API. "When": เมื่อมีการรับหรือส่งข้อมูลผ่าน API.
from core.models import Recipe  # "What": นำเข้าโมเดล Recipe จากแอปพลิเคชัน core. "Why": ใช้ในการเชื่อมโยงกับ Serializer. "How": ใช้โมเดล Recipe ในการกำหนดข้อมูลที่จะจัดการ. "Where": ใช้ใน Serializer class. "When": เมื่อมีการจัดการข้อมูลของ Recipe.

class RecipeSerializer(serializers.ModelSerializer):
    """
    "What": Serializer สำหรับโมเดล Recipe.
    "Why": ใช้ในการแปลงข้อมูลของ Recipe ให้เป็นรูปแบบที่สามารถส่งผ่าน API ได้.
    "How": กำหนดฟิลด์และการตั้งค่าของโมเดล Recipe ในคลาส Meta.
    "Where": ใช้ในฟังก์ชันการรับส่งข้อมูลผ่าน API.
    "When": เมื่อมีการเรียกใช้ API เพื่อจัดการข้อมูล Recipe.
    """
    class Meta:
        model = Recipe  # "What": กำหนดโมเดลที่ใช้ใน Serializer. "Why": เพื่อเชื่อมโยงกับโมเดล Recipe. "How": ใช้ model = Recipe ในคลาส Meta. "Where": ใช้ใน Serializer class. "When": เมื่อกำหนดฟิลด์และการตั้งค่าของ Serializer.
        fields = ['id', 'title', 'time_miuntes', 'price', 'link', 'description']  # "What": กำหนดฟิลด์ที่จะใช้ใน Serializer. "Why": เพื่อระบุฟิลด์ที่ต้องการส่งผ่าน API. "How": ใช้ fields ในคลาส Meta. "Where": ใช้ใน Serializer class. "When": เมื่อกำหนดฟิลด์ของ Serializer.
        read_only_fields = ['id']  # "What": กำหนดฟิลด์ที่อ่านได้อย่างเดียว. "Why": เพื่อป้องกันการแก้ไขฟิลด์ id. "How": ใช้ read_only_fields ในคลาส Meta. "Where": ใช้ใน Serializer class. "When": เมื่อกำหนดฟิลด์ของ Serializer.

class RecipeDeailSerializer(RecipeSerializer):
    """
    "What": Serializer สำหรับการแสดงรายละเอียดของ Recipe.
    "Why": ใช้ในการแสดงข้อมูลเพิ่มเติมในรายละเอียดของ Recipe.
    "How": ใช้คลาส Meta ของ RecipeSerializer และเพิ่มฟิลด์ description.
    "Where": ใช้ในฟังก์ชันการแสดงรายละเอียดของ Recipe.
    "When": เมื่อมีการเรียกใช้ API เพื่อแสดงรายละเอียดของ Recipe.
    """
    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']  # "What": เพิ่มฟิลด์ description ใน Serializer. "Why": เพื่อแสดงรายละเอียดเพิ่มเติมใน API. "How": ใช้ fields ในคลาส Meta. "Where": ใช้ใน Serializer class. "When": เมื่อกำหนดฟิลด์ของ Serializer.
