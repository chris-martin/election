from django.db import models

class Bill(models.Model):
  number = models.CharField(max_length = 20) # example: H.R. 3261
  nick = models.CharField(max_length = 200) # example: SOPA
  name = models.CharField(max_length = 200) # example: Stop Online Piracy Act
  def __unicode__(self):
    return self.nick

class Politician(models.Model):
  name = models.CharField(max_length = 100) # example: John Barrow
  def __unicode__(self):
    return self.name

class Supporter(models.Model):
  bill = models.ForeignKey(Bill)
  politician = models.ForeignKey(Politician)

