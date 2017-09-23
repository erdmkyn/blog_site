from django.db import models



# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile')
    userImg = models.ImageField(blank=True, null=True)
    user_img_path=models.CharField(blank=True,null=True,max_length=500)
    user_bio=models.TextField(max_length=250,null=True,blank=True)
    control = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username + ' Profile'

    class Meta:
        verbose_name_plural='kullanıcı profilleri'
        verbose_name='kullaıcı profili'




