from django import forms


class KondorseForm(forms.Form):
    CHOICES = (
        ('1', 'A'),
        ('2', 'B'),
        ('3', 'C'),
    )
    place1 = forms.ChoiceField(choices = CHOICES)
    place2 = forms.ChoiceField(choices = CHOICES)
    place3 = forms.ChoiceField(choices = CHOICES)