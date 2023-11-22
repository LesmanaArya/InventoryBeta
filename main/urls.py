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
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('increement_amount/<int:id>', views.increement_amount, name='increement_amount'),
    path('decreement_amount/<int:id>', views.decreement_amount, name='decreement_amount'),
    path('delete_item/<int:id>', views.delete_item, name='delete_item'),
    path('edit_product/<int:id>', views.edit_product, name='edit_product'),
    path('get-product/', views.get_product_json, name='get_product_json'),
    path('create-product-ajax/', views.add_product_ajax, name='add_product_ajax'),
    path('create-flutter/', views.create_product_flutter, name='create_product_flutter'),
]
