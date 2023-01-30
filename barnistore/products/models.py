from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField('name', max_length=200)
    slug = models.SlugField('slug', max_length=200)
    description = models.TextField('description', blank=True)
    price = models.IntegerField('price')
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='products')
    image = models.ImageField('image', upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name
