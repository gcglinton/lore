from django.db import models

from django.utils.translation import gettext_lazy as _

# Create your models here.



STAKEHOLDER_ROLES = {
    "new": "New",
    "approved": "Approved",
    "queued": "Queued",
    "rejected": "Rejected",
    "in_progress": "In Progress",
}


class SBDA(models.Model):
   name = models.CharField(max_length=200)
   name_fr = models.CharField(max_length=200)
   code = models.CharField(max_length=20)
   code_cloud = models.CharField(max_length=2)

class People(models.Model):
   class Roles(models.TextChoices):
      EVO = "LT_EVO", _("LegoTeam - EVO")
      OPS = "LT_OPS", _("LegoTeam - Ops")
   name_first = models.CharField(max_length=200)
   name_last = models.CharField(max_length=200)
   email = models.EmailField()
   partner = models.ForeignKey(SBDA, on_delete=models.PROTECT)
   phone = models.CharField(max_length=10)
   is_lego_team = models.BooleanField(default=False)

   def __str__(self):
      return f"{self.name_last}, {self.name_first}"

def get_evo():
   return {i: i for i in People.objects.all()}

class Experiment(models.Model):
   class Status(models.IntegerChoices):
      New = 1
      Approved = 2
      Queued = 3
      Rejected = 4
      In_Progress = 5   
   
   name = models.CharField(max_length=20)
   name_long = models.CharField(max_length=200)
   #stakeholders = models.ManyToManyField(People, related_name="experiment_stakeholders")
   status = models.IntegerField(choices=Status, default=1)
   sbda = models.OneToOneField(SBDA, on_delete=models.PROTECT, default=-1)

   def __str__(self):
      return self.name

class ExperimentPeople(models.Model):
   exp_id = models.OneToOneField(Experiment, on_delete=models.PROTECT)
   person = models.OneToOneField(People, on_delete=models.PROTECT)
   role = models.CharField(choices=People.Roles, max_length=200)
