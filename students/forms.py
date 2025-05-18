from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'registration_number', 'enrolled_courses']

    # Example validation: email must be a university email (.edu)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and not email.endswith('.edu'):
            raise forms.ValidationError("Email must be a university (.edu) address.")
        return email

    # You can add other custom validators here, e.g. for registration_number
    def clean_registration_number(self):
        reg_num = self.cleaned_data.get('registration_number')
        if reg_num and not reg_num.isalnum():
            raise forms.ValidationError("Registration number should be alphanumeric only.")
        return reg_num
