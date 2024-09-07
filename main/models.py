from django.db import models


class TimeSimple(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeSimple):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Post(TimeSimple):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
