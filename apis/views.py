from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Group, Students, Teacher, Attendance
from .forms import GroupForm, StudentForm, TeacherForm, AttendanceForm
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.db.models import Q
@login_required
def user_logout(request):
    logout(request) 
    return render(request, 'registration/log_out.html') 

def login(request):
    return redirect("accounts/login/")

def base(request):
    template = loader.get_template("base.html")
    return HttpResponse(template.render())
# Views for Group
class GroupListView(ListView):
    model = Group
    template_name = "group_list.html"
    context_object_name = "groups"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')  
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | 
                Q(is_active__icontains=query)    
            )
        return queryset


class GroupDetailView(DetailView):
    model = Group
    template_name = "group_detail.html"
    context_object_name = "group"


class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = "group_form.html"
    success_url = reverse_lazy("group_list")


class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = "group_form.html"
    success_url = reverse_lazy("group_list")


class GroupDeleteView(DeleteView):
    model = Group
    template_name = "group_confirm_delete.html"
    success_url = reverse_lazy("group_list")


# Views for Students
class StudentListView(ListView):
    model = Students
    template_name = "student_list.html"
    context_object_name = "students"


class StudentDetailView(DetailView):
    model = Students
    template_name = "student_detail.html"
    context_object_name = "student"


class StudentCreateView(CreateView):
    model = Students
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student_list")


class StudentUpdateView(UpdateView):
    model = Students
    form_class = StudentForm
    template_name = "student_form.html"
    success_url = reverse_lazy("student_list")


class StudentDeleteView(DeleteView):
    model = Students
    template_name = "student_confirm_delete.html"
    success_url = reverse_lazy("student_list")


# Views for Teacher
class TeacherListView(ListView):
    model = Teacher
    template_name = "teacher_list.html"
    context_object_name = "teachers"


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = "teacher_detail.html"
    context_object_name = "teacher"


class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "teacher_form.html"
    success_url = reverse_lazy("teacher_list")


class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = "teacher_form.html"
    success_url = reverse_lazy("teacher_list")


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = "teacher_confirm_delete.html"
    success_url = reverse_lazy("teacher_list")


# Views for Attendance
class AttendanceListView(ListView):
    model = Attendance
    template_name = "attendance_list.html"
    context_object_name = "attendances"


class AttendanceDetailView(DetailView):
    model = Attendance
    template_name = "attendance_detail.html"
    context_object_name = "attendance"


class AttendanceCreateView(CreateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = "attendance_form.html"
    success_url = reverse_lazy("attendance_list")


class AttendanceUpdateView(UpdateView):
    model = Attendance
    form_class = AttendanceForm
    template_name = "attendance_form.html"
    success_url = reverse_lazy("attendance_list")


class AttendanceDeleteView(DeleteView):
    model = Attendance
    template_name = "attendance_confirm_delete.html"
    success_url = reverse_lazy("attendance_list")
