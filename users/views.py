from django.shortcuts import render, redirect
from source import settings
from courses.views import course
from courses.models import Course
from courses.forms import *
from .forms import *
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password


def home(request):
    title = 'eLearning'
    context = {
        "title": title,
    }

    return render(request, "home.html", context)


def profile(request):
    title = 'Profile'
    add_course_form = AddCourseForm(request.POST or None)
    add_user_form = AddUser(request.POST or None)
    delete_user_form = DeleteUser(request.POST or None)
    queryset = User.objects.all()

    context = {
        "title": title,
        "form": add_course_form,
        "form2": add_user_form,
        "form3": delete_user_form,
        "queryset": queryset,
    }

    if add_user_form.is_valid():
        instance = add_user_form.save(commit=False)
        passwd = add_user_form.cleaned_data.get("password")
        instance.password = make_password(password=passwd,
                                          salt='salt', )
        instance.save()
        return HttpResponseRedirect('/profile')

    if delete_user_form.is_valid():
        instance = delete_user_form.save(commit=False)
        delete_user_name = delete_user_form.cleaned_data.get("username")

        try:
            User.objects.get(username=delete_user_name).delete()
        except User.DoesNotExist:
            pass

        return HttpResponseRedirect('/profile')

    if add_course_form.is_valid():
        instance = add_course_form.save(commit=False)
        instance.course_link = '/courses/' + instance.course_name
        instance.save()
        return course(request, course_name=instance.course_name)

    if request.user.is_authenticated():
        if request.user.is_staff and not request.user.is_superuser:
            queryset = Course.objects.all()
            context = {
                "queryset": queryset,
                "form": add_course_form
            }
            return render(request, "professor_dashboard.html", context)
        elif request.user.is_superuser:
            return render(request, "sysadmin_dashboard.html", context)
        else:
            return render(request, "student_dashboard.html", context)
    else:
        return redirect(settings.LOGIN_URL)


def update_profile(request, username):
    if request.user.is_superuser:
        user = User.objects.get(username=username)

        data_dict = {'username': user.username, 'email': user.email}
        update_user_form = EditUser(initial=data_dict, instance=user)
        title = 'Edit user'
        context = {
            "title": title,
            "update_user_form": update_user_form,
        }

        if request.POST:
            user_form = EditUser(request.POST, instance=user)

            if user_form.is_valid():
                instance = user_form.save(commit=False)
                passwd = user_form.cleaned_data.get("password")
                instance.password = make_password(password=passwd,
                                                  salt='salt', )
                instance.save()

                return redirect('/profile/')

        return render(request, "edit_user.html", context)
