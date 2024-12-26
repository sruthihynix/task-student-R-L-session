from django.shortcuts import render,redirect
from app1.models import Student_Info
from django.http import HttpResponse

# to register the student details to the db

def reg_page(request):
    if request.method == 'POST':
# get form data
        name=request.POST.get('name')
                    # request.POST['name']
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
    # print(name)
# check pwd match
        if password1 != password2:
            return HttpResponse("Password do not match")
 # Create a new Student_Info instance
        student_info = Student_Info(
                            s_name=name,
                            username=username,
                            password=password1,
                         )
        student_info.save()
# REDIRECT TO HOME PAGE AFTER REGISTERING
        return redirect('login')
    return render(request,'registration.html',locals()) # Using locals(): This will automatically pass all local variables to the template, including name, username, standard, division, etc.

def home_page(request):
    print(' home')
    if 'my_user' in request.session:
        return render(request,'home.html')
    else:
        return redirect('login')


def login_page(request):
    if request.method == 'POST':
# Extract username and password from the form
        username=request.POST['uname']
        password = request.POST.get('pwd')

# Check if the user exists in the database
        try:
            student = Student_Info.objects.get(username=username)
# Check if the password matches
            if student.password == password:
# Redirect to the home page if valid
                request.session['my_user']=username

                return redirect('home')
            else:
                return HttpResponse("Invalid password. Please try again.")

        except Student_Info.DoesNotExist:
# Display an error message if the username is not found
            return HttpResponse("Invalid username. Please try again.")

    return render(request, 'login.html')

def logout_page(request):
    return redirect('registration')

def show_students(request):
    print("students")
    if 'my_user'  in request.session:
        students = Student_Info.objects.all()
        t=students.count()
        # print(t)
        return render(request,'show.html',{'students':students})
    else:
        return redirect('login')

def log_btn(request):
    return redirect('login')