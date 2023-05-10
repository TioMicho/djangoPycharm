from django.db import models


class Person(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    birth = models.DateField()
    height = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    weight = models.DecimalField(max_digits=6, decimal_places=3, null=True, blank=True)

    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    def __str__(self):
        return self.fullname()


class Tweet(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    message = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'@{self.author} dice "{self.message}"'