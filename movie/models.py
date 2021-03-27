from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'users/user_{0}/{1}'.format(instance.user.id, filename)


class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length= 10)
    bio = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to=user_directory_path, blank=True)

    def get_absolute_url(self):
        return reverse('movie:index')

    def __str__(self):
        return self.user.username




