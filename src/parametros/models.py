from django.db import models
from ckeditor.fields import RichTextField
#IMPORTAMOS LA LISTA

    def __unicode__(self):
        return self.NombEtni


class TipoDocu(models.Model):
    NombtiDo = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.NombtiDo


class EstaCivil(models.Model):
    NombEsCi = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.NombEsCi


class TipoEstu(models.Model):
    NombTiEs = models.CharField(max_length = 50) 
    def __unicode__(self):
        return self.NombTiEs


class TipoLogr(models.Model):
    NombTiLo = models.CharField(max_length = 50)
    def __unicode__(self):
        return self.NombTiLo