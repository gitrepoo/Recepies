from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import csv
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView



def home(request):
    if request.user.is_authenticated:
        return redirect('/receipe/')
    return redirect('/login/')
    

class ReceipeExportAPIView(APIView):
    def get(self, requests):
        response = HttpResponse(content='text/csv')
        response['Content-Disposition'] = 'attachment; filename="recepies.csv"'

        writer = csv.writer(response)

        writer.writerow([
            "ID",
            "Receipe name",
            "Receipe description",

        ])

        for receipe in Recepie.objects.all():
            writer.writerow([
                receipe.id,
                receipe.receipe,
                receipe.receipe_description,
                
            ])
        
        return response



@login_required(login_url='/login/') 
def receipe(request): 
    if request.method == "POST": 
        data = request.POST

        receipe = data.get('receipe')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        Recepie.objects.create(
          user=request.user,
          receipe = receipe,
          receipe_description = receipe_description,
          receipe_image = receipe_image,

    )  
        
        return redirect('/receipe/')
    queryset  = Recepie.objects.all() 

    if request.GET.get('search'):
        queryset = queryset.filter(receipe__icontains = request.GET.get('search'))
    context = {'receipe': queryset}

    return render(request, 'receipe.html', context) 



@login_required(login_url='/login/')
def delete_receipe(request, id):
    del_recepie = get_object_or_404( Recepie, id=id)

    if del_recepie.user != request.user:
        return HttpResponse("Not allowed", status=403)
    
    del_recepie.delete()
    return redirect('/receipe/')



@login_required(login_url='/login/')
def update_receipe(request, id):
    update_rec = get_object_or_404(Recepie, id=id)

    if update_rec.user != request.user:
        return HttpResponse("Not allowed", status=403)

    if request.method == "POST":
        data = request.POST

        update_rec.receipe = data.get('receipe')
        update_rec.receipe_description = data.get('receipe_description')

        if request.FILES.get('receipe_image'):
            update_rec.receipe_image = request.FILES.get('receipe_image')

        update_rec.save()   
        return redirect('/receipe/')

    context = {"receipe": update_rec}
    return render(request, 'update_receipe.html', context)
   

def login_page(request):

    if request.method == "POST":
        username = request.POST.get('username') 
        password = request.POST.get('password')


        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username')
            return redirect('/login/')
        
        user = authenticate(username = username, password=password)

        if user is None:
            messages.error(request, 'Invalid password')
            return redirect('/login/')
        
        else:
            login(request, user) 
            return redirect('/receipe/')
        

    return render (request, "login.html")


def logout_page(request):
    logout(request)
    return redirect('/login/')
    
def register_page(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name') 
        username = request.POST.get('username') 
        password = request.POST.get('password') 

        user = User.objects.filter(username=username)
        if user.exists():
            messages.info(request, 'Username already exist.')
            return redirect('/register/')

        
        user = User.objects.create(
             first_name = first_name, 
             last_name = last_name,
             username = username
        )

        user.set_password(password)
        user.save()

        messages.info(request, 'Your account has been created successfully.You can now log in!') 
        return redirect('/register/')
    
    return render (request, "register.html")  
     