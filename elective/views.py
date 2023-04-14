from django.shortcuts import render
from django.http import HttpResponse
from student.models import student
from django.conf import settings
from subject.models import subject,Exposure_Courses
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

    
    
    compulsory_list = subject.objects.filter(sem=1,type='N').values_list('sub_name',flat=True)
    compulsory_sem1 = list(compulsory_list)
    print("Sem1: = ",compulsory_sem1)
    
    compulsory_list = subject.objects.filter(sem=2,type='N').values_list('sub_name',flat=True)
    compulsory_sem2 = list(compulsory_list)
    print("Sem2: = ",compulsory_sem2)
    
    compulsory_list = subject.objects.filter(sem=3,type='N').values_list('sub_name',flat=True)
    compulsory_sem3 = list(compulsory_list)
    print("Sem3: = ",compulsory_sem3)
    
    compulsory_list = subject.objects.filter(sem=4,type='N').values_list('sub_name',flat=True)
    compulsory_sem4 = list(compulsory_list)
    print("Sem4: = ",compulsory_sem4)
    
    compulsory_list = subject.objects.filter(sem=5,type='N').values_list('sub_name',flat=True)
    compulsory_sem5 = list(compulsory_list)
    print("Sem5: = ",compulsory_sem5)
    
    compulsory_list = subject.objects.filter(sem=6,type='N').values_list('sub_name',flat=True)
    compulsory_sem6 = list(compulsory_list)
    print("Sem6: = ",compulsory_sem6)
    
    compulsory_list = subject.objects.filter(sem=7,type='N').values_list('sub_name',flat=True)
    compulsory_sem7 = list(compulsory_list)
    print("Sem7: = ",compulsory_sem7)
    
    compulsory_list = subject.objects.filter(sem=8,type='N').values_list('sub_name',flat=True)
    compulsory_sem8 = list(compulsory_list)
    print("Sem8: = ",compulsory_sem8)
    name_str = student.objects.filter(roll_no=16010121813).values('stud_name')
    name = name_str[0]['stud_name']
    print("Name = ",name)
    
    dept_str = student.objects.filter(roll_no=16010121813).values('dept')
    dept = dept_str[0]['dept']
    print("Department = ",dept)


    subjects = subject.objects.filter(sem=5,type='DE').values('sub_id','sub_name')
    s5e = [subject['sub_name'] for subject in subjects]
    students = student.objects.filter(roll_no=16010121813).values('opt_course')
    opt_courses = students[0]['opt_course'].split(',')
    opt_courses_flat = [course.strip() for course in opt_courses]
    sem5_elective = ""
    for s1 in opt_courses_flat:
        for s2 in s5e:
            if(s1 == s2):
                sem5_elective = s1
                break
    print("Sem5 Elective = ",sem5_elective)
    
    
    subjects = subject.objects.filter(sem=6,type='DE').values('sub_id','sub_name')
    s5e = [subject['sub_name'] for subject in subjects]
    sem6_elective = ""
    for s1 in opt_courses_flat:
        for s2 in s5e:
            if(s1 == s2):
                sem6_elective = s1
                break
    print("Sem6 Elective = ",sem6_elective)
    
    subjects = subject.objects.filter(sem=7,type='DE').values('sub_id','sub_name')
    s5e = [subject['sub_name'] for subject in subjects]
    sem7_elective = []
    for s1 in opt_courses_flat:
        for s2 in s5e:
            if(s1 == s2):
                sem7_elective.append(s1)
    print("Sem7 Elective = ",sem7_elective)
    
    subjects = subject.objects.filter(sem=8,type='DE').values('sub_id','sub_name')
    s5e = [subject['sub_name'] for subject in subjects]
    sem8_elective = []
    for s1 in opt_courses_flat:
        for s2 in s5e:
            if(s1 == s2):
                sem8_elective.append(s1)
    print("Sem8 Elective = ",sem8_elective)
    
    exp1 = Exposure_Courses.objects.filter(sem=1).values_list('course_name',flat=True)
    exposure1 = list(exp1)
    #print(exposure1)
    for s1 in opt_courses_flat:
        for s2 in exposure1:
            if(s1 == s2):
                exp1 = s1
                break
    print("Sem1 Exposure Course = ",exp1)
    
    exp2 = Exposure_Courses.objects.filter(sem=2).values_list('course_name',flat=True)
    exposure2 = list(exp2)
    #print(exposure2)
    for s1 in opt_courses_flat:
        for s2 in exposure2:
            if(s1 == s2):
                exp2 = s1
                break
    print("Sem2 Exposure Course = ",exp2)
    
    unique_entries = list(student.objects.values_list('hon_min', flat=True).distinct())
    print(unique_entries)
    
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