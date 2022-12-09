from .models import Article
from django.forms import ModelForm, TextInput, DateInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'full_text', 'date', 'series']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название аниме'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор аниме'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание аниме'
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "series": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество серий'
            })
        }