from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from pictures.models import CatPicture


class CatPictureTest(TestCase):
    def create_cat_picture(
        self,
        title="Test Title",
        description="Test Description",
        image="../media/test_cat_picture.jpg",
    ):
        return CatPicture.objects.create(
            title=title, description=description, image=image
        )

    def test_cat_picture_creation(self):
        cat_picture = self.create_cat_picture()
        self.assertTrue(isinstance(cat_picture, CatPicture))

    def test_cat_picture_title(self):
        cat_picture = self.create_cat_picture()
        self.assertEqual(cat_picture.__str__(), cat_picture.title)
        self.assertTrue(isinstance(cat_picture.title, str))
        self.assertGreaterEqual(len(cat_picture.title), 0)

    def test_cat_picture_description(self):
        cat_picture = self.create_cat_picture()
        self.assertTrue(isinstance(cat_picture.description, str))
        self.assertGreaterEqual(len(cat_picture.description), 0)

    def test_cat_picture_image(self):
        cat_picture = self.create_cat_picture()
        self.assertGreater(cat_picture.image.height, 0)
        self.assertGreater(cat_picture.image.width, 0)
        self.assertGreater(cat_picture.image.size, 0)


class CatPicturesAPITests(APITestCase):


    def setUp(self):
        self.username = "Test"
        self.email = "foo@bar.com"
        self.password = "test"

        self.title = "Test Title"
        self.description = "Test Description"
        self.image = "../media/test_cat_picture.jpg"

        self.view_name = "cat_picture-list"
        self.user = self.create_user()


    def create_user(self, username="Test", password="test"):
        return User.objects.create(username=self.username, email=self.email, password=self.password)


    def test_create_cat_picture(self):
        url = reverse(self.view_name)
        data = {
            "title": self.title,
            "description": self.description,
            "image": self.image,
        }
        self.client.login(username=self.username, password=self.password)
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CatPicture.objects.count(), 1)
        self.assertEqual(CatPicture.objects.get().title, self.title)


    def test_read_cat_pictures(self):
        url = reverse(self.view_name)
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CatPicture.objects.count(), 1)
        self.assertEqual(CatPicture.objects.get().title, self.title)
