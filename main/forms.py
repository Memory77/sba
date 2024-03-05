from django import forms 
from .models import PredApi


class PredApiForm(forms.ModelForm):
    class Meta:
        model = PredApi
        fields = ['State', 'Zip','BankState', 'RevLineCr', 'LowDoc', 'NewExist', 'UrbanRural', 'FranchiseCode', 'NAICS', 'Term'
                  ,'NoEmp','CreateJob','RetainedJob','GrAppv','SBA_Appv']
        labels = {
                "State": "Select your state",
                "Zip": "Enter your state's ZIP code",
                "BankState": "Bank state",
                "RevLineCr": "Revolving line of credit",
                "LowDoc": "Low-doc",
                "NewExist": "New or existing",
                "UrbanRural": "Urban or rural",
                "FranchiseCode": "Enter franchise code",
                "NAICS": "Enter NAICS numbers",
                "Term": "Term",
                "NoEmp": "Number of employees",
                "CreateJob": "Number of jobs created",
                "RetainedJob": "Number of jobs retained",
                "GrAppv": "Approved loan amount",
                "SBA_Appv": "SBA-approved loan amount"
        }
        
    def save(self, commit=True):
        instance = super().save(commit=False)
        
        # Ici, vous pouvez inclure la logique pour définir FranchiseBinary et Industry
        instance.FranchiseBinary = 0 if instance.FranchiseCode in [0, 1] else 1
        instance.Industry = instance.map_naics_to_industry()

        if commit:
            instance.save()
            self.save_m2m()
        return instance