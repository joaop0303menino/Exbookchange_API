from rest_framework import serializers
from .models import Announces, EnumExchangeDonation, EnumStatus, ImagesBook
from apps.users.models import User

class ImagesBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesBook
        fields = ['id', 'announce', 'image', 'is_cover']
        
class AnnounceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    author_full_name = serializers.CharField( write_only=True)
    conservation_status = serializers.CharField(write_only=True)
    images = ImagesBookSerializer(many=True, read_only=True)  

    class Meta:
        model = Announces
        fields = [
            "id",
            "title",
            "description",
            "type",
            "user",
            "author_full_name",
            "conservation_status",
            "images",
            "posted_at",
        ]
        read_only_fields = ["id", "posted_at"]

    def validate_type(self, value):
        if value not in [EnumExchangeDonation.EXCHANGE, EnumExchangeDonation.DONATION]:
            raise serializers.ValidationError("Tipo inválido. Use '1' (Exchange) ou '2' (Donation).")
        return value

    def validate_conservation_status(self, value):
        if value not in EnumStatus.values:
            raise serializers.ValidationError("Status de conservação inválido.")
        return value

    def validate_author_id(self, value):
        if value and not User.objects.filter(pk=value).exists():
            raise serializers.ValidationError("Autor inválido.")
        return value