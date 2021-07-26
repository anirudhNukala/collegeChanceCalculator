from django.db import models


# Create your models here.
class AdmissionStats(models.Model):
    male_yield = models.IntegerField()
    male_selectivity = models.IntegerField()
    female_yield = models.IntegerField()
    female_selectivity = models.IntegerField()
            
  

class Scores(models.Model):
    act_compostite25 = models.IntegerField()
    act_english25 = models.IntegerField()
    act_math25 = models.IntegerField()
    sat_compostite25 = models.IntegerField()
    sat_english25 = models.IntegerField()
    sat_math25= models.IntegerField()
    act_composite75 = models.IntegerField()
    act_english75 = models.IntegerField()
    act_math75 = models.IntegerField()
    sat_composite75 = models.IntegerField()
    sat_english75 = models.IntegerField()
    sat_math75= models.IntegerField()

   

class College(models.Model):
    name = models.CharField(max_length=200)
    ipeds = models.IntegerField()
    scores = models.OneToOneField(Scores, on_delete=models.CASCADE,)
    AdmissionStats = models.OneToOneField(AdmissionStats, on_delete=models.CASCADE,)
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=200)
    act_composite = models.IntegerField()
    act_english = models.IntegerField()
    act_math = models.IntegerField()
    sat_composite = models.IntegerField(null=True)
    sat_english = models.IntegerField()
    sat_math = models.IntegerField()
    def __str__(self):
        return self.name
