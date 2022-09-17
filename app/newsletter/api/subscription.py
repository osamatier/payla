from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from newsletter.services.subscription import confirm as confirm_subscription
from newsletter.services.subscription import start as start_subscription


@permission_classes([IsAuthenticated])
@api_view(["POST"])
def subscribe(request: Request) -> Response:
    start_subscription(request.user.client)
    return Response({}, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
@api_view()
def confirm_user_subscription(request: Request, secret_code) -> Response:
    confirm_subscription(secret_code)
    return Response({}, status=status.HTTP_200_OK)
