from django import forms
from blog.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content", "image", "price")
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Enter the title opf your post", "maxlength": 120}),
            "content": forms.Textarea(attrs={"placeholder": "Enter the content"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) <= 2:
            raise forms.ValidationError("The title should have more than 2 characters.")
        if type(title[:1]) == int:
            raise forms.ValidationError("The title shouldn't begin with a number.")

        return title.strip()

    def clean_content(self):
        content = self.cleaned_data["content"]
        if len(content) <= 20:
            raise forms.ValidationError("Too short content.")

        return content.strip()
