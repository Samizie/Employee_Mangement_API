from django.urls import path, include
from .views import home, DepartmentListCreateView,EmployeeListCreateView, EmployeeDetailView, PerformanceReviewListCreateView




urlpatterns = [
    path("", home, name='home' ),
    path('api/v1/departments/', DepartmentListCreateView.as_view(), name='dept-list'),
    path('api/v1/employees/', EmployeeListCreateView.as_view(), name='employee-create'),
    path('api/v1/employee/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('api/v1/reviews/', PerformanceReviewListCreateView.as_view(), name='review-create'),
]