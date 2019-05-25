from django import forms
from django.template.defaultfilters import slugify

from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['blog_url', 'twitter_handle', 'location', 'bio']
        exclude = ['user', 'slug']

        def save(self):
            instance = super(PostForm, self).save(commit=False)
            instance.slug = slugify(instance.name)
            instance.save()
            return instance
