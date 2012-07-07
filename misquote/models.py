from django.db import models


class Author(models.Model):
	author_name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return u'Author Name: %s' %(self.author_name)
	
class Quote(models.Model):
	quote = models.CharField(max_length=100)
	
	def __unicode__(self):
		return u'Quote: %s' %(self.quote)
