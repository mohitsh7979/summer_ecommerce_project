from django import forms 


class StudentForm(forms.Form):
    FullName = forms.CharField()
    Email = forms.EmailField()
    Roll_no = forms.IntegerField()
    Mobile_No = forms.IntegerField()
    Address = forms.CharField()
    Pin_code = forms.IntegerField()
    Image = forms.ImageField()
    