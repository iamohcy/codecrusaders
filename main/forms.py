from django.contrib.auth.models import User
from django import forms

# class RegistrationForm(forms.Form):

#     username = forms.RegexField(regex=r'^\w+$')
#     email = forms.EmailField()
#     full_name = forms.CharField()
#     password = forms.CharField()
#     dob = forms.DateField()

#     def clean_username(self):
#         try:
#             user = User.objects.get(username=self.cleaned_data['username'])
#         except User.DoesNotExist:
#             return self.cleaned_data['username']
#         raise forms.ValidationError("The username already exists. Please try another one.")

# class NewGrumbForm(forms.Form):
#     text = forms.CharField(max_length=140)
#     image = forms.ImageField(required=False)

# class NewCommentForm(forms.Form):
#     grumb_id = forms.DecimalField()
#     text = forms.CharField(max_length=2000)
#     image = forms.ImageField(required=False)

# class ProfileAboutMeForm(forms.Form):
#     text = forms.CharField(max_length=2000, required=False)

# class ProfileLinksForm(forms.Form):
#     text = forms.CharField(max_length=500, required=False)

# class ProfileContactsForm(forms.Form):
#     phone = forms.CharField(max_length=20, required=False)
#     email = forms.EmailField(required=False)
#     address = forms.CharField(max_length=200, required=False)
#     website = forms.URLField(required=False)
#     facebook = forms.URLField(required=False)

# class ImageForm(forms.Form):
#     image = forms.ImageField()

# class SearchForm(forms.Form):
#     text = forms.CharField(max_length=200, required=False)
