from django.urls import include, path
from main.views import create_shop_flutter, show_main
from main.views import show_main, create_shop_entry
from main.views import show_main, create_shop_entry, show_xml
from main.views import show_main, create_shop_entry, show_xml, show_json
from main.views import show_main, create_shop_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_shop, delete_shop, add_shop_entry_ajax, create_shop_flutter
app_name = 'main'
 
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-shop-entry', create_shop_entry, name='create_shop_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-shop/<uuid:id>', edit_shop, name='edit_shop'),
    path('delete/<uuid:id>', delete_shop, name='delete_shop'),
    path('create-shop-entry-ajax', add_shop_entry_ajax, name='add_shop_entry_ajax'),
    path('create-flutter/', create_shop_flutter, name='create_shop_flutter'),
    path('auth/', include('authentication.urls')),
]