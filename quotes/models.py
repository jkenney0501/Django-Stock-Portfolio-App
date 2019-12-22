from django.db import models

# Create  models here.

class Stock(models.Model):
	ticker = models.CharField(max_length=10)
	#pay attention ot use double unerscores or you will get "stock object" as your DB output
	def __str__(self):
		return self.ticker


