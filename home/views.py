from django.shortcuts import render,HttpResponse,redirect
from .models import User 
# Create your views here.
def index(request):
    context={
        "variable":"this is some text"
    }
    return render (request, 'index.html',context)

def register(request):
    return render(request, 'register.html',{})

def insertuser(request):
    vuid = request.POST['tuid'];
    vuname = request.POST['tuname'];
    vuemail = request.POST['tuemail'];
    vucotact = request.POST['tucontact'];
    us=User(uid=vuid, uname=vuname, uemail=vuemail, ucontact=vucotact);
    us.save();
    return render(request, 'register.html', {})

def show(request):
    users=User.objects.all()
    return render(request, 'show.html',{'users':users})

def delete(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect('/show')

def update(request,id):
    users=User.objects.get(uid=id)
    return render(request, 'update.html',{'users':users})

def edit(request,id):
    users=User.objects.filter(uid=id).update(uname=request.POST['tuname'],uemail=request.POST['tuemail'],ucontact=request.POST['tucontact'])
    return redirect('/show')