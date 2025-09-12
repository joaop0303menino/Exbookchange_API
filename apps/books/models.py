from django.db import models
from ..users.models import User

class EnumStatus(models.TextChoices):
    STATUS_1 = '1', 'Status 1'
    STATUS_2 = '2', 'Status 2'
    STATUS_3 = '3', 'Status 3'
    STATUS_4 = '4', 'Status 4'
    STATUS_5 = '5', 'Status 5'


class EnumExchangeDonation(models.TextChoices):
    EXCHANGE = '1', 'Exchange'
    DONATION = '2', 'Donation'


class Author(models.Model):
    full_name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.full_name
    


    def __str__(self):
        return f"{self.get_status_display()} - {self.description_status or ''}"

class Announces(models.Model):
    conservation_status = models.CharField(
        max_length=1,
        choices=EnumStatus.choices,
        default=EnumStatus.STATUS_1
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='announces_created'
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='announces_authored'
    )
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    is_archived = models.BooleanField(default=False)
    type = models.CharField(
        max_length=1,
        choices=EnumExchangeDonation.choices,
        default=EnumExchangeDonation.EXCHANGE
    )
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_type_display()})"

class ImagesBook(models.Model):
    announce = models.ForeignKey(
        Announces, 
        on_delete=models.CASCADE, 
        related_name='images'
    )
    image = models.ImageField(upload_to='announces/')
    is_cover = models.BooleanField(default=False)

    def __str__(self):
        return f"Imagem do anúncio {self.announce.id}"