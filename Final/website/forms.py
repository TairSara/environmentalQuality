from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, products
from django.utils.translation import gettext_lazy as _

class PrivateSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    location = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.usertype = False
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')  # Fixed typo here
        user.email = self.cleaned_data.get('email')
        user.location = self.cleaned_data.get('location')
        if commit:
            user.save()
        return user

class CorpSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    location = forms.CharField(required=True)
    comp_num = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.usertype = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')  
        user.email = self.cleaned_data.get('email')
        user.location = self.cleaned_data.get('location')
        user.comp_num = self.cleaned_data.get('comp_num')
        if commit:
            user.save()
        return user
    

class ProductForm(forms.ModelForm):
    class Meta:
        model = products
        fields = ["id", "product_name", "Product_type", "value", "bin_type"]
        labels = {
            "id": _("מזהה"),
            "product_name": _("שם מוצר"),
            "Product_type": _("סוג מוצר"),
            "value": _("מחיר/נקודות"),
            "bin_type": _("סוג פח"),
        }

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        self.fields['bin_type'].required = False
        
    def clean(self):
        cleaned_data = super().clean()
        pID = cleaned_data.get('id')
        product_name = cleaned_data.get('product_name')
        bin_type = cleaned_data.get('bin_type')
        Product_type = cleaned_data.get('Product_type')
        value = cleaned_data.get('value')
        # Custom validation example
        # if pID is not None:
        #     raise forms.ValidationError(pID)
        if Product_type == False and not bin_type:
            raise forms.ValidationError("עבור מוצרי מיחזור חייב לבחור סוג פח" + str(pID))

        if value and value < 0:
            raise forms.ValidationError("ערך מחיר/נקודות צריך להיות גדול מ-0")

        return cleaned_data