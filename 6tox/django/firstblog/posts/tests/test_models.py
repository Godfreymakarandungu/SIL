import pytest
from django.core.management import call_command

def test_an_admin_view(admin_client):
    response = admin_client.get('/admin/')
    assert response.status_code == 200
def test_new_user(django_user_model):
    django_user_model.objects.create(username = "makara", password = "kiugokiega") 
     
