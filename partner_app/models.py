from django.db import models
from phonenumber_field.formfields import PhoneNumberField
from django.core.validators import RegexValidator

ROLE_CHOICES = (
	("Guest", "Guest"),
	("Orbiter", "Orbiter"),
	("Cosmonaut", "Cosmonaut"),
)
# Partner Model
phone_regex = RegexValidator(regex=r'^(\+\d{1,3})?,?\s?\d{8,13}', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class partner(models.Model):
    phonenumber = models.CharField(validators=[phone_regex], max_length=17, blank=True,primary_key=True) # Validators should be a list
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    role=models.CharField(choices=ROLE_CHOICES,default="Orbitor",max_length=60)
    registeration= models.DateTimeField(auto_now_add=True)
    attendance=models.IntegerField(default=0)
    foodcounter=models.IntegerField(default=0)
    # image = models.FileField(blank=True)

    def __str__(self):
        return self.phonenumber

class postimage(models.Model):
    post = models.ForeignKey(partner, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
    img_description=models.CharField(max_length=30)
 
    def __str__(self):
        return self.post.phonenumber


