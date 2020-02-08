from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.urls import reverse
from products.slug import unique_slugify
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

Measuring_scale = (
    ('I', 'Items'),
    ('C', 'Carton'),
    ('P', 'Pack'),
    ('K', 'KG'),
    ('P', 'Pound'),
    ('M', 'Meter'),
    ('R', 'Room'),
)


class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_desc = models.CharField(max_length=50)
    category_pic = models.ImageField(upload_to='category_images', default='category_images/default.jpg')

    def __str__(self):
        return self.category_name


class product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.SET_DEFAULT, default=21)
    slug = models.SlugField()
    min_qty = models.CharField(max_length=10)
    max_qty = models.CharField(max_length=10)
    location = models.CharField(max_length=50)
    tags = TaggableManager(blank=True)
    desc = models.TextField()
    max_user = models.IntegerField(default=1)
    scale = models.CharField(choices=Measuring_scale, max_length=3)
    pub_date = models.DateField(default=datetime.now(), blank=True)
    image = models.ImageField(upload_to='shop/product_images', default='default.jpg')

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        slug = '%s' % (self.title)
        unique_slugify(self, slug)
        super(product, self).save()

    def get_absolute_url(self):
        return reverse('prod_view', kwargs={'slug': self.slug})


class ProductBooked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.FloatField()
    date = models.DateField(default=datetime.now())
    payment = models.BooleanField(default=False)

    def __str__(self):
        return self.items.title

    def get_total_item_price(self):
        return self.quantity * self.items.price

    def get_total(self):
        total = 0
        for item in ProductBooked:
            total += item.quantity * item.items.price
        return total


Priority = {
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
}


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(ProductBooked)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered_complete = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class UserNotes(models.Model):
    notes_user = models.ForeignKey(User, on_delete=models.CASCADE)
    notes_priority = models.CharField(choices=Priority, max_length=10)
    notes_text = models.TextField()


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    budget = models.BooleanField(default=False)
    time = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.user + ' ' + self.product
