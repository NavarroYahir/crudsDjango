from django.contrib import admin
from django.urls import path,include
from ninja import NinjaAPI
from crud_ninja.api.api import router as crud_router

api = NinjaAPI()
api.add_router("/api/", crud_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('crud_FBV.urls')),
    path('', include('crud_CBV.urls')),
    path("api/", api.urls), 

]
