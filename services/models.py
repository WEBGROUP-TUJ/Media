from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True)

    def __str__(self):
        return self.name

    def __len__(self):
        return len([i for i in self.service_set.all()])

    class Meta:
        verbose_name_plural = 'Categories'


class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.name


class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name