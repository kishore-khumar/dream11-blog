from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'Start with your name.. eg, i am johnson,this is awesome blog','class':'box'}))
    class Meta:
        model=Comment
        fields=('content',)