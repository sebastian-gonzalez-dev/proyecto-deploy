from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import FormularioCrearTarea
from .models import Task
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required




# Create your views here.

def Home(request):
    return render(request, 'home.html', {'pagina_actual': 'home'})


def Signup(request):
   

    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm, 'pagina_actual':'signup'})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], request.POST['password1'])
                user.save()
                login(request, user)
                return render(request, 'tasks.html', {'pagina_actual':'tasks'})
            except:
                return render(request, 'signup.html', {'mensaje':'Usuario ya existe', 'form': UserCreationForm, 'pagina_actual':'signup'})    
            
        return render(request, 'signup.html', {'mensaje':'Contraseñas no coinciden', 'form': UserCreationForm,'pagina_actual':'signup'})
        
@login_required
def Tasks(request):
    tareas = Task.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request,'tasks.html', {'pagina_actual':'tasks', 'tareas': tareas})


@login_required
def Signout(request):
    logout(request)
    return render(request, 'home.html', {'pagina_actual':'home'})
  

# def Signin(request):
#     if request.method == 'GET':
#         return render(request, 'signin.html', {'pagina_actual':'signin', 'form': AuthenticationForm})
#     else:
#         user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
#         if user is None:
#             return redirect('tasks')
#             # return render(request, 'signin.html', {'pagina_actual':'signin', 'form': AuthenticationForm})
#         else:
#             login(request, user)
#             return render(request, 'tasks.html', {'pagina_actual':'signin', 'form': AuthenticationForm})

        

def Signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('tasks')
        else:
            # Manejar el caso de autenticación fallida
            return render(request, 'signin.html', {'pagina_actual': 'signin', 'form': AuthenticationForm, 'error': 'Autenticación fallida'})
    else:
        return render(request, 'signin.html', {'pagina_actual': 'signin', 'form': AuthenticationForm})

@login_required
def CreateTask(request):
    if request.method == 'GET':
        return render(request, 'create_tasks.html', {'form': FormularioCrearTarea})
    else:
        form = FormularioCrearTarea(request.POST)
        if (form.is_valid()):
            task = form.save(commit=False)  # No guarda en la base de datos aún
            task.user = request.user  # Asocia la tarea con el usuario actual
            task.save()  # Ahora guarda en la base de datos con el usuario asociado

            # print(request.POST)
            # print(request.POST['title'], request.POST['description'], request.POST['important'])
            return redirect('tasks')
        
@login_required
def ListTasks(request):
    tareas = Task.objects.filter(user=request.user, important=True)
    data = {'tareas': tareas}
    return render(request, 'listTasks.html', data)
        

@login_required
def TaskDetail(request, id):
   
        if request.method == 'GET':
            task = get_object_or_404(Task, pk=id )    
            form = FormularioCrearTarea(instance=task)
            return render(request, 'task_detail.html', {'form':form, 'task':task})
        else:
            try:
                task = get_object_or_404(Task, pk=id)
                form = FormularioCrearTarea(request.POST, instance=task)
                form.save()
                return redirect('tasks')
            except:
              
                return render(request, 'task_detail.html', {'form': form,'task':task} )

 
@login_required
def CompletedTask(request, id):
    task = get_object_or_404(Task, pk=id, user= request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')


@login_required
def DeleteTask(request, id):
    task = get_object_or_404(Task, pk=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')


@login_required
def TaskCompleted(request):
    tareas = Task.objects.filter(user=request.user, datecompleted__isnull=False)
    return render(request, 'tasks.html', {'tareas': tareas})