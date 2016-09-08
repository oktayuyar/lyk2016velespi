from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import(
 	login as auth_login,
 	logout as auth_logout
)
from profiles.forms import RegistrationForm,LoginForm


def register(request):
    form=RegistrationForm()

    if request.method=="POST":
        form=RegistrationForm(request.POST)

        if form.is_valid(): # valid formdaki veriler geçerli mi dolumu
            form.save()

            messages.info(
                request,
                "Kayıt başarılı. Şimdi login olabilirsiniz"
            )
            return redirect("login")

    return render(request,"register.html",{
        "form" : form
    })


def login(request):
    form= LoginForm()

    if request.method=="POST":
        form =LoginForm(request.POST)

        if form.is_valid():
            auth_login(request, form.user)
            messages.info(
                request,
                "Giriş Yaptınız."
            )
            if request.GET.get("next"):
                return redirect(request.GET["next"])
            else:
                return  redirect("index")



    return render(request,"login.html",{
        "form" :form
    })



def logout(request):
    auth_logout(request)
    return redirect("/")

