from ..models import Announces

def get_announces_service(filters=None):

    queryset = Announces.objects.all()

    if filters:
        if "type" in filters:
            queryset = queryset.filter(type=filters["type"])
        if "title" in filters:
            queryset = queryset.filter(title__icontains=filters["title"])
        if "conservation_status" in filters:
            queryset = queryset.filter(conservation_status=filters["conservation_status"])

    return queryset