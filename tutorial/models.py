from django.db import models
from datetime import datetime


# Create your models here.

################### USER ####################

class User(models.Model):
    # Attributes
    username = models.CharField(max_length=32)
    email = models.CharField(max_length=256)
    #password ??? see plugins

    # Methods
    def get_upvoted(self):
        "returns all upvoted tutorials"
        return Vote.objects.filter(user=self).filter(isPositive=True)
    def get_downvoted(self):
        "returns all downvoted tutorials"
        return Vote.objects.filter(user=self).filter(isPositive=False)

#############################################



################# TUTORIALS #################

# Tutorials have a dynamically generated index and are made up of chapters
class Tutorial(models.Model):
    # Attributes
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    author = models.ForeignKey(User) # From User app
    date_created = models.DateTimeField('date_created', auto_now_add=True)
    date_modified = models.DateTimeField('date_modified', auto_now_add=True)
    upvotes = models.IntegerField(default=1)
    downvotes = models.IntegerField(default=0)
    # tags = TaggableManager() #See: https://github.com/alex/django-taggit
    # locale ??? Search plugins for this
    is_public = models.BooleanField(default=False)

    # Methods
    def update_votes(self):
        "updates upvotes and downvotes value"
        self.upvotes = len(Vote.objects.filter(tutorial=self).filter(isPositive=True))
        self.downvotes = len(Vote.objects.filter(tutorial=self).filter(isPositive=False))

    def get_votes(self):
        return self.upvotes - self.downvotes

class Chapter(models.Model):
    # Attributes
    title = models.CharField(max_length=256)
    sequence = models.IntegerField(default=0)
    tutorial = models.ForeignKey(Tutorial)
    parent_chapter = models.ForeignKey('Chapter')
    content = models.CharField(max_length=16384)

    # Methods

    class Meta:
        unique_together = ('sequence', 'tutorial', 'parent_chapter') # Sequence is unique within the tutorial and/or parent chapter
        order_with_respect_to = 'tutorial'
        order_with_respect_to = 'parent_chapter'
        ordering = ('parent_chapter', 'sequence', 'tutorial')

#############################################



################### VOTE ####################

class Vote(models.Model):
    # Attributes
    isPositive = models.BooleanField(default=True)
    user = models.ForeignKey(User)
    tutorial = models.ForeignKey(Tutorial)

    # Methods

#############################################
