from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django import forms

from .models import Category, Tag, Post

class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = '__all__'

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)

