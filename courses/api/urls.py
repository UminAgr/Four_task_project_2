from django.urls import path
from .views import CoursesAPIList, CoursesAPIView


urlpatterns = [
    path('api/v1/courses/', CoursesAPIList.as_view()),
    path('api/v1/courses/<int:pk>/', CoursesAPIView.as_view()),

]