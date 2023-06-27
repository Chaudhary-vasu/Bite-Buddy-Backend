from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from .serializers import RegisterSerializer
from django.contrib.auth import authenticate

# for login api token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    
    
# Register API
@api_view(["POST"])
def register_api(request):
    serializer = RegisterSerializer(data=request.data)
    # raise_exception=True is done for getting proper exception error when we enter invalid data
    serializer.is_valid(raise_exception=True)

    user = serializer.save()

    # when we create a token we get two things: created and token
    # _, token = AuthToken.objects.create(user)

    return Response(
        {
            "status": status.HTTP_201_CREATED,
            "user_info": serializer.data,
        }
    )

# @api_view(["GET"])
# def get_user_data(request):
#     user = request.user
#     if user.is_authenticated:
#         return Response(
#             {
#                 "status": status.HTTP_200_OK,
#                 "user_info": {
#                     "id": user.id,
#                     "username": user.username,
#                 },
#             }
#         )
#     return Response(
#         {
#             "status": status.HTTP_401_UNAUTHORIZED,
#             "message": "User is not authenticated!",
#         }
#     )

@api_view(['GET'])
def getRoutes(request):
    routes = ["/api/login", "api/login/refresh"]
    return Response(routes)
