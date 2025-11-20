from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from django.http import JsonResponse

from apps.books.models import Announces
from apps.books.serializers import AnnounceSerializer


class TestAnnounceView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        announce_id = request.query_params.get("announce_id")

        if announce_id:
            announce = Announces.objects.filter(id=announce_id).first()

            if announce is None:
                return JsonResponse(
                    {"status": "error", "message": "Announce not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serializer = AnnounceSerializer(announce)
            return JsonResponse(
                {"status": "success", "announce": serializer.data},
                status=200
            )

        announces = Announces.objects.all()

        if not announces.exists():
            return JsonResponse(
                {"status": "error", "message": "No announces found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = AnnounceSerializer(announces, many=True)
        return JsonResponse(
            {"status": "success", "announces": serializer.data},
            status=200
        )

    def post(self, request):
        data = request.data.copy()
        data["user"] = request.user.id

        serializer = AnnounceSerializer(data=data)

        if not serializer.is_valid():
            return JsonResponse(
                {"status": "error", "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        announce = serializer.save()

        return JsonResponse(
            {"status": "success", "announce": AnnounceSerializer(announce).data},
            status=201
        )

    def put(self, request):
        announce_id = request.data.get("announce_id")

        if not announce_id:
            return JsonResponse(
                {"status": "error", "message": "announce_id is required"},
                status=400
            )

        announce = Announces.objects.filter(id=announce_id, user=request.user).first()

        if announce is None:
            return JsonResponse(
                {"status": "error", "message": "Announce not found or not yours"},
                status=404
            )

        serializer = AnnounceSerializer(announce, data=request.data, partial=True)

        if not serializer.is_valid():
            return JsonResponse(
                {"status": "error", "message": serializer.errors},
                status=400
            )

        serializer.save()

        return JsonResponse(
            {"status": "success", "announce": serializer.data},
            status=200
        )

    def delete(self, request):
        announce_id = request.data.get("announce_id")

        if not announce_id:
            return JsonResponse(
                {"status": "error", "message": "announce_id is required"},
                status=400
            )

        announce = Announces.objects.filter(id=announce_id, user=request.user).first()

        if announce is None:
            return JsonResponse(
                {"status": "error", "message": "Announce not found or not yours"},
                status=404
            )

        announce.delete()

        return JsonResponse(
            {"status": "success", "message": "Announce deleted"},
            status=200
        )
