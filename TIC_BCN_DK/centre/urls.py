from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teachers/', views.teachers, name='teachers'),
    path('students/', views.students, name='students'),
    path('teachers/teacher/<int:pk>', views.teacher, name='teacher'),
    path('students/student/<int:pk>', views.student, name='student'),
    path('form', views.form, name='form'),
    path('update-user/<int:pk>', views.update_person, name='update_person'),
    path('delete-persona/<int:pk>', views.delete_person, name='delete_person')
]
