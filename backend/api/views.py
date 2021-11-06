from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from rest_framework.permissions import AllowAny

class CreateCustomUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return HttpResponseRedirect(redirect_to='http://127.0.0.1:5500/success.html')
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
