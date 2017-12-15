"""
Models defines our models.
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class RecommendedPlace(models.Model):
	"""
	RecommendedPlace is a model for our recommended places.
	"""
	place_name = models.CharField(max_length=200)
	place_ranking = models.IntegerField()
	num_times_shared = models.IntegerField()

	def __str__(self):
		"""__str__ gives a string representation of our place
    	:return: String representation of the model
		"""
		return "{} {} {}".format(self.place_name, self.place_ranking, self.num_times_shared)