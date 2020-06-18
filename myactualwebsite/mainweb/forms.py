from django import forms
from mainweb.models import Prospect

class NewProspect(forms.ModelForm):
    class Meta:
        model = Prospect
        fields = "__all__"

