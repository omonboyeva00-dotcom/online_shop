from django.core.mail import send_mail
from django.shortcuts import render, redirect

# Create your views here.
from django.views import  View
from django.contrib.auth import authenticate,login,logout
from django.conf import settings

from .utils import generate_code
from . models import CustomerUser,EmailCode
from django.utils import timezone





class RegisterView(View):
    def get(self,request):
        return render(request,'auth/register.html')

    def post(self,request):
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password= request.POST['confirm_password']

        if CustomerUser.objects.filter(username=username).exists():
            return render(request,'auth/register.html',{
                "error":"bu username band"
            })

        if password!=confirm_password:
            return render(request,'auth/register.html',{
                "error":"parollar mos emas"
            })

        user= CustomerUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_active=False
        )

        code=generate_code()

        send_mail(
            "tasdiqlash kodi",
            f"sizning tasdiqlash kodingiz {code}.",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        EmailCode.objects.create(user=user, code=code)

        request.session['user_id'] = user.id

        return redirect('verify_email')

class Verify_EmailView(View):
    def get(self, request):
        return render(request, 'auth/verify_email.html')

    def post(self, request):
        code = request.POST.get('code')
        user_id = request.session.get('user_id')

        if not user_id:
            return redirect('register')

        user = CustomerUser.objects.get(id=user_id)

        otp = EmailCode.objects.filter(
            user=user,
            code=code,
            is_activated=False
        ).last()

        if not otp:
            return render(request, 'auth/verify_email.html', {
                "error": "Kod noto‘g‘ri yoki allaqachon ishlatilgan"
            })

        otp.is_activated = True
        otp.activated_at = timezone.now()
        otp.save()

        return redirect('set_new_password')



class SetNewPasswordView(View):
    def get(self, request):
        if not request.session.get('user_id'):
            return redirect('login')

        return render(request, 'auth/set_new_password.html')

    def post(self, request):
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login')

        if password != confirm_password:
            return render(request, 'auth/set_new_password.html', {
                "error": "Parollar mos emas"
            })

        user = CustomerUser.objects.get(id=user_id)
        user.set_password(password)
        user.is_active = True
        user.save()


        del request.session['user_id']

        return redirect('login')


class LoginView(View):
    def get(self,request):
        return render(request,'auth/login.html')

    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user is None:
            return render(request,'auth/login.html',{
                "error":"username yoki password xato kiritilgan"
            })
        login(request,user)
        return redirect('index')


def logout_(request):
    logout(request)
    return redirect('login')



