from ..models import Announces

def update_announce(announce_id, user, data):
    try:
        announce = Announces.objects.get(pk=announce_id, user=user)
    except Announces.DoesNotExist:
        return None, "Anúncio não encontrado ou você não tem permissão."

    for field, value in data.items():
        setattr(announce, field, value)
    announce.save()
    return announce, None