from django.contrib import admin
from django.urls import path
from .views import home_page, about_us

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', home_page),
	path('about-us', about_us)
]
