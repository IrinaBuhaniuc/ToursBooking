from django.test import TestCase, Client
from django.urls import reverse
from apps.tours import models
from apps.user.models import User

# Test Case # Test<view-name>View
class TestResourcesView(TestCase):
    def setUp(self) -> None:
        self.client = Client()

        self.user = User.objects.create_user(
            username="igor",
            password="irina1234",
            first_name="Igor",
            last_name="Bang",
            email="igor.bang@gmail.com",
        )

        self.cat = models.Category.objects.create(cat="Restaurants")

        # create without the tag, so that the id is auto generated
        self.tour = models.Tour.objects.create(
            user_id=self.user,
            cat_id=self.cat,
            title="Osho",
            description="Best restaurant in Chisinau.",
            price = 10.99,
        )
        
        
    def test_home_page_return_200_status(self):
        response = self.client.get(
                    reverse('home-page'), # access usl using 
                    HTTP_USER_AGENT='Mozilla/5.0',
                    HTTP_CONTENT_TYPE = 'text/plain'
                    )
        
        self.assertEqual(response.status_code, 200)
        
    # def test_home_page_view_resource_count(self):
    #     # Arrange
    #     expected_resource_count = 1
        
    #     response = self.client.get(
    #                 reverse('home-page'), # access usl using 
    #                 HTTP_USER_AGENT='Mozilla/5.0',
    #                 HTTP_CONTENT_TYPE = 'text/plain'
    #                 )
    #     self.assertEqual(response.context['cnt'], expected_resource_count)