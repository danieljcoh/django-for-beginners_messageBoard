from django.test import TestCase
from django.urls import reverse

from .models import Post
# Create your tests here.

# TODO
# URL exists at / and returns a 200 HTTP status code
# URL is available by its name of "home"
# Correct template is used called "post_list.html"
# Homepage content matches what we expect in the database


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(content="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.content, "This is a test!")

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("post-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "post_list.html")
        self.assertContains(response, "This is a test!")
