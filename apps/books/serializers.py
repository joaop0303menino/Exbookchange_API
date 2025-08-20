from rest_framework import serializers
from .models import Announces, ConservationStatus, EnumExchangeDonation
from apps.users.models import User


class AnnounceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    author_id = serializers.IntegerField(required=False, allow_null=True, write_only=True)
    conservation_status_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Announces
        fields = [
            "id",
            "title",
            "description",
            "type",
            "user",
            "author_id",
            "conservation_status_id",
            "posted_at",
        ]
        read_only_fields = ["id", "posted_at"]

    def validate_type(self, value):
        if value not in [EnumExchangeDonation.EXCHANGE, EnumExchangeDonation.DONATION]:
            raise serializers.ValidationError("Tipo inválido. Use 'E' (exchange) ou 'D' (donation).")
        return value

    def validate_conservation_status_id(self, value):
        if not ConservationStatus.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Status de conservação inválido.")
        return value

    def validate_author_id(self, value):
        if value and not User.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Autor inválido.")
        return value