from django.urls import path
from . import views

app_name ="food"

urlpatterns = [
    path("",views.Index, name="views"),
    # path("items/", views.list, name="list"),
    path("<int:item_id>",views.detail, name="detail"),
    #add items
    path("add/",views.create_item, name="create_item"),
    path("update/<int:id>/",views.update_item, name="update_item"),
    path ("delete/<int:id>",views.delete_item, name="delete_item"),
    

]
