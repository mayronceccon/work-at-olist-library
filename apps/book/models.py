import datetime
from django.db import models
from utils.validators import year_validator
from apps.author.models import Author


class Book(models.Model):
    name = models.CharField(max_length=254)
    edition = models.CharField(max_length=10)
    publication_year = models.IntegerField(
        validators=[year_validator]
    )
    authors = models.ManyToManyField(
        Author,
        related_name="books"
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.strip()
        super(Book, self).save(*args, **kwargs)

    class Meta:
        unique_together = ("name", "edition",)
