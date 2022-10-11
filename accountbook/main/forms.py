from django import forms
from .models import Consume


class ArticleForm(forms.ModelForm):
    date = forms.DateField(
        label='날짜',
        widget=forms.DateField(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the title',
                'maxlength': 10,
            }
        )
    )

    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the content',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={
            'required': '내용을 입력하세요.',
        }
    )

    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
