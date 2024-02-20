"""
URL configuration for proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tasks import views as tasks


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", tasks.Home, name="home"),
    path("signup/", tasks.Signup, name="signup"),
    path("tasks/", tasks.Tasks, name="tasks"),
    path('logout/', tasks.Signout , name="logout"),
    path('signin/', tasks.Signin , name="signin"),
    path('create_task/', tasks.CreateTask , name="createTask"),
    path('listasks/', tasks.ListTasks , name="lisTask"),
    path('tasks/<int:id>/', tasks.TaskDetail , name="taskDetail"),
    path('tasks/<int:id>/complete', tasks.CompletedTask, name="CompletedTask"),
    path('tasks/<int:id>/delete', tasks.DeleteTask, name="DeleteTask"),
    path('tasks_completed/', tasks.TaskCompleted, name="taskCompleted"),



]
