from django import forms
from .models import Group, Students, Teacher, Attendance


# Form for Group
class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'is_active']  # Excluded 'date' since it is non-editable
        widgets = {
            'is_active': forms.CheckboxInput(),  # Improved widget for BooleanField
        }


# Form for Students
class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['f_name', 'l_name', 'email', 'phone', 'username', 'group', 'is_active']  # Excluded 'date'
        widgets = {
            'group': forms.CheckboxSelectMultiple(),  # Widget for Many-to-Many relationship
            'is_active': forms.CheckboxInput(),       # Widget for BooleanField
        }


# Form for Teacher
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['f_name', 'l_name', 'email', 'phone', 'subject', 'group', 'user']  # All editable fields
        widgets = {
            'group': forms.CheckboxSelectMultiple(),  # Widget for Many-to-Many relationship
        }


# Form for Attendance
class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        # Excluded 'omadan' and 'raftan' if they're auto-set fields
        fields = ['der_mekunam', 'nameoyam', 'student']
        widgets = {
            'der_mekunam': forms.Textarea(attrs={'rows': 3}),  # Improved textarea
            'nameoyam': forms.Textarea(attrs={'rows': 3}),     # Improved textarea
        }
