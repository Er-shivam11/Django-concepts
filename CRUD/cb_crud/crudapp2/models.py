from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
# import the standard Django Model
# from built-in library


# declare a new model with a name "GeeksModel"
class ShivamBytes(models.Model):

	# fields of the model
	name = models.CharField(max_length = 200)
	city = models.CharField(max_length = 200)
	description = models.TextField()

	# renames the instances of the model
	# with their title name
	def __str__(self):
		return self.name
