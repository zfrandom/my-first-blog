from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model): #the post is a django model, so django knows that it should be saved in teh databse
	author = models.ForeignKey('auth.User') #a link to another model. Many to one relationship
	title = models.CharField(max_length=200) #text with a limited unm of char
	text = models.TextField() #long text without limit
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null= True)
	def publish(self):
		self.published_date=timezone.now()
		self.save() #save the object to the database
	def __str__(self):
		return self.title

