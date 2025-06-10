from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI
from apps.crud_ninja.api.api import router as user_router
import apps.crud_FBV.urls


api = NinjaAPI()
api.add_router("/api/", user_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.crud_FBV.urls')),
    path('', include('apps.crud_CBV.urls')),
    path("api/", api.urls),
]
