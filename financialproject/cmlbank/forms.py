from django import forms
from .models import Registration



class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
    #     widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
    #          'districts': forms.Select(attrs={'class': 'form-select'}),
    #          'branch': forms.Select(attrs={'class': 'form-select'}),
    #     }
    #
    # def __int__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['branch'].queryset = Branch.objects.all()     #none -
    #
    #     if 'district' in self.data:
    #         try:
    #             district = int(self.data.get('district'))
    #             self.fields['branch'].queryset = Branch.objects.filter(district=district).order_by('name')
    #         except (ValueError, TypeError):
    #             pass
    #     elif self.instance.pk:
    #         self.fields['branch'].queryset = self.instance.country.city_set.order_by('name')
