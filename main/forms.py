from django import forms 
from .models import PredApi


class PredApiForm(forms.ModelForm):
    class Meta:
        model = PredApi
        fields = ['State', 'Zip','BankState', 'RevLineCr', 'LowDoc', 'NewExist', 'UrbanRural', 'FranchiseCode', 'NAICS', 'Term'
                  ,'NoEmp','CreateJob','RetainedJob','GrAppv','SBA_Appv']
        labels = {
            "State": "Selectionnez l'Etat",
            "Zip": "Renseignez le code zip de votre état",
            "BankState": "l'Etat de la banque",
            "RevLineCr": "Revlinecr",
            "LowDoc": "Lowdoc",
            "NewExist": "Nouveauté",
            "UrbanRural": "Urban/Rural",
            "FranchiseCode": "Entrez votre code de franchise",
            "NAICS": "Entrez vos numéros NAICS",
            "Term": "Term",
            'NoEmp': "Nombre d'employés",
            'CreateJob': "Nombre d'emplois créés",
            'RetainedJob': "Nombre d'emplois retenus",
            'GrAppv': 'Montant approuvé',
            'SBA_Appv':'Montant approuvé par la SBA'
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