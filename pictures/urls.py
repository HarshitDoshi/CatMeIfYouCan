from django.urls import path
from pictures.views import CatPictureViewSet

cat_picture_list = CatPictureViewSet.as_view({"get": "list", "post": "create"})
cat_picture_detail = CatPictureViewSet.as_view(
    {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
)

urlpatterns = [
    path("", cat_picture_list, name="cat_picture-list"),
    path("<int:pk>/", cat_picture_detail, name="cat_picture-detail"),
]
