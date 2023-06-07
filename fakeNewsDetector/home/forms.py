from django import forms
from home.models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['sourceURL', 'newsContent']
