import pytest
import pip._vendor.requests as requests

product_endpoint = "http://localhost:8000/v1/products/"

class TestProduct:
  def test_product_list(self):
    response = requests.get(product_endpoint)
    assert response.json().get('all') is not None

  def test_product_details(self):
    response = requests.get(product_endpoint+'1')
    assert response.json().get('name') is not None