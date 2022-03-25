from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from core.decorators import unauthenticated_user
from core.forms import ImageForm
from core.models import *
from core.functions import *


# Create your views here.

@unauthenticated_user
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('core:dashboard')
        else:
            # return ilvalid login page
            messages.error(request,'Tu dirección electrónica/contraseña no son válidas, o tu cuenta está desactivada.')
    
    return render(request, 'core/login.html')


def LogoutPage(request):
    logout(request)
    return redirect('core:loginpage')

@login_required()
def DashBoard(request):
    images = request.user.imagebank_set.select_related('user')
    categories = ImageCategory.objects.all().order_by('description')

    for x in  images:
        print(x.image.url)

    if not images:
        msg='No tienes imagenes cargardas'
    else:
        msg=''


    context={
        'images':images,
        'categories':categories,
        'msg':msg,

    }

    return render(request, 'core/dashboard.html', context)


def AddImage(request):
    form = ImageForm()
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.POST)
            image = form.save(commit=False)
            image.user = request.user
            # I sav before in order to get the img.pk
            image.save()
            
            # to save a respective categories into the m2m relation
            # I build the getImateCategories function, taht return a list
            # and I used the * to  expand that list into arguments :)
            image.categories.add(*getImageCategories(request.POST))
          
            messages.success(
                request, ":) La imagen se ha guardado correctamente...!")
        else:
            messages.error(request, ":( Algo salio mal, intenta de nuevo..!")
        return redirect('core:dashboard')
    context = {
        'form': form,
        'add' : True,
    }
    
    return render(request, 'core/crud_image.html', context)

def EditImage(request, pk):
    image = ImageBank.objects.get(pk=pk)
    img_selected = image.categories.all().order_by('description')
    img_to_select = ImageCategory.objects.exclude(id__in = img_selected) 
   
      
    form = ImageForm(instance=image)

    if request.method == "POST" :
        form = ImageForm(request.POST, request.FILES, instance=image)
      
        if form.is_valid():
            form.save()
            if request.FILES:
                messages.success(
                request, ":) El registro se ha actualizado con el nuevo fichero")

            messages.success(
                request, ":) La imagen se ha guardado correctamente...!")
        
            return redirect('core:dashboard')

    context = {
        'form'              :form,
        'image'             :image,
        'edit'              :True,
        'img_to_select'     :img_to_select,
        'img_selected'      :img_selected,
        
    }
    return render(request, 'core/crud_image.html', context)

def DeleteImage(request, pk):
    image = ImageBank.objects.get(pk=pk)
    img_selected = image.categories.all().order_by('description')
    
    form = ImageForm(instance=image)
    
    if request.method == "POST" :
        image.delete()
        
        
        return redirect('core:dashboard')

    context = {
        'form'              :form,
        'image'             :image,
        'delete'            :True,
        'img_selected'      :img_selected,
        
    }
    return render(request, 'core/crud_image.html', context)
   





