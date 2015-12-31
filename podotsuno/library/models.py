from django.db import models


class Fandom(models.Model):
	name = models.CharField(max_length=255)


class Pairing(models.Model):
	name = models.CharField(max_length=255)


class Author(models.Model):
	name = models.CharField(max_length=255)


class Podfic(models.Model):

	title = models.CharField(max_length=255)

	status = models.CharField()

	authors = models.ManyToManyField('Author')
	fandoms = models.ManyToManyField('Fandom')

	has_author_agreement = models.BooleanField(default=False)
