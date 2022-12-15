from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

#class NewUser(AbstractUser):
 #   pass

   # email = models.CharField(max_length=100)
  #  image = models.ImageField(upload_to='uploads/', blank=True, null=True)
  #  date_of_birth = models.DateTimeField(null=True)


#class Profile(models.Model):
   # user = models.OneToOneField(User, on_delete=models.CASCADE)
   # email = models.CharField(max_length=100)
    #image = models.ImageField(upload_to='uploads/', blank=True, null=True)
   # date_of_birth = models.DateTimeField()

  #  @receiver(post_save, sender=User)
  #  def create_user_profile(sender, instance, created, **kwargs):
   #     if created:
    #        Profile.objects.create(user=instance)
    
   # @receiver(post_save, sender=User)
   # def save_user_profile(sender, instance, **kwargs):
   #     instance.profile.save()





class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    end_date = models.DateTimeField()
    bid_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}'
        
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''


class Auction(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bid = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    
    def __str__(self):
        return "USER_ID: " + str(self.bid)
    
    #def get_image(self):
    #    if self.image:
    #        return "http://localhost:8080" + self.image.url
    #    return ''


class Question(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    question_text = models.TextField(blank=True, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "USER_ID: " + str(self.question_text)


class Answers(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return "USER_ID: " + str(self.answer)