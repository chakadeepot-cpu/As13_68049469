from django.urls import path
from . import views  # ใช้ . แทน myapp เพื่อความกระชับและลด error

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),  # เติม / ปิดท้าย
    
    # เส้นทางสำหรับระบบ ลบ และ แก้ไข (เติม / ทุกอัน)
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('update/<int:id>/', views.update, name='update'),
]