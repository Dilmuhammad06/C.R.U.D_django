from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','text','slug']


class UpdateForm(PostForm):
    def __init__(self, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            instance = kwargs['instance']
            self.fields['title'].initial = instance.title
            self.fields['text'].initial = instance.text
            self.fields['slug'].initial = instance.slug