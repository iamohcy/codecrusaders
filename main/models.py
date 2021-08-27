from django.db import models
from django.contrib.auth.models import User
import os
from uuid import uuid4

# Credits: http://stackoverflow.com/questions/15140942/django-imagefield-change-file-name-on-upload
def path_and_rename(path):
    def wrapper(instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return os.path.join(path, filename)
    return wrapper

# # Create your models here.
# class Grumb(models.Model):
#     class Meta:
#         ordering = ['-datetime']

#     dislikes = models.ManyToManyField(User, related_name='grumb_dislike_set')
#     user = models.ForeignKey(User, related_name='grumb_set')
#     text = models.CharField(max_length=200)
#     image = models.ImageField(upload_to=path_and_rename('grumb_pic/'))
#     datetime = models.DateTimeField()
#     datetime_str = models.CharField(max_length=20)

#     def __unicode__(self):
#         return self.user.username + ": " + self.text

# class Comment(models.Model):
#     class Meta:
#         ordering = ['datetime']

#     grumb = models.ForeignKey(Grumb)
#     dislikes = models.ManyToManyField(User, related_name='comment_dislike_set')
#     user = models.ForeignKey(User, related_name='comment_set')
#     text = models.CharField(max_length=200)
#     image = models.ImageField(upload_to=path_and_rename('comment_pic/'))
#     datetime = models.DateTimeField()
#     datetime_str = models.CharField(max_length=20)

#     def __unicode__(self):
#         return self.user.username + ": " + self.text

# class Link(models.Model):
#     url = models.URLField()

#     def __unicode__(self):
#         return self.url

# class Profile(models.Model):
#     verification_code = models.CharField(max_length=60)

#     profile_pic = models.ImageField(upload_to=path_and_rename('profile_pic/'))

#     about_me = models.CharField(max_length=1000, blank=True)

#     contact_phone = models.CharField(max_length=20, blank=True)
#     contact_email = models.EmailField(blank=True)
#     contact_address = models.CharField(max_length=200, blank=True)
#     contact_website = models.URLField(blank=True)
#     contact_facebook = models.URLField(blank=True)

#     links = models.ManyToManyField(Link)

#     user = models.OneToOneField(User)
#     followed_user = models.ManyToManyField(User, related_name='followed_user_set')
#     blocked_user = models.ManyToManyField(User, related_name='blocked_user_set')

#     def __unicode__(self):
#         return self.user.username + ": " + self.contact_email

    # def save(self):
    #     super(Profile, self).save()

    #     image_path = self.profile_pic.path
    #     image = Image.open(image_path)

    #     max_width = 500
    #     max_height = 500
    #     image = ImageOps.fit(image, (max_width, max_height,), method=Image.ANTIALIAS)
    #     image.save(image_path)

    #     super(Profile, self).save()
