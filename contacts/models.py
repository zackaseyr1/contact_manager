from django.db import models

class Contact(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    REGION_CHOICES = [
        ('Awdal', 'Awdal'),
        ('Bakool', 'Bakool'),
        ('Banaadir', 'Banaadir'),
        ('Bari', 'Bari'),
        ('Bay', 'Bay'),
        ('Galguduud', 'Galguduud'),
        ('Gedo', 'Gedo'),
        ('Hiraan', 'Hiraan'),
        ('Jubbada Dhexe', 'Jubbada Dhexe'),
        ('Jubbada Hoose', 'Jubbada Hoose'),
        ('Mudug', 'Mudug'),
        ('Nugaal', 'Nugaal'),
        ('Sanaag', 'Sanaag'),
        ('Shabeellaha Dhexe', 'Shabeellaha Dhexe'),
        ('Shabeellaha Hoose', 'Shabeellaha Hoose'),
        ('Sool', 'Sool'),
        ('Togdheer', 'Togdheer'),
        ('Woqooyi Galbeed', 'Woqooyi Galbeed'),
    ]

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    region = models.CharField(max_length=100, choices=REGION_CHOICES)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_added = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name
