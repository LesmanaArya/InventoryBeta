from django.urls import path
from . import views

app_name = 'main'
# URL Config
urlpatterns = [
    path('', views.home, name='home'),  # Jika url main nya berupa string kosong, jalankan fungsi home yang ada di views.py
    path('create-product/', views.create_product, name='create_product'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<int:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', views.show_json_by_id, name='show_json_by_id'),
]
