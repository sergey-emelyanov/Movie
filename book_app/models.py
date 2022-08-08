from django.db import models
from pytils.translit import slugify
from django.urls import reverse

class BookShop(models.Model):
	title = models.CharField(max_length=70)
	rating = models.IntegerField()
	is_best_seller = models.BooleanField()
	author = models.CharField(max_length=100,null=True)
	slug = models.SlugField(default='', null=False)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(BookShop, self).save(*args, **kwargs)


	def get_url(self):
		return reverse('book-details', args=[self.slug])

	def __str__(self):
		return f"{self.title} {self.rating}"
