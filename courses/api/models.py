from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=45)
    imgpath = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = models.CharField(max_length=45)
    longitude = models.CharField(max_length=45)
    address = models.CharField(max_length=60)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)

    def __str__(self):
        return self.address


class Contact(models.Model):
    contacts = [
        (1, 'PHONE'),
        (2, 'FACEBOOK'),
        (3, 'EMAIL'),
    ]
    type = models.IntegerField(choices=contacts)
    value = models.CharField(max_length=100)
    course = models.ForeignKey("Course", on_delete=models.CASCADE)

    def __str__(self):
        return self.value


class Course(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='course')
    logo = models.ImageField(null=True)

    def __str__(self):
        return self.name
