from django import forms
from .models import Staff
import re

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'email', 'staff_id', 'department']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('.edu'):
            raise forms.ValidationError("Email must be a university (.edu) address.")
        return email

    def clean_staff_id(self):
        staff_id = self.cleaned_data.get('staff_id')
        if not re.match(r'^STF\d{3}$', staff_id):
            raise forms.ValidationError("Staff ID must be in the format STF followed by 3 digits (e.g., STF001).")
        return staff_id
