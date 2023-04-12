from django.shortcuts import render
from django.http import HttpResponse
from student.models import student
from django.conf import settings
from subject.models import subject

def login(request):
    context={
        'google_client_id': settings.GOOGLE_CLIENT_ID,
        'google_client_secret': settings.GOOGLE_CLIENT_SECRET
    }
    return render(request,'login.html',context)

def nav(request):
    return render(request, 'nav.html')

def index(request):
    my_list = ['AI', 'ML', 'DSIP','IS','CC']
    context = {'my_list': my_list}
    return render(request, 'index.html', context)

def sem2(request):
    my_list = ['AI', 'ML', 'DSIP','IS','CC']
    context = {'my_list': my_list}
    return render(request, 'sem2.html', context)


def sem3(request):
    my_list = ['AI', 'ML', 'DSIP','IS','CC']
    context = {'my_list': my_list}
    return render(request, 'sem3.html', context)

def sem4(request):
    my_list = ['AI', 'ML', 'DSIP','IS','CC']
    context = {'my_list': my_list}
    return render(request, 'sem4.html', context)

def sem5(request):
    my_list = ['AI', 'ML', 'DSIP','IS','CC']
    context = {'my_list': my_list}
    return render(request, 'sem5.html', context)

def sem6(request):
    my_list = ['AI', 'ML', 'DSIP','IS','CC']
    context = {'my_list': my_list}
    return render(request, 'sem6.html', context)

def sem7(request):
    my_list = ['AI', 'ML', 'DSIP','IS','CC']
    context = {'my_list': my_list}
    return render(request, 'sem7.html', context)

def sem8(request):
    my_list = ['AI', 'ML', 'DSIP','IS','CC']
    context = {'my_list': my_list}
    return render(request, 'sem8.html', context)

def card(request):
    return render(request, 'card.html')

def importt(request):
    return render(request, 'import.html')

def course_selection(request):
    return render(request, 'course_selection.html')

def faculty_dashboard(request):
    return render(request, 'faculty_dashboard.html')



def register(request):
    subjects = subject.objects.filter(sem=5).values('sub_id','sub_name')
    students = student.objects.filter(roll_no=16010121819).values('opt_course')
    electives = []
    for stud in students:
        #print(stud)
        electives.append(stud['opt_course'])

    sem5_elective = ""

    split_list = [s.split(', ') for s in electives]
    #print(electives)
    for elective in electives:
        separate_strings = elective.split(', ')
    print(separate_strings)
    for subjectx in subjects:
        for opt in separate_strings:
            if subjectx['sub_name'] == opt:
                sem5_elective = opt
    #print(students)
    #print(split_list)
    print("Sem5 = ",sem5_elective)
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