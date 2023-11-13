from .models import Todo
from django import forms
class TodoForm(forms.ModelForm):
    """Form definition for Todo."""

    class Meta:
        """Meta definition for Todoform."""
        model = Todo
        fields = ('name','images')
        labels = {
            'name': 'Enter Your Name',
            'images': 'Upload Your Picture',
        }
    
    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder']='Enter Your Name'
        self.fields['images'].widget.attrs['placeholder']='Upload Your Profile Photo'
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
    
    
