from django.db import models

# Create your models here.

''' Models for questions '''
class Question(models.Model):
	'''text feild for question'''
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	'''for string convertion of question model'''
	def __str__(self):
		return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):            
        return self.choice_text

