from django import forms
from .models import Todo


class TodoCreateForm(forms.ModelForm):
    # titlef = forms.CharField(label="Title", required=False)
    # bodyf = forms.CharField(label="Body")
    # createdf = forms.DateTimeField(label="Created")
    class Meta:
        model = Todo
        fields = "__all__"


class TodoUpdateform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'body', 'created')
