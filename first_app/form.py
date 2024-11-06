from django import forms

class LoginForm(forms.Form):
    name = forms.CharField(label = 'User Name')
    email = forms.EmailField(label='User Email')
    file = forms.FileField()
    age = forms.IntegerField(label = "Age")
    CHOICES = [('S','Small'), ('M', 'Medium'),('L', 'Large')]
    Select_Size = forms.ChoiceField(choices=CHOICES)
    Pizza = [('M','Mutton'), ('B', 'Beef'), ('C', 'Chicken')]
    Select_Item = forms.MultipleChoiceField(choices=Pizza)
    All_above_info_is_valid = forms.BooleanField()
