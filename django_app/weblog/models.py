from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length = 100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length = 255, null = True, blank = True)
    body_text = models.TextField(null = True, blank = True)
    pub_date = models.DateField(null = True, blank = True)
    mod_date = models.DateField(null = True, blank = True)
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField(null = True, blank = True)
    n_pingbacks = models.IntegerField(null = True, blank = True)
    rating = models.IntegerField(null = True, blank = True)

    def __str__(self):
        return self.headline
