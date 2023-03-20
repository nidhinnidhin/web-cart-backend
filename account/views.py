from rest_framework import generics,permissions
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .serializers import RegisterSerializer,AccountEditSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from .models import ForgetPasswordOTP, Profile
from datetime import datetime
import time
import random
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

class Register(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    permission_classes = [permissions.AllowAny]

class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AccountEditView(APIView):
    def put(self,request):
        user = self.request.user
        print(request.data)
        user.username = request.data["username"]
        user.first_name = request.data["firstname"]
        user.last_name = request.data["lastname"]
        user.email = request.data["email"]
        user.save()
        print(user.first_name)
    
        print(user)
        return Response({"status": "Success"})
    permission_classes = [permissions.IsAuthenticated]

class AccountDetail(APIView):
    def get(self,request):
        user = self.request.user
        data = {
            "firstname":user.first_name,
            "lastname":user.last_name,
            "username":user.username,
            "email":user.email,
        }
        return Response(data)
    
    permission_classes = [permissions.IsAuthenticated]

class ForgetPasswordGenerateOTP(APIView):
    def post(self, request):
        email = request.data["email"]
        print(email)
        if not User.objects.filter(email = email).exists():
            return Response({"message": "Invalid Email ID."}, status = 400)
        user = User.objects.get(email = email)
        print(user)
        if ForgetPasswordOTP.objects.filter(user = user).exists():
            print("Exists - deleted")
            ForgetPasswordOTP.objects.filter(user = user).delete()
        new_otp = ""
        for i in range(4):
            new_otp += str(random.randint(0,9))
        print(new_otp)
        otp = ForgetPasswordOTP.objects.create(user = user, otp=new_otp, created_on = datetime.now())

        subject = 'OTP to reset password - Web Cart'
        message = f'Hi {user.username}, your OTP is {new_otp} to reset your password.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email, ]
        send_mail( subject, message, email_from, recipient_list )

        print(otp.created_on)
        return Response({"status": "Success"})

class ResetPassword(APIView):
    def post(self, request):
        email = request.data["email"]
        otp = request.data["otp"]
        password1 = request.data["password1"]
        password2 = request.data["password2"]

        user = User.objects.get(email = request.data["email"])

        if password1 != password2:
            return Response({"message": "Password doesn't match."}, status = 400)
        elif not User.objects.filter(email = request.data["email"]).exists():
            return Response({"message": "Invalid Email ID."}, status = 400)
        elif not ForgetPasswordOTP.objects.filter(user = user).exists():
            return Response({"message": "Generate OTP to change password."}, status = 400)

        otp_obj = ForgetPasswordOTP.objects.get(user = user)
        difference = datetime.now() - otp_obj.created_on
        if difference.total_seconds()/60 > 10:
            otp_obj.delete()
            return Response({"message": "OTP expired, generate new to continue."}, status = 400)

        if otp == otp_obj.otp:
            user.set_password(password1)
            user.save()
            otp_obj.delete()
        else:
            return Response({"message": "OTP doesn't match."}, status = 400)

        return Response({"status": "Success"})