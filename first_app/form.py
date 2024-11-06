from django import forms
from django.core import validators
class LoginForm(forms.Form):
    name = forms.CharField(label = 'Full Name: ', help_text='Please Enter Your First & Last Name', required=False, widget=forms.Textarea(attrs={'id':'text_area', 'class':'class-1', 'placeholder':'Please Enter Your Full Name'}))
    email = forms.EmailField(label='User Email')
    file = forms.FileField()
    age = forms.IntegerField(label = "Age")
    birthday = forms.DateField(label='Birthday', widget= forms.DateInput(attrs = {'type': 'date'}))
    appointment = forms.DateTimeField(label='Appointment', widget= forms.DateInput(attrs = {'type': 'datetime-local'}))
    CHOICES = [('S','Small'), ('M', 'Medium'),('L', 'Large')]
    Select_Size = forms.ChoiceField(choices=CHOICES)
    Pizza = [('M','Mutton'), ('B', 'Beef'), ('C', 'Chicken')]
    Select_Item = forms.MultipleChoiceField(choices=Pizza)
    All_above_info_is_valid = forms.BooleanField()


# class validForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     def clean(self):
#         cleaned_data = super().clean()
#         name_val = self.cleaned_data['name']
#         email_val= self.cleaned_data['email']
#         if len(name_val) <10:
#             raise forms.ValidationError('Enter a name with at least 10 characters!')

#         if '.com' not in email_val:
#             raise forms.ValidationError('Email must contain ".com"')

def len_check(value):
    if len(value) <10:
        raise forms.ValidationError('Enter a value at least 10 chars')

class validForm(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(10, message='')])
    text = forms.CharField(widget=forms.TextInput, validators=[len_check])
    email = forms.CharField(widget=forms.EmailInput, validators=[validators.EmailValidator(message='Enter a valid Email')])
    age = forms.IntegerField(validators=[validators.MaxValueValidator(30, message='Age Must Maximum 30'), validators.MinValueValidator(18, message='Age must minimum 18')])
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message='File must be in pdf format!')])

