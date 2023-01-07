from email import message
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.utils import timezone






def index(request):
    due_date = timezone.datetime.now()
    due_assignments = Lecturer.objects.filter(due__lt = due_date).delete()
    return render(request, 'index.html')






@login_required(login_url = 'signin')
def assignment(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        datetime = request.POST["datetime"]
        attachment = request.FILES['attachment']
        course_code = request.user.course_code
        user = request.user

        courses =Lecturer.objects.create(
            title = title,
            description = description,
            due = datetime,
            course_code = course_code,
            attachment = attachment,
            user = user
        
        )
        courses.save()
        messages.success(request, "Assignment Uploaded Successfully!!!")
        
    due_date = timezone.datetime.now()
    due_assignments = Lecturer.objects.filter(due__lt = due_date).delete()

    return render(request, 'upload-a-question.html')





def view_answers(request):

    submission = Student.objects.filter(course_code = request.user.course_code)
    questions = Lecturer.objects.filter(user = request.user)

    context = {
            "submission": submission,
            "questions": questions
        }

    due_date = timezone.datetime.now()
    due_assignments = Lecturer.objects.filter(due__lt = due_date).delete()
    
    
    
    time_delete_answer = timezone.now()- timezone.timedelta(days=30)
    delete_answer = Student.objects.filter(date_created__lt = time_delete_answer).delete()
    
    return render(request, 'view-answers.html', context)





@login_required(login_url = 'signin')
def dashboard(request):

    # ASSIGNMENTS POSTED BY LECTURER
    assignment = Lecturer.objects.all()

    # ASSIGNMENTS SUBMITTED BY STUDENTS
    submit = Student.objects.all()

    context = {
        "assignment": assignment,
        "submit": submit,
    }
    
    due_date = timezone.datetime.now()
    due_assignments = Lecturer.objects.filter(due__lt = due_date).delete()
    return render(request, "dashboard.html", context)





@login_required(login_url = 'signin')
def submit(request, pk):

    assignment = Lecturer.objects.get(id = pk)
    if request.method == "POST":
        answer = request.POST['answer']
        attachment = request.FILES['attachment']
        mat_no = request.user.mat_no
        name = request.user.first_name + ' ' + request.user.last_name
        course_code = assignment.course_code
        assignment_title = request.POST['assign_title']

        submit = Student.objects.create(
            user = request.user,
            answer = answer,
            mat_no = mat_no,
            name = name,
            course_code = course_code,
            assignment = assignment,
            attachment = attachment,
            assign_title = assignment_title
        )
        submit.save()
        messages.success(request, "Assignment Submitted Successfully!!!")


    submission = Student.objects.filter( user = request.user).filter(assignment = assignment.id)


    context = {
            "assignment": assignment,
            "submission": submission
        }
    due_date = timezone.datetime.now()
    due_assignments = Lecturer.objects.filter(due__lt = due_date).delete()
    return render(request, "student-answer.html", context)





@login_required(login_url = 'signin')
def mark_answers(request, pk):

    answers = Student.objects.get(id = pk)
    questions = Lecturer.objects.filter(user = request.user)
    list = Lecturer.objects.filter(id = pk)
    if request.method == "POST":
        score = request.POST['mark']
    
        score = Student.objects.filter(id = pk).update(score = score)
        messages.success(request, "Score Has Been Added Successfully!!!")

  
    context = {
        "answers": answers,
        "list": list,
        "questions": questions,

    }
    
    due_date = timezone.datetime.now()
    due_assignments = Lecturer.objects.filter(due__lt = due_date).delete()

    return render(request, "open-answer.html", context)






@login_required(login_url = 'signin')
def view_assignments(request):
    assignments = Lecturer.objects.filter(user = request.user)
    context = {
        "assignments": assignments
    }

    due_date = timezone.datetime.now()
    due_assignments = Lecturer.objects.filter(due__lt = due_date).delete()
    
    return render(request, "assignments.html", context)






@login_required(login_url = 'signin')
def delete_assignments(request, pk):
    assignments = Lecturer.objects.get(id = pk)
    assignments.delete()
    return redirect("view_assignments")







def register(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            username = request.POST['username']
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            status = request.POST['status']
            mat_no = request.POST['mat']
            course_code = request.POST['course']
            password = request.POST['password']

            if CustomUser.objects.filter(username = username).exists():
                messages.error(request,"Username Taken")

            elif CustomUser.objects.filter(email= email).exists():
                messages.error(request,"Email Already Exists")

            elif CustomUser.objects.filter(mat_no=mat_no).exists():
                messages.error(request,"Mat No Already Exists")

            elif CustomUser.objects.filter(course_code = course_code).exists():
                messages.error(request,"Course Already Registered")
            
            else:
                user = CustomUser.objects.create_user(username, email, password)
                user.first_name = fname
                user.last_name = lname
                user.course_code = course_code
                user.mat_no = mat_no
                user.status = status
                user.save()
                return redirect('signin')
     

        return render(request, 'register.html')
    else:
        return redirect('dashboard')








def signin(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            username = request.POST["Username"]
            password = request.POST["password"]
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid Credentials")
                return redirect('signin')
        return render(request, 'signin.html')
    else:
        return redirect('dashboard')

        

@login_required(login_url = 'signin')
def profile(request):
    return render(request, 'profile.html')





def signout(request):
    logout(request)
    return redirect('signin')







