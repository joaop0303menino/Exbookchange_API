from apps.transactions.models import ExchangeDonationHistoric
class ExchangeDonationService:
    def __init__(self):
        self.model = ExchangeDonationHistoric

    def create_exchange(self, **data):
        return self.model.objects.create(**data)

    def get_exchange_by_user_receiver(self, user_receiver):
        return self.model.objects.filter(user_receiver=user_receiver).first()