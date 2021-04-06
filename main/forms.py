from django import forms
from .models import MyModel


class MyForm(forms.ModelForm):
    # Defines form attributes
    class Meta:
        model = MyModel
        fields = ["first_name", "middle_name", "last_name", "age", ]
        # Customizes form field labels to display
        labels = {'first_name': "Name", 'middle_name': "Middle", 'last_name': "Last", 'age': "Age", }
