from django.contrib import admin
from django.urls import path
from gs1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuinfo/<int:pk>/',views.student_detail),
    path('stulist/',views.student_list),
    path('stucreate/', views.student_create),
    path('studentapi/',views.student_api),
]
