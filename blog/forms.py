from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'is_published', 'price')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter the title opf your post', 'maxlength': 120}),
            'content': forms.Textarea(attrs={'placeholder': 'Enter the content'}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) <= 2:
            raise forms.ValidationError('The title should have more than 2 characters.')

        return title.strip()
