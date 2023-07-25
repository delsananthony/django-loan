from django import forms
from .models import Member


class MemberForm(forms.Form):
    firstname = forms.CharField(max_length=225)
    lastname = forms.CharField(max_length=225)
    middlename = forms.CharField(max_length=225)


class MembersForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"

        # fields = ('name','gender','dob','mobile','email','aadhaar','country','address')

        # widgets = {
        #     'dob': forms.DateInput(attrs={'type':'date'}),
        #     'address':forms.Textarea(attrs={'cols':10,'rows':3})
        # }
        # labels = {
        #     'name':'Display Name'
        # }
