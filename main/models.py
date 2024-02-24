from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

#stocker les informations de l'api en bdd
class PredApi(models.Model):

    NEW_EXIST_CHOICES = (
        (1, 'Existing business'),
        (2, 'New business'),
    )
    URBANRURAL_CHOICES = (
        (1, 'Urban'),
        (2, 'Rural'),
        (0, 'Undefined'),
    )
    REVLINECR_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
    LOWDOC_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    State = models.CharField(max_length=2)
    BankState = models.CharField(max_length=2)
    RevLineCr = models.CharField(max_length=1,choices=REVLINECR_CHOICES)
    LowDoc = models.CharField(max_length=1,choices=LOWDOC_CHOICES)
    NewExist = models.IntegerField(choices=NEW_EXIST_CHOICES)
    UrbanRural = models.IntegerField(choices=URBANRURAL_CHOICES)
    FranchiseBinary = models.IntegerField()
    Zip = models.IntegerField()
    NAICS = models.IntegerField()
    Term = models.IntegerField()
    NoEmp = models.IntegerField()
    CreateJob = models.IntegerField()
    RetainedJob = models.IntegerField()
    FranchiseCode = models.IntegerField()
    GrAppv = models.FloatField()
    SBA_Appv = models.FloatField()
    Industry = models.CharField(max_length=50)
    #stocker la prédiction elle-même
    Prediction = models.IntegerField(null=True, blank=True)  #null et blank=True pour permettre de sauvegarder sans prédiction initialement

    def __str__(self):
        return f"Prediction for {self.State} - {self.Industry}"