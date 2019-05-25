from django import forms
from django.forms import ModelForm
from blog.models import Entry


class EntryForm(ModelForm):

    class Meta:

        model = Entry

        # fields = ['blog', 'headline']
        ''
        fields = '__all__'

        widgets = {
            'body_text': forms.Textarea(attrs={'style': 'background-color:red'}),  # 关键是这一行
        }













class NameForm(forms.Form):

    username = forms.CharField(label='Your Name', max_length=100)


BIRTH_YEAR_CHOICES = ('1980', '1981', '1982', '2000')
FAVORITE_COLORS_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'subject',
                                                                           'style': 'background-color:red'}))
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )

