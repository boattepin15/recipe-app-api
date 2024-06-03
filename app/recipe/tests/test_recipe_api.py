from rest_framework.test import APIClient  # "What": นำเข้าโมดูล APIClient จาก Django REST framework. "Why": ใช้ในการทดสอบ API. "How": ใช้คลาส APIClient ในการสร้าง client สำหรับทดสอบ API. "Where": ใช้ในทุกฟังก์ชันการทดสอบ API. "When": เมื่อมีการทดสอบ API.
from django.test import TestCase  # "What": นำเข้าโมดูล TestCase จาก Django. "Why": ใช้ในการสร้างชุดทดสอบสำหรับ Django. "How": ใช้คลาส TestCase ในการสร้างชุดทดสอบ. "Where": ใช้ในทุกฟังก์ชันการทดสอบ. "When": เมื่อมีการทดสอบฟังก์ชันต่างๆ ใน Django.
from rest_framework import status  # "What": นำเข้าโมดูล status จาก Django REST framework. "Why": ใช้ในการตรวจสอบสถานะของการตอบสนอง API. "How": ใช้สถานะต่างๆ ในการเปรียบเทียบกับผลลัพธ์ที่ได้จาก API. "Where": ใช้ในฟังก์ชันการทดสอบ API. "When": เมื่อมีการตรวจสอบสถานะของการตอบสนอง API.
from django.urls import reverse  # "What": นำเข้าโมดูล reverse จาก Django. "Why": ใช้ในการสร้าง URL แบบย้อนกลับ. "How": ใช้ฟังก์ชัน reverse ในการสร้าง URL จากชื่อเส้นทาง. "Where": ใช้ในฟังก์ชันการทดสอบ. "When": เมื่อมีการทดสอบ URL ใน Django.
from django.contrib.auth import get_user_model  # "What": นำเข้าโมดูล get_user_model จาก Django. "Why": ใช้ในการรับโมเดลผู้ใช้ที่กำหนดเอง. "How": ใช้ฟังก์ชัน get_user_model ในการรับโมเดลผู้ใช้. "Where": ใช้ในฟังก์ชันการทดสอบ. "When": เมื่อมีการทดสอบผู้ใช้ใน Django.
from decimal import Decimal  # "What": นำเข้าโมดูล Decimal จาก Python. "Why": ใช้ในการจัดการตัวเลขทศนิยม. "How": ใช้คลาส Decimal ในการสร้างตัวเลขทศนิยม. "Where": ใช้ในฟังก์ชันการทดสอบ. "When": เมื่อมีการทดสอบฟังก์ชันที่เกี่ยวข้องกับตัวเลขทศนิยม.
from core.models import Recipe  # "What": นำเข้าโมเดล Recipe จากแอปพลิเคชัน core. "Why": ใช้ในการเชื่อมโยงกับการทดสอบ. "How": ใช้โมเดล Recipe ในการกำหนดข้อมูลที่จะทดสอบ. "Where": ใช้ในฟังก์ชันการทดสอบ. "When": เมื่อมีการทดสอบข้อมูลของ Recipe.
from recipe.serializers import RecipeSerializer, RecipeDeailSerializer  # "What": นำเข้า Serializer จากแอปพลิเคชัน recipe. "Why": ใช้ในการแปลงข้อมูลของ Recipe ให้เป็นรูปแบบที่สามารถทดสอบได้. "How": ใช้คลาส Serializer ในการสร้าง Serializer class. "Where": ใช้ในฟังก์ชันการทดสอบ. "When": เมื่อมีการทดสอบการรับหรือส่งข้อมูลผ่าน API.

RECIPE_URL = reverse('recipe:recipe-list')  # "What": กำหนด URL สำหรับการเรียกใช้งาน API ของ Recipe. "Why": ใช้ในการทดสอบการเรียกใช้งาน API. "How": ใช้ฟังก์ชัน reverse ในการสร้าง URL. "Where": ใช้ในฟังก์ชันการทดสอบ. "When": เมื่อมีการทดสอบการเรียกใช้งาน API.

def detail_url(recipe_id):
    """Create and return a recipe detail URL.
    "What": สร้างและคืนค่า URL สำหรับรายละเอียดของ Recipe.
    "Why": ใช้ในการทดสอบการเรียกใช้งาน API สำหรับรายละเอียดของ Recipe.
    "How": ใช้ฟังก์ชัน reverse ในการสร้าง URL โดยใช้ id ของ Recipe.
    "Where": ใช้ในฟังก์ชันการทดสอบ.
    "When": เมื่อมีการทดสอบการเรียกใช้งาน API สำหรับรายละเอียดของ Recipe.
    """
    return reverse('recipe:recipe-detail', args=[recipe_id])

def create_recipe(user, **params):
    """Create and return a sample recipe.
    "What": สร้างและคืนค่าตัวอย่าง Recipe.
    "Why": ใช้ในการทดสอบการสร้าง Recipe.
    "How": ใช้โมเดล Recipe ในการสร้าง Recipe ใหม่.
    "Where": ใช้ในฟังก์ชันการทดสอบ.
    "When": เมื่อมีการทดสอบการสร้าง Recipe.
    """
    defaults = {
        'title': "Simple recipe title",
        'time_miuntes': 22,
        'price': Decimal('5.25'),
        'description': 'Sample description',
        'link': 'http://example.com/recipe.pdf'
    }

    defaults.update(params)
    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe

def create_user(**params):
    """Create and return a new user.
    "What": สร้างและคืนค่าผู้ใช้ใหม่.
    "Why": ใช้ในการทดสอบการสร้างผู้ใช้.
    "How": ใช้ฟังก์ชัน get_user_model ในการสร้างผู้ใช้ใหม่.
    "Where": ใช้ในฟังก์ชันการทดสอบ.
    "When": เมื่อมีการทดสอบการสร้างผู้ใช้.
    """
    return get_user_model().objects.create_user(**params)


class PublicRecipeAPITests(TestCase):
    """Test unauthenticated API requests.
    "What": ทดสอบการเรียกใช้งาน API โดยไม่มีการยืนยันตัวตน.
    "Why": เพื่อให้แน่ใจว่าการเรียกใช้งาน API โดยไม่มีการยืนยันตัวตนจะถูกปฏิเสธ.
    "How": ใช้คลาส TestCase ในการสร้างชุดทดสอบ.
    "Where": ใช้ในฟังก์ชันการทดสอบ.
    "When": เมื่อมีการทดสอบการเรียกใช้งาน API โดยไม่มีการยืนยันตัวตน.
    """

    def setUp(self):
        """Set up the test client.
        "What": ตั้งค่าคลาสทดสอบ.
        "Why": เพื่อเตรียมความพร้อมสำหรับการทดสอบ.
        "How": ใช้ฟังก์ชัน setUp ในการกำหนดค่าคลาสทดสอบ.
        "Where": ใช้ในฟังก์ชันการทดสอบ.
        "When": ก่อนที่จะทำการทดสอบ.
        """
        self.client = APIClient()

    def test_auth_required(self):
        """Test that authentication is required to call API.
        "What": ทดสอบว่าต้องมีการยืนยันตัวตนในการเรียกใช้งาน API.
        "Why": เพื่อให้แน่ใจว่าการเรียกใช้งาน API โดยไม่มีการยืนยันตัวตนจะถูกปฏิเสธ.
        "How": ใช้ฟังก์ชัน get ในการเรียกใช้งาน API และตรวจสอบสถานะการตอบสนอง.
        "Where": ใช้ในฟังก์ชันการทดสอบ.
        "When": เมื่อมีการทดสอบการเรียกใช้งาน API โดยไม่มีการยืนยันตัวตน.
        """
        res = self.client.get(RECIPE_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeApiTests(TestCase):
    """ Test authenticated API requests.
    "What": ทดสอบการเรียกใช้งาน API โดยมีการยืนยันตัวตน.
    "Why": เพื่อให้แน่ใจว่าการเรียกใช้งาน API โดยมีการยืนยันตัวตนสามารถทำงานได้ถูกต้อง.
    "How": ใช้คลาส TestCase ในการสร้างชุดทดสอบ.
    "Where": ใช้ในฟังก์ชันการทดสอบ.
    "When": เมื่อมีการทดสอบการเรียกใช้งาน API โดยมีการยืนยันตัวตน.
    """
    def setUp(self):
        """Set up the test client and user.
        "What": ตั้งค่าคลาสทดสอบและผู้ใช้.
        "Why": เพื่อเตรียมความพร้อมสำหรับการทดสอบ.
        "How": ใช้ฟังก์ชัน setUp ในการกำหนดค่าคลาสทดสอบและสร้างผู้ใช้ใหม่.
        "Where": ใช้ในฟังก์ชันการทดสอบ.
        "When": ก่อนที่จะทำการทดสอบ.
        """
        self.client = APIClient()
        self.user = create_user(email='user@gmail.com', password='test1234')
        # self.user = get_user_model().objects.create_user(
        #     "user@gmail.com",
        #     "test1234"
        # )
        self.client.force_authenticate(self.user)

def test_retrieve_recipes(self):
    """Test retrieving a list of recipes.
    "What": ทดสอบการดึงข้อมูลรายการของ Recipe.
    "Why": เพื่อให้แน่ใจว่าการดึงข้อมูลรายการของ Recipe สามารถทำงานได้ถูกต้อง.
    "How": ใช้ฟังก์ชัน get ในการเรียกใช้งาน API และตรวจสอบสถานะการตอบสนอง.
    "Where": ใช้ในฟังก์ชันการทดสอบ.
    "When": เมื่อมีการทดสอบการดึงข้อมูลรายการของ Recipe.
    """
    create_recipe(user=self.user)
    create_recipe(user=self.user)

    res = self.client.get(RECIPE_URL)
    recipes = Recipe.objects.all().order_by('-id')
    serializer = RecipeSerializer(recipes, many=True)
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(res.data, serializer.data)

def test_recipe_list_limited_to_user(self):
    """Test list of recipes is limited to authenticated user.
    "What": ทดสอบว่ารายการ Recipe ถูกจำกัดสำหรับผู้ใช้ที่ยืนยันตัวตน.
    "Why": เพื่อให้แน่ใจว่าผู้ใช้ที่ไม่ได้รับอนุญาตจะไม่สามารถเข้าถึงรายการ Recipe ของผู้ใช้คนอื่นได้.
    "How": สร้าง Recipe สำหรับผู้ใช้หลายคนและตรวจสอบการตอบสนอง.
    "Where": ใช้ในฟังก์ชันการทดสอบ.
    "When": เมื่อมีการทดสอบการดึงข้อมูลรายการของ Recipe.
    """
    other_user = get_user_model().objects.create_user(
        "test@gmail.com",
        "password1234"
    )
    create_recipe(user=other_user)
    create_recipe(user=self.user)

    res = self.client.get(RECIPE_URL)
    recipes = Recipe.objects.filter(user=self.user)
    serializer = RecipeSerializer(recipes, many=True)
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(res.data, serializer.data)

def test_get_recipe_recipe_detail(self):
    """Test get recipe detail.
    "What": ทดสอบการดึงรายละเอียดของ Recipe.
    "Why": เพื่อให้แน่ใจว่ารายละเอียดของ Recipe สามารถดึงข้อมูลได้ถูกต้อง.
    "How": ใช้ฟังก์ชัน get ในการเรียกใช้งาน API และตรวจสอบสถานะการตอบสนอง.
    "Where": ใช้ในฟังก์ชันการทดสอบ.
    "When": เมื่อมีการทดสอบการดึงรายละเอียดของ Recipe.
    """
    recipe = create_recipe(user=self.user)
    url = detail_url(recipe.id)
    res = self.client.get(url)
    serializer = RecipeDeailSerializer(recipe)
    self.assertEqual(res.data, serializer.data)

def test_create_recipe(self):
    """Test creating a recipe.
    "What": ทดสอบการสร้าง Recipe.
    "Why": เพื่อให้แน่ใจว่าการสร้าง Recipe สามารถทำงานได้ถูกต้อง.
    "How": ใช้ฟังก์ชัน post ในการเรียกใช้งาน API และตรวจสอบสถานะการตอบสนอง.
    "Where": ใช้ในฟังก์ชันการทดสอบ.
    "When": เมื่อมีการทดสอบการสร้าง Recipe.
    """
    payload = {
        'title': "Simple recipe title",
        'time_miuntes': 22,
        'price': Decimal('5.25'),
        'description': 'Sample description',
        'link': 'http://example.com/recipe.pdf'
    }
    res = self.client.post(RECIPE_URL, payload)

    self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    recipe = Recipe.objects.get(id=res.data['id'])
    for key in payload.keys():
        self.assertEqual(payload[key], getattr(recipe, key))

def test_partial_update(self):
    """Test partial update of a recipe.
    "What": ทดสอบการอัปเดตบางส่วนของ Recipe.
    "Why": เพื่อให้แน่ใจว่าการอัปเดตบางส่วนของ Recipe สามารถทำงานได้ถูกต้อง.
    "How": ใช้ฟังก์ชัน patch ในการเรียกใช้งาน API และตรวจสอบสถานะการตอบสนอง.
    "Where": ใช้ในฟังก์ชันการทดสอบ.
    "When": เมื่อมีการทดสอบการอัปเดตบางส่วนของ Recipe.
    """
    original_link = "http://example.com/recipe.pdf"
    recipe = create_recipe(
        user=self.user,
        title='Sample recipe title',
        link=original_link
    )

    payload = {'title': 'New Recipe Title'}
    url = detail_url(recipe_id=recipe.id)
    res = self.client.patch(url, payload)

    recipe.refresh_from_db()
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(recipe.title, payload['title'])
    self.assertEqual(recipe.link, original_link)
    self.assertEqual(recipe.user, self.user)

def test_full_update(self):
    """Test full update of a recipe.
    "What": ทดสอบการอัปเดตทั้งหมดของ Recipe.
    "Why": เพื่อให้แน่ใจว่าการอัปเดตทั้งหมดของ Recipe สามารถทำงานได้ถูกต้อง.
    "How": ใช้ฟังก์ชัน put ในการเรียกใช้งาน API และตรวจสอบสถานะการตอบสนอง.
    "Where": ใช้ในฟังก์ชันการทดสอบ.
    "When": เมื่อมีการทดสอบการอัปเดตทั้งหมดของ Recipe.
    """
    recipe = create_recipe(
        user=self.user,
        title='Sample recipe title',
        link='http://example.com/recipe.pdf',
        description='Sample description'
    )

    payload = {
        'title': 'Updated recipe title',
        'time_miuntes': 25,
        'price': Decimal('10.00'),
        'description': 'Updated description',
        'link': 'http://example.com/updated_recipe.pdf'
    }

    url = detail_url(recipe.id)
    res = self.client.put(url, payload)

    recipe.refresh_from_db()
    self.assertEqual(res.status_code, status.HTTP_200_OK)
    self.assertEqual(recipe.title, payload['title'])
    self.assertEqual(recipe.time_miuntes, payload['time_miuntes'])
    self.assertEqual(recipe.price, payload['price'])
    self.assertEqual(recipe.description, payload['description'])
    self.assertEqual(recipe.link, payload['link'])
    self.assertEqual(recipe.user, self.user)

def test_update_user_return_error(self):
    """Test changing the recipe user results in an error.
    "What": ทดสอบการเปลี่ยนผู้ใช้ของ Recipe และให้ผลลัพธ์เป็นข้อผิดพลาด.
    "Why": เพื่อให้แน่ใจว่าการเปลี่ยนผู้ใช้ของ Recipe จะไม่สามารถทำได้.
    "How": ใช้ฟังก์ชัน patch ในการเรียกใช้งาน API และตรวจสอบสถานะการตอบสนอง.
    "Where": ใช้ในฟังก์ชันการทดสอบ.
    "When": เมื่อมีการทดสอบการเปลี่ยนผู้ใช้ของ Recipe.
    """
    new_user = create_user(email="user2@gmail.com", password="test1234")
    recipe = create_recipe(user=self.user)

    payload = {'user': new_user}
    url = detail_url(recipe_id=recipe.id)
    self.client.patch(url, payload)
    recipe.refresh_from_db()
    self.assertEqual(recipe.user, self.user)

def test_delete_recipe(self):
    """Test deleting a recipe.
    "What": ทดสอบการลบ Recipe.
    "Why": เพื่อให้แน่ใจว่าการลบ Recipe สามารถทำงานได้ถูกต้อง.
    "How": ใช้ฟังก์ชัน delete ในการเรียกใช้งาน API และตรวจสอบสถานะการตอบสนอง.
    "Where": ใช้ในฟังก์ชันการทดสอบ.
    "When": เมื่อมีการทดสอบการลบ Recipe.
    """
    recipe = create_recipe(user=self.user)

    url = detail_url(recipe.id)
    res = self.client.delete(url)

    self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
    self.assertFalse(Recipe.objects.filter(id=recipe.id).exists())

def test_delete_other_users_recipe_error(self):
    """Test that a user cannot delete or update another user's recipe.
    "What": ทดสอบว่าผู้ใช้ไม่สามารถลบหรืออัปเดต Recipe ของผู้ใช้อื่นได้.
    "Why": เพื่อให้แน่ใจว่าผู้ใช้ที่ไม่ได้รับอนุญาตจะไม่สามารถเข้าถึง Recipe ของผู้ใช้อื่นได้.
    "How": สร้าง Recipe สำหรับผู้ใช้คนอื่นและพยายามลบ Recipe นั้น.
    "Where": ใช้ในฟังก์ชันการทดสอบ.
    "When": เมื่อมีการทดสอบการลบหรืออัปเดต Recipe ของผู้ใช้อื่น.
    """
    new_user = create_user(
       email="user2@gmail.com",
       password='test1234' 
    )
    recipe = create_recipe(user=new_user)
    url = detail_url(recipe.id)
    res = self.client.delete(url)

    self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
    self.assertTrue(Recipe.objects.filter(id=recipe.id).exists())
