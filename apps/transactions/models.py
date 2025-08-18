from django.db import models

# Create your models here.


from apps.users.models import User
from apps.books.models import Announces

# Tabela de trocas/doações
class ExchangeDonation(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="exchange_donations")
    id_announce = models.ForeignKey(Announces, on_delete=models.CASCADE, related_name="exchange_donations")
    user_receiver = models.CharField(max_length=150) 

    def __str__(self):
        return f"{self.id_user} -> {self.user_receiver} (Announce: {self.id_announce})"

class ExchangeDonationHistoric(models.Model):
    id_exchangedonation = models.ForeignKey(
        ExchangeDonation, 
        on_delete=models.CASCADE, 
        related_name="historic"
    )
    date_transaction = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Histórico de {self.id_exchangedonation} em {self.date_transaction}"