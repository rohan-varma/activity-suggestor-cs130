# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class RecommendedPlace(models.Model):
	place_name = models.CharField(max_length=200)
	place_ranking = models.IntegerField()
	num_times_shared = models.IntegerField()

	def __str__(self):
		return "{} {} {}".format(self.place_name, self.place_ranking, self.num_times_shared)

class TestModel(models.Model):
	text = models.CharField(max_length=200)

	def __str__(self):
		return "{}".format(self.text)