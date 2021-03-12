from django.db import models

class Books(models.Model):
    book_name = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published',null=True)
    author = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.book_name