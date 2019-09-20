# import urllib.request,json
from .models import Category 
def get_category(id):
        category_object = None
        if category_details_response:
          id = category_details_response.get('id')
          cat_name = category_details_response.get('category_name')
          category_object = Category(id,cat_name)
          return category_object