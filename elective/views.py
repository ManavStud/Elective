from django.shortcuts import render
from django.http import HttpResponse
from student.models import student

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        stud_name = request.POST.get('stud_name')
        dept = request.POST.get('dept')
        sem_pass = request.POST.get('sem_pass')
        hon_min = request.POST.get('hon_min')
        kt = request.POST.get('kt')
        admit_year = request.POST.get('admit_year')
        opt_course = request.POST.get('opt_course')
        gpa = request.POST.get('gpa')

        # Create a new instance of your model with the submitted data
        new_object = student(
            roll_no=roll_no,
            stud_name=stud_name,
            dept=dept,
            sem_pass=sem_pass,
            hon_min=hon_min,
            kt=kt,
            admit_year=admit_year,
            opt_course=opt_course,
            gpa=gpa
        )

        # Save the new object to the database
        new_object.save()

        # Redirect to a success page
        return render(request, 'index.html')

    # Render the form template if this is a GET request
    return render(request, 'register.html')