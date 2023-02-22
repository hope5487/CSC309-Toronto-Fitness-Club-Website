from django.contrib.auth import get_user_model
from django import forms
from django.core.exceptions import ValidationError

from banks.models import Bank, Branch


class BankAddForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['name', 'description', 'inst_num', 'swift_code']

    def __init__(self, *args, **kwargs):
        super(BankAddForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['description'].required = False
        self.fields['inst_num'].required = False
        self.fields['swift_code'].required = False

    def clean(self):
        cleaned_data = super().clean()
        errors = {}
        if len(cleaned_data['name']) is 0:
            errors['name'] = ValidationError("This field is required")
        if len(cleaned_data['description']) is 0:
            errors['description'] = ValidationError("This field is required")
        if len(cleaned_data['inst_num']) is 0:
            errors['inst_num'] = ValidationError("This field is required")
        if len(cleaned_data['swift_code']) is 0:
            errors['swift_code'] = ValidationError("This field is required")
        if errors:
            raise ValidationError(errors)
        return cleaned_data


class BranchAddForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['name', 'transit_num', 'address', 'email', 'capacity']

    def __init__(self, *args, **kwargs):
        super(BranchAddForm, self).__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['transit_num'].required = False
        self.fields['address'].required = False
        self.fields['email'].required = False
        self.fields['capacity'].required = False

    def clean(self):
        cleaned_data = super().clean()
        errors = {}
        if 'name' in cleaned_data and len(cleaned_data['name']) is 0:
            errors['name'] = ValidationError("This field is required")
        if 'transit_num' in cleaned_data and len(cleaned_data['transit_num']) is 0:
            errors['transit_num'] = ValidationError("This field is required")
        if 'address' in cleaned_data and len(cleaned_data['address']) is 0:
            errors['address'] = ValidationError("This field is required")
        if 'email' in cleaned_data and len(cleaned_data['email']) is 0:
            errors['email'] = ValidationError("This field is required")
        if errors:
            raise ValidationError(errors)
        return cleaned_data


