from django import forms
from .models import Post, Comment
from django_ckeditor_5.widgets import CKEditor5Widget


class PostCreateForm(forms.ModelForm):
    """
    Форма добавления статей на сайте
    """

    class Meta:
        model = Post
        fields = ('title', 'category', 'description', 'text', 'thumbnail', 'status', 'tags')

        widgets = {
            # Применяем CKEditor только для полей 'description' и 'text'
            'description': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            ),
            'text': CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="extends"
            )
        }

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in ['text', 'description']:
                self.fields[field].widget.attrs.update({
                    'class': 'form-control',
                    'autocomplete': 'off'
                })

class PostUpdateForm(PostCreateForm):
    """
    Форма обновления статьи на сайте
    """

    class Meta:
        model = Post
        fields = PostCreateForm.Meta.fields + ('fixed', )

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)

        self.fields['fixed'].widget.attrs.update({
            'class': 'form-check-input'
        })


class CommentCreateForm(forms.ModelForm):
    """
    Форма добавления комментариев к статьям
    """
    parent = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={'cols': 30, 'rows': 5, 'placeholder': 'Комментарий', 'class': 'form-control'}))

    class Meta:
        model = Comment
        fields = ('content',)