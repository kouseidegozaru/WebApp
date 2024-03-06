from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    gender_choices=[
        ('男','男'),
        ('女','女'),
        ('その他','その他'),
    ]

    gender = forms.ChoiceField(choices=gender_choices)

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = '名'
        self.fields['last_name'].label = '姓'
        self.fields['email'].label = 'メールアドレス'
        self.fields['phone_number'].label = '電話番号'
        self.fields['age'].label = '年齢'
        self.fields['gender'].label = '性別'

    class Meta:
        model = Customer
        fields = ['last_name', 'first_name', 'email', 'phone_number','age','gender']
