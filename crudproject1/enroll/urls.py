from django.urls import path
from .views import add_show, delete_data, update_data

urlpatterns = [
    path('', add_show, name="addandshow"),
    path('delete/<int:id>/', delete_data, name="deletedata"),
    path('<int:id>/', update_data, name="updatedata"),
]
