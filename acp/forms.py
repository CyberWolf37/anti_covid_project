from django import forms

class FightForm(forms.Form):
    name = forms.CharField(max_length=30)
    lastname = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    social_security_usr = forms.DecimalField()

    def clean(self):
        cleaned_data = super(FightForm, self).clean()
        name = cleaned_data.get('name')
        lastname = cleaned_data.get('lastname')
        email = cleaned_data.get('email')
        social_security_usr = cleaned_data.get('social_security_usr')
        if not name and not email and not lastname and not social_security_usr:
            raise forms.ValidationError('You have to write something!')
        elif not name or not email or not social_security_usr:
            raise forms.ValidationError('Nous avons besoin d\'un nom, d\'un email et d\'un numéro de sécurité sociale')