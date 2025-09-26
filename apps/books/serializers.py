from rest_framework import serializers
from .models import Announces, EnumExchangeDonation, EnumStatus, ImagesBook
from apps.books.models import Author


class ImagesBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesBook
        fields = ['id', 'announce', 'image', 'is_cover']


class AnnounceSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    author_full_name = serializers.CharField(write_only=True)
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

    def create(self, validated_data):
        author_name = validated_data.pop("author_full_name")

        if validated_data.get("type") not in [
            EnumExchangeDonation.EXCHANGE,
            EnumExchangeDonation.DONATION
        ]:
            raise serializers.ValidationError({
                "type": "Tipo inválido. Use '1' (Exchange) ou '2' (Donation)."
            })

        if validated_data.get("conservation_status") not in EnumStatus.values:
            raise serializers.ValidationError({
                "conservation_status": "Status de conservação inválido."
            })

        author, _ = Author.objects.get_or_create(full_name=author_name)
        announce = Announces.objects.create(author=author, **validated_data)
        return announce

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.type = validated_data.get('type', instance.type)
        instance.conservation_status = validated_data.get('conservation_status', instance.conservation_status)
        
        author_name = validated_data.get("author_full_name")
        if author_name:
            author, _ = Author.objects.get_or_create(full_name=author_name)
            instance.author = author

        instance.save()
        return instance