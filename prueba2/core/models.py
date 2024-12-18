from django.db import models
# Create your models here.
class Usuario(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Para usar un hash seguro
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Libro(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    book = models.ForeignKey(Libro, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.book} ({self.rating})"