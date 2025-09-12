from django.db import models
from apps.users.models import User
from apps.books.models import Announces

class ExchangeDonationHistoric(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="exchange_donations")
    id_announce = models.ForeignKey(
            Announces,
            on_delete=models.CASCADE,
            null=True,   
            blank=True
         )
    user_receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    date_transaction = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id_user} -> {self.user_receiver} (Announce: {self.id_announce})"
