from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Movie(models.Model):
	name = models.CharField(max_length=40)
	rating = models.IntegerField()
	year = models.IntegerField(null=True)
	budget = models.IntegerField(default=100000)
	slug = models.SlugField(default='',null=False)

	def save(self, *args, **kwargs):
		self.slug=slugify(self.name)
		super(Movie, self).save(*args, **kwargs)

	def get_url(self):
		return reverse('movie-details', args=[self.slug])

	def __str__(self):
		return f"{self.name} {self.rating}"
