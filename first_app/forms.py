from django import forms

class LoginForm(forms.Form):
    name = forms.CharField (label = "User Name")
    file = forms.FileField()
    # email = forms.EmailField (label = "User Email")
    # age = forms.IntegerField (label = "Age")
    # weight = forms.FloatField(label = "Weight")
    # balance = forms.DecimalField(label = "Balance")
    # check = forms.BooleanField(label = "All info is checked")
    # birthday = forms.DateField(label = "Birth Day")
    # appointment = forms.DateTimeField(label="Appointment")
    # CHOICES = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
    # size = forms.ChoiceField(choices=CHOICES)
    # Meal = [('P', 'Pizza'), ('B', 'Burger'), ('M', 'Mashroom')]
    # item = forms.MultipleChoiceField(choices=Meal)
