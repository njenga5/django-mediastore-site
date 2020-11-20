from django.test import TestCase, LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from commonops.models import User


class CommonopsTests(TestCase, LiveServerTestCase):

    # @classmethod
    # def setUpTestData(cls):
    #     cls.user = User.objects.create(first_name='testuser',
    #                                     middle_name='testuser', 
    #                                     last_name='testuser',
    #                                     phone_number='0712345678',
    #                                     email='testuser@test.com',
    #                                     date_of_birth='1990-01-01',
    #                                     password='password'
    #                                     )
    # @classmethod
    # def setUpClass(cls):
    #     super().setUpClass()
    #     cls.driver = WebDriver()
    #     cls.driver.implicitly_wait(10)
    
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
    #     super().tearDownClass()

    def test_login_required(self):
        response = self.client.get('/dashboard/')
        self.assertRedirects(response, '/commonops/auth/')

    
