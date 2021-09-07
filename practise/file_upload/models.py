from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdf/')
    cover = models.ImageField(upload_to='books/cover/',null=True,blank=True)

    # pip install Pillow
    def delete(self,*args,**kwargs):
        self.pdf.delete()
        self.cover.delete()
        super(Book,self).delete(*args,**kwargs)

    def __str__(self):
        return self.title