from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'description', 'credits']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Course name is required.")
        if len(name) < 3:
            raise forms.ValidationError("Course name must be at least 3 characters long.")
        return name

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if not code:
            raise forms.ValidationError("Course code is required.")
        if len(code) < 4:
            raise forms.ValidationError("Course code must be at least 4 characters long.")
        # Example: Check if course code format is valid (e.g., ABC123)
        import re
        if not re.match(r'^[A-Z]{3}\d{3}$', code):
            raise forms.ValidationError("Course code must be in format: AAA111.")
        return code

    def clean_credits(self):
        credits = self.cleaned_data.get('credits')
        if credits is None:
            raise forms.ValidationError("Credits are required.")
        if not (1 <= credits <= 10):
            raise forms.ValidationError("Credits must be between 1 and 10.")
        return credits
