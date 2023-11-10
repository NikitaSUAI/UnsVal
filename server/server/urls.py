from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', views.user, name='user'),
    path('api/login/', views.issue_token, name='issue_token'),
    path('answer/', views.create_user, name='get_answer')
]
