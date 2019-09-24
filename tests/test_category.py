import unittest
from app.models import Category

class CategoryTest(unittest.TestCase):

  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_category = Category(1,'Health')

  # def test_instance(self):
  #   self.assertTrue(isinstance(self.new_category,Category))

