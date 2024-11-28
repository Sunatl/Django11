from django.urls import path
from .views import *

urlpatterns = [
    
    path("Home",base,name="base"),
    path("",login,name="logn"),
    path('logout/',user_logout, name='logout'),
    # Group URLs
    path("groups/", GroupListView.as_view(), name="group_list"),
    path("groups/<int:pk>/", GroupDetailView.as_view(), name="group_detail"),
    path("groups/create/", GroupCreateView.as_view(), name="group_create"),
    path("groups/<int:pk>/update/", GroupUpdateView.as_view(), name="group_update"),
    path("groups/<int:pk>/delete/", GroupDeleteView.as_view(), name="group_delete"),

    # Students URLs
    path("students/", StudentListView.as_view(), name="student_list"),
    path("students/<int:pk>/", StudentDetailView.as_view(), name="student_detail"),
    path("students/create/", StudentCreateView.as_view(), name="student_create"),
    path("students/<int:pk>/update/", StudentUpdateView.as_view(), name="student_update"),
    path("students/<int:pk>/delete/", StudentDeleteView.as_view(), name="student_delete"),

    # Teacher URLs
    path("teachers/", TeacherListView.as_view(), name="teacher_list"),
    path("teachers/<int:pk>/", TeacherDetailView.as_view(), name="teacher_detail"),
    path("teachers/create/", TeacherCreateView.as_view(), name="teacher_create"),
    path("teachers/<int:pk>/update/", TeacherUpdateView.as_view(), name="teacher_update"),
    path("teachers/<int:pk>/delete/", TeacherDeleteView.as_view(), name="teacher_delete"),

    # Attendance URLs
    path("attendances/", AttendanceListView.as_view(), name="attendance_list"),
    path("attendances/<int:pk>/", AttendanceDetailView.as_view(), name="attendance_detail"),
    path("attendances/create/", AttendanceCreateView.as_view(), name="attendance_create"),
    path("attendances/<int:pk>/update/", AttendanceUpdateView.as_view(), name="attendance_update"),
    path("attendances/<int:pk>/delete/", AttendanceDeleteView.as_view(), name="attendance_delete"),
]
