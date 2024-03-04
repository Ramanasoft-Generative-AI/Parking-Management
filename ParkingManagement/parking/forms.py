from django import forms
from .models import Category
from .models import AddVehicle

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['parking_area_no', 'vehicle_type', 'vehicle_limit', 'parking_charge']

        widgets = {
            'parking_area_no': forms.TextInput(attrs={'class:': 'form-control'}),
            'vehicle_type': forms.TextInput(attrs={'class:': 'form-control'}),
            'vehicle_limit': forms.TextInput(attrs={'class:': 'form-control'}),
            'parking_charge': forms.TextInput(attrs={'class:': 'form-control'}),
        }

class AddVehicleForm(forms.ModelForm):
    class Meta:
        model = AddVehicle
        fields = ['vehicle_no', 'vehicle_type', 'parking_area_no', 'parking_charge']

        widgets = {
            'vehicle_no': forms.TextInput(attrs={'class:': 'form-control'}),
            'vehicle_type': forms.TextInput(attrs={'class:': 'form-control'}),
            'parking_area_no': forms.TextInput(attrs={'class:': 'form-control'}),
            'parking_charge': forms.TextInput(attrs={'class:': 'form-control'}),
        }

