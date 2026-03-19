from django.http import JsonResponse 
from rest_framework import status  
from apps.books.models import Announces, Author

class AnnounceService: 
    def __init__(self): 
        self.announces_model = Announces
        
    def getAnnounces(self):
        Announces = self.announces_model.objects.filter(is_archived=False)
        
        if not Announces.exists():
            return JsonResponse({"status": "error", "message": "No announces found"}, status=status.HTTP_404_NOT_FOUND)
        
        return Announces
        
    def getAnnounceById(self, validated_data):
        announce_id = validated_data.get("announce_id")
        announce = self.announces_model.objects.get(id=announce_id)
            
        if not announce.exists():
            return JsonResponse({"status": "error", "message": "Announce not found"}, status=status.HTTP_404_NOT_FOUND)
        
        return announce
 
    def getAnnounceByProfile(self, validated_data):
        user_id = validated_data.get("user_id")
        announces = self.announces_model.objects.filter(user_id=user_id)
        
        if not announces.exists():
            return JsonResponse({"status": "error", "message": "No announces found for this profile"}, status=status.HTTP_404_NOT_FOUND)
        
        return announces
       
    def create_announce_service(validated_data, request_user):

        conservation_status_value = validated_data["conservation_status"]

        author_full_name = validated_data.pop("author_full_name")
        author, _ = Author.objects.get_or_create(full_name=author_full_name)

        announce = Announces.objects.create(
            title=validated_data["title"],
            description=validated_data.get("description", ""),
            type=validated_data["type"],
            conservation_status=conservation_status_value, 
            user=request_user,
            author=author,
        )
        return announce

    
    def update_announce(announce_id, user, data):
        announce = Announces.objects.get(pk=announce_id, user=user)
        
        if not announce.exists():
            return None, JsonResponse({"status": "error", "message": "Announce not found"}, status=status.HTTP_404_NOT_FOUND)

        for field, value in data.items():
            setattr(announce, field, value)
        announce.save()
        return announce, None
    
    def delete_announce(announce_id, user):
        announce = 1 