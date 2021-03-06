from django.db import models
from mongoengine import *
# Create your models here.


class Comment(EmbeddedDocument):
	content = StringField(max_length=256)
	rating = IntField()

	#def __str__(self):
	#	return "Comment(content = '%s', rating = %s)"% (self.content, str(self.rating))

	#def ratingText(self):
	#	return Blog.RATING_CHOICES[self.rating-1][1]

class Blog(Document):

	title = StringField(max_length=256)
	post_date = DateTimeField('Post Date')
	reply_to = EmailField('Reply To')
	content = StringField()
	comments = ListField(EmbeddedDocumentField(Comment))
	#def __str__(self):
	#	return "Blog(title = '%s')"%(self.title)

	def rating(self):
		#@To Do : Rating Calcuation
		return None

#	def __unicode__(self):
#       	return self.title

	RATING_CHOICES = (
		 (1 , 'Lame'),
		 (2 , 'Weak'),
		 (3 , 'OK'),
		 (4 , 'Nice'),
		 (5 , 'Rocks'),
		 )






