#from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from DB.models import student,subject,honorminor,exposure_courses,faculty,preference
from django.conf import settings
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
from django import template


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request,'login.html')

def nav(request):
    return render(request, 'nav.html')

def index(request):
    if request.user.is_authenticated:
        # Check if user's email is in the faculty table
        if faculty.objects.filter(fac_email=request.user.email).exists():
            # Redirect user to faculty_dashboard page
            return redirect('faculty_dashboard')
        else:
            return redirect('card')
    
    exp1 = exposure_courses.objects.filter(sem=1).values_list('course_name',flat=True)
    exposure1 = list(exp1)
    # for s1 in opt_courses_flat:
    #     for s2 in exposure1:
    #         if(s1 == s2):
    #             exp1 = s1
    #             break
    print("Sem1 Exposure Course = ",exp1)
    compulsory_list = subject.objects.filter(sem=1,type='N').values_list('sub_name',flat=True)
    compulsory_sem1 = list(compulsory_list)
    context = {
        'my_list': exposure1,
        'compulsory_sem1':compulsory_sem1,
        }
    
    roll = request.POST.get('roll')
    pref1 = request.POST.get('pref1')
    pref2 = request.POST.get('pref2')
    pref3 = request.POST.get('pref3')
    pref4 = request.POST.get('pref4')
    pref5 = request.POST.get('pref5')
    pref6 = request.POST.get('pref6')
    pref7 = request.POST.get('pref7')
    pref8 = request.POST.get('pref8')
    gpa = request.POST.get('gpa')
    
    if request.method == "POST":
        P = preference()
        name_str = student.objects.filter(roll_no=16010121003).values()
        P.name = name_str[0]['stud_name']
        P.roll = roll
        P.sem = 1
        P.dept = name_str[0]['dept']
        P.pref1 = pref1
        P.pref2 = pref2
        P.pref3 = pref3
        P.pref4 = pref4
        P.pref5 = pref5
        P.pref6 = pref6
        P.pref7 = pref7
        P.pref8 = pref8
        P.save()
    

    return render(request, 'index.html', context)


def sem2(request):
    email = request.user.email
    print(email)
    
    rollno=student.objects.get(email=email)
    roll_fetch=rollno.roll_no
    print(roll_fetch)


    exp2 = exposure_courses.objects.filter(sem=2).values_list('course_name',flat=True)
    exposure2 = list(exp2)
    compulsory_list = subject.objects.filter(sem=2,type='N').values_list('sub_name',flat=True)
    compulsory_sem2 = list(compulsory_list)
    roll=request.POST.get('roll')
    pref1 = request.POST.get('pref1')
    pref2 = request.POST.get('pref2')
    pref3 = request.POST.get('pref3')
    pref4 = request.POST.get('pref4')
    pref5 = request.POST.get('pref5')
    pref6 = request.POST.get('pref6')
    pref7 = request.POST.get('pref7')
    pref8 = request.POST.get('pref8')
    gpa = request.POST.get('gpa')
    print(roll)
   # print(pref1 + "\n",pref2 + "\n",pref3+ "\n",pref4+ "\n",pref5+ "\n",pref6+ "\n",pref7+ "\n",pref8+ "\n")
    print(gpa)
    if request.method == "POST":
        P = preference()
        name_str = student.objects.filter(roll_no=16010121003).values()
        P.stud_name = "Manav"
        P.roll_no = roll
        P.sem = 2
        P.dept = "COMP"
        P.pref1 = pref1
        P.pref2 = pref2
        P.pref3 = pref3
        P.pref4 = pref4
        P.pref5 = pref5
        P.pref6 = pref6
        P.pref7 = pref7
        P.pref8 = pref8
        P.save()
    # pref1=request.POST.get()
    # try:
    #     preference_obj = preference.objects.get(roll=roll)
    #     print("Preference row already exists for roll number:", roll)
    # except preference.DoesNotExist:
    # # Create a new row with the given roll number and preferences
    #     preference_obj = preference.objects.create(roll=roll, preference=preference)
    #     print("Preference row created for roll number:", roll)
    # preference_list = preference_obj.preference
    # # my_list = ['AI', 'ML', 'DSIP','IS','CC']
    options=['pref1','pref2','pref3','pref4','pref5','pref6','pref7','pref8']
    context = {
        'my_list': exposure2,
        'compulsory_sem2':compulsory_sem2,
        'pref':options,
        }
    return render(request, 'sem2.html', context)


def sem3(request):
    email = request.user.email
    print(email)
    
    try:
        rollno=student.objects.get(email=email)
    except student.DoesNotExist:
        return HttpResponse("You are not authorized to access this page.")
    roll_fetch=rollno.roll_no
    print(roll_fetch)
    #my_list = ['AI', 'ML', 'DSIP','IS','CC']
    
    compulsory_list = subject.objects.filter(sem=3,type='N').values_list('sub_name',flat=True)
    compulsory_sem3 = list(compulsory_list)
    print("Sem3: = ",compulsory_sem3)
    context = {
        #'my_list': my_list,
        'compulsory_sem3':compulsory_sem3
        }
    return render(request, 'sem3.html', context)
    

def sem4(request):
    email = request.user.email
    print(email)
    
    rollno=student.objects.get(email=email)
    roll_fetch=rollno.roll_no
    print(roll_fetch)

    compulsory_list = subject.objects.filter(sem=4,type='N').values_list('sub_name',flat=True)
    compulsory_sem4 = list(compulsory_list)
    print("Se43: = ",compulsory_sem4)
    context = {
    #   'my_list': my_list,
        'compulsory_sem4':compulsory_sem4
        }
    return render(request, 'sem4.html', context)


def sem5(request):
    email = request.user.email
    print(email)
    
    rollno=student.objects.get(email=email)
    roll_fetch=rollno.roll_no
    print(roll_fetch)

    roll=request.POST.get('roll')
    pref1 = request.POST.get('pref1')
    pref2 = request.POST.get('pref2')
    pref3 = request.POST.get('pref3')
    pref4 = request.POST.get('pref4')
    gpa = request.POST.get('gpa')
    
    if request.method == "POST":
        P = preference()
        P.stud_name = "X"
        P.roll_no = roll
        P.sem = 5
        P.dept = "COMP"
        P.pref1 = pref1
        P.pref2 = pref2
        P.pref3 = pref3
        P.pref4 = pref4
        print(P)
        P.save()
    print(gpa)
    print(roll)
    # print(pref1 + "\n",pref2 + "\n",pref3+ "\n",pref4+ "\n",pref5+ "\n",pref6+ "\n",pref7+ "\n",pref8+ "\n")
    print(gpa)
    try:
        #preference_obj = preference.objects.get(roll=roll)
        print("Preference row already exists for roll number:", roll)
    except preference.DoesNotExist:
    # Create a new row with the given roll number and preferences
        preference_obj = preference.objects.create(roll=roll, preference=preference)
        print("Preference row created for roll number:", roll)
    name_str = student.objects.filter(roll_no=16010121003).values('stud_name')
    name = name_str[0]['stud_name']
    print("Name = ",name)
    dept_str = student.objects.filter(roll_no=16010121003).values('dept')
    dept = dept_str[0]['dept']
    print("Department = ",dept)
    my_list = subject.objects.filter(type='DE',sem=5).values_list('sub_name',flat=True)
    my_list = list(my_list)
    context = {'my_list': my_list}
    compulsory_list = subject.objects.filter(sem=3,type='N').values_list('sub_name',flat=True)
    compulsory_sem5 = list(compulsory_list)
    print("Sem5: = ",compulsory_sem5)
    context = {
        'my_list': my_list,
        'compulsory_sem5':compulsory_sem5
        }
    return render(request, 'sem5.html', context)


def sem6(request):
    email = request.user.email
    print(email)
    
    # try:
    #     rollno=student.objects.get(email=email)
    # except student.DoesNotExist:
    #     return HttpResponse("You are not authorized to access this page.")
    #roll_fetch=rollno.roll_no
    #print(roll_fetch)
    
    name_str = student.objects.filter(roll_no=16010121003).values('stud_name')
    name = name_str[0]['stud_name']
    print("Name = ",name)

    dept_str = student.objects.filter(roll_no=16010121003).values('dept')
    dept = dept_str[0]['dept']
    print("Department = ",dept)

    my_list = subject.objects.filter(type='DE',sem=6).values_list('sub_name',flat=True)
    my_list = list(my_list)    
    compulsory_list = subject.objects.filter(sem=3,type='N').values_list('sub_name',flat=True)
    compulsory_sem6 = list(compulsory_list)
    print("Sem6: = ",compulsory_sem6)
    context = {
        'my_list': my_list,
        'compulsory_sem6':compulsory_sem6
        }
    roll=request.POST.get('roll')
    pref1 = request.POST.get('pref1')
    pref2 = request.POST.get('pref2')
    pref3 = request.POST.get('pref3')
    pref4 = request.POST.get('pref4')
    pref5 = request.POST.get('pref5')
    pref6 = request.POST.get('pref6')
    pref7 = request.POST.get('pref7')
    pref8 = request.POST.get('pref8')
    gpa = request.POST.get('gpa')
    print(roll)
    print(pref1,pref2,pref3,pref4,pref5,pref6,pref7,pref8)
    print(gpa)
    print("pref1 = ",pref1)
    if request.method == "POST":
        P = preference()
        name_str = student.objects.filter(roll_no=16010121003).values()
        # name_str = student.objects.filter(email=var).valueslist(roll,flat=True)
        # roll = name_str[0]['roll']
        P.name = name_str[0]['stud_name']
        P.roll = roll
        P.sem = 2
        P.dept = name_str[0]['dept']
        P.pref1 = pref1
        P.pref2 = pref2
        P.pref3 = pref3
        P.pref4 = pref4
        P.pref5 = pref5
        P.pref6 = pref6
        P.pref7 = pref7
        P.pref8 = pref8
        P.save()
    return render(request, 'sem6.html', context)


def sem7(request):
    email = request.user.email
    print(email)
    
    rollno=student.objects.get(email=email)
    roll_fetch=rollno.roll_no
    print(roll_fetch)
    

    name_str = student.objects.filter(roll_no=16010121003).values('stud_name')
    name = name_str[0]['stud_name']
    print("Name = ",name)
    
    dept_str = student.objects.filter(roll_no=16010121003).values('dept')
    dept = dept_str[0]['dept']
    print("Department = ",dept)
    
    my_list_de3 = subject.objects.filter(type='DE3',sem=7).values_list('sub_name',flat=True)
    my_list_de3 = list(my_list_de3) 
    #print("de3: ",my_list_de3)
    # my_list = ['AI', 'ML', 'DSIP','IS','CC']
    context = {'my_list_de3': my_list_de3}

    
    my_list_de4 = subject.objects.filter(type='DE4',sem=7).values_list('sub_name',flat=True)
    my_list_de4 = list(my_list_de4) 
    #print("de4: ",my_list_de4)
    # my_list = ['AI', 'ML', 'DSIP','IS','CC']
    context = {'my_list_de4': my_list_de4}

    compulsory_list = subject.objects.filter(sem=7,type='N').values_list('sub_name',flat=True)
    compulsory_sem7 = list(compulsory_list)
    #print("Sem7: = ",compulsory_sem7)
    context = {
        'my_list_de3': my_list_de3,
        'my_list_de4': my_list_de4,
        'compulsory_sem7':compulsory_sem7
        }
    if request.method == 'POST':
        roll=request.POST.get('roll')
        pref_de3_1 = request.POST.get('Pref1')
        pref_de3_2 = request.POST.get('Pref2')
        pref_de3_3 = request.POST.get('Pref3')
        pref_de3_4 = request.POST.get('Pref4')
        pref_de3_5 = request.POST.get('Pref5')
        pref_de3_6 = request.POST.get('Pref6')
        pref_de3_7 = request.POST.get('Pref7')

        pref_de4_1 = request.POST.get('pref1')
        pref_de4_2 = request.POST.get('pref2')
        pref_de4_3 = request.POST.get('pref3')
        pref_de4_4 = request.POST.get('pref4')
        pref_de4_5 = request.POST.get('pref5')
        pref_de4_6 = request.POST.get('pref6')

        # pref4 = request.POST.get('pref4')
        # pref5 = request.POST.get('pref5')
        # pref6 = request.POST.get('pref6')
        # pref7 = request.POST.get('pref7')
        # pref8 = request.POST.get('pref8')
        gpa = request.POST.get('gpa')
        print(roll)
        print(pref_de3_1,pref_de3_2,pref_de3_3,pref_de3_4,pref_de3_5,pref_de3_6,pref_de3_7,pref_de3_8)
        print(pref_de4_1,pref_de4_2,pref_de4_3,pref_de4_4,pref_de4_5,pref_de4_6,pref_de4_7,pref_de4_8)
        print(gpa)
        
        
        P = preference()
        name_str = student.objects.filter(roll_no=16010121003).values()
        P.name = name_str[0]['stud_name']
        P.roll = roll
        P.sem = 71
        P.dept = name_str[0]['dept']
        P.pref1 = pref_de3_1
        P.pref2 = pref_de3_2
        P.pref3 = pref_de3_3
        P.pref4 = pref_de3_4
        P.pref5 = pref_de3_5
        P.pref6 = pref_de3_6
        P.pref7 = pref_de3_7

        P.save()
        
        P = preference()
        P.name = name_str[0]['stud_name']
        P.roll = roll
        P.sem = 72
        P.dept = name_str[0]['dept']
        P.pref1 = pref_de4_1
        P.pref2 = pref_de4_2
        P.pref3 = pref_de4_3
        P.pref4 = pref_de4_4
        P.pref5 = pref_de4_5
        P.pref6 = pref_de4_6

        P.save()
    return render(request, 'sem7.html', context)


def sem8(request):
    email = request.user.email
    print(email)
    
    try:
        rollno=student.objects.get(email=email)
    except student.DoesNotExist:
        return HttpResponse("You are not authorized to access this page.")
    roll_fetch=rollno.roll_no
    print(roll_fetch)
    
    name_str = student.objects.filter(roll_no=16010121003).values('stud_name')
    name = name_str[0]['stud_name']
    #print("Name = ",name)
    
    dept_str = student.objects.filter(roll_no=16010121003).values('dept')
    dept = dept_str[0]['dept']
    print("Department = ",dept)

    my_list_de5 = subject.objects.filter(type='DE5',sem=8).values_list('sub_name',flat=True)
    my_list_de5 = list(my_list_de5) 
    print("de5: ",my_list_de5)
    # my_list = ['AI', 'ML', 'DSIP','IS','CC']
    context = {'my_list_de5': my_list_de5}

    #kumbalitrance
   # my_list = ['AI', 'ML', 'DSIP','IS','CC']
   
    my_list_de6 = subject.objects.filter(type='DE6',sem=8).values_list('sub_name',flat=True)
    my_list_de6 = list(my_list_de6) 
    print("de5: ",my_list_de6)
    context = {'my_list_de6': my_list_de6}
    compulsory_list = subject.objects.filter(sem=8,type='N').values_list('sub_name',flat=True)
    compulsory_sem8 = list(compulsory_list)
    print("Sem8: = ",compulsory_sem8)
    context = {
        'my_list_de5': my_list_de5,
        'my_list_de6': my_list_de6,
        'compulsory_sem8':compulsory_sem8
        }
    if request.method == 'POST':
        roll=request.POST.get('roll')
        pref_de3_1 = request.POST.get('Pref1')
        pref_de3_2 = request.POST.get('Pref2')
        pref_de3_3 = request.POST.get('Pref3')
        pref_de3_4 = request.POST.get('Pref4')
        pref_de3_5 = request.POST.get('Pref5')
        pref_de3_6 = request.POST.get('Pref6')


        pref_de4_1 = request.POST.get('pref1')
        pref_de4_2 = request.POST.get('pref2')
        pref_de4_3 = request.POST.get('pref3')
        pref_de4_4 = request.POST.get('pref4')
        pref_de4_5 = request.POST.get('pref5')
        pref_de4_6 = request.POST.get('pref6')
        # pref4 = request.POST.get('pref4')
        # pref5 = request.POST.get('pref5')
        # pref6 = request.POST.get('pref6')
        # pref7 = request.POST.get('pref7')
        # pref8 = request.POST.get('pref8')
        gpa = request.POST.get('gpa')
        print(roll)
        # print(pref_de3_1,pref_de3_2,pref_de3_3,pref_de3_4,pref_de3_5,pref_de3_6,pref_de3_7,pref_de3_8)
        # print(pref_de4_1,pref_de4_2,pref_de4_3,pref_de4_4,pref_de4_5,pref_de4_6,pref_de4_7,pref_de4_8)
        print(gpa)
        
        
        P = preference()
        name_str = student.objects.filter(roll_no=16010121003).values()
        P.name = name_str[0]['stud_name']
        P.roll = roll
        P.sem = 81
        P.dept = name_str[0]['dept']
        P.pref1 = pref_de3_1
        P.pref2 = pref_de3_2
        P.pref3 = pref_de3_3
        P.pref4 = pref_de3_4
        P.pref5 = pref_de3_5
        P.save()
        
        P = preference()
        P.name = name_str[0]['stud_name']
        P.roll = roll
        P.sem = 82
        P.dept = name_str[0]['dept']
        P.pref1 = pref_de4_1
        P.pref2 = pref_de4_2
        P.pref3 = pref_de4_3
        P.pref4 = pref_de4_4
        P.pref5 = pref_de4_5
        P.pref6 = pref_de4_6
        P.save()
        
    return render(request, 'sem8.html', context)



def card(request):
    email = request.user.email
    print(email)
    
    try:
        rollno=student.objects.get(email=email)
    except student.DoesNotExist:
        return HttpResponse("You are not authorized to access this page.")
    roll_fetch=rollno.roll_no
    print(roll_fetch)
    
    name_str = student.objects.filter(roll_no=16010121003).values()
    roll_no = name_str[0]['roll_no']
    name = name_str[0]['stud_name']
    department = name_str[0]['dept']
    sem_pass = name_str[0]['dept']
    honorminor = name_str[0]['hon_min']
    gpa = name_str[0]['gpa']
    compulsory_list = subject.objects.filter(sem=1,type='N').values_list('sub_name',flat=True)
    compulsory_sem1 = list(compulsory_list)
    #print("Sem1: = ",compulsory_sem1)
    
    compulsory_list = subject.objects.filter(sem=2,type='N').values_list('sub_name',flat=True)
    compulsory_sem2 = list(compulsory_list)
    #print("Sem2: = ",compulsory_sem2)
    
    compulsory_list = subject.objects.filter(sem=3,type='N').values_list('sub_name',flat=True)
    compulsory_sem3 = list(compulsory_list)
    #print("Sem3: = ",compulsory_sem3)
    
    compulsory_list = subject.objects.filter(sem=4,type='N').values_list('sub_name',flat=True)
    compulsory_sem4 = list(compulsory_list)
    #print("Sem4: = ",compulsory_sem4)
    
    compulsory_list = subject.objects.filter(sem=5,type='N').values_list('sub_name',flat=True)
    compulsory_sem5 = list(compulsory_list)
    print("Sem5: = ",compulsory_sem5)
    
    compulsory_list = subject.objects.filter(sem=6,type='N').values_list('sub_name',flat=True)
    compulsory_sem6 = list(compulsory_list)
    #print("Sem6: = ",compulsory_sem6)
    
    compulsory_list = subject.objects.filter(sem=7,type='N').values_list('sub_name',flat=True)
    compulsory_sem7 = list(compulsory_list)
    #print("Sem7: = ",compulsory_sem7)
    
    compulsory_list = subject.objects.filter(sem=8,type='N').values_list('sub_name',flat=True)
    compulsory_sem8 = list(compulsory_list)
    #print("Sem8: = ",compulsory_sem8)
    
    # dept_str = student.objects.filter(roll_no=16010121813).values('dept')
    # dept = dept_str[0]['dept']
    # print("Department = ",dept)


    subjects = subject.objects.filter(sem=5,type='DE').values('sub_id','sub_name')
    s5e = [subject['sub_name'] for subject in subjects]
    students = student.objects.filter(roll_no=16010121003).values('opt_course')
    opt_courses = students[0]['opt_course'].split(',')
    opt_courses_flat = [course.strip() for course in opt_courses]
    sem5_elective = ""
    for s1 in opt_courses_flat:
        for s2 in s5e:
            if(s1 == s2):
                sem5_elective = s1
                break
    #print("Sem5 Elective = ",sem5_elective)
    
    
    subjects = subject.objects.filter(sem=6,type='DE').values('sub_id','sub_name')
    s5e = [subject['sub_name'] for subject in subjects]
    sem6_elective = ""
    for s1 in opt_courses_flat:
        for s2 in s5e:
            if(s1 == s2):
                sem6_elective = s1
                break
    #print("Sem6 Elective = ",sem6_elective)
    
    subjects = subject.objects.filter(sem=7,type='DE').values('sub_id','sub_name')
    s5e = [subject['sub_name'] for subject in subjects]
    sem7_elective = []
    for s1 in opt_courses_flat:
        for s2 in s5e:
            if(s1 == s2):
                sem7_elective.append(s1)
    #print("Sem7 Elective = ",sem7_elective)
    
    subjects = subject.objects.filter(sem=8,type='DE').values('sub_id','sub_name')
    s5e = [subject['sub_name'] for subject in subjects]
    sem8_elective = []
    for s1 in opt_courses_flat:
        for s2 in s5e:
            if(s1 == s2):
                sem8_elective.append(s1)
    #print("Sem8 Elective = ",sem8_elective)
    
    exp1 = exposure_courses.objects.filter(sem=1).values_list('course_name',flat=True)
    exposure1 = list(exp1)
    #print(exposure2)
    for s1 in opt_courses_flat:
        for s2 in exposure1:
            if(s1 == s2):
                exp1 = s1
                break
    
    exp2 = exposure_courses.objects.filter(sem=2).values_list('course_name',flat=True)
    exposure2 = list(exp2)
    #print(exposure2)
    for s1 in opt_courses_flat:
        for s2 in exposure2:
            if(s1 == s2):
                exp2 = s1
                break
    #print("Sem2 Exposure Course = ",exp2)
    
    #Student: Name, Department, HonorMinor, Sempass
    #Subjects
    context = {
        "compulsory_sem1": compulsory_sem1,
        "compulsory_sem2": compulsory_sem2,
        "compulsory_sem3": compulsory_sem3,
        "compulsory_sem4": compulsory_sem4,
        "compulsory_sem5": compulsory_sem5,
        "compulsory_sem6": compulsory_sem6,
        "compulsory_sem7": compulsory_sem7,
        "compulsory_sem8": compulsory_sem8,
        "sem5_elective": sem5_elective,
        "sem6_elective": sem6_elective,
        "sem7_elective": sem7_elective,
        "sem8_elective": sem8_elective,
        "exp1": exp1,
        "exp2": exp2, 
        "student_name": name,
        "department": department,
        "roll_no": roll_no ,
        "honorminor": honorminor,
        "sempass": sem_pass,
    }
    print(context)
    return render(request, 'card.html',context)


def importt(request):
    email = request.user.email
    print(email)
    
    try:
        rollno=student.objects.get(email=email)
    except student.DoesNotExist:
        return HttpResponse("You are not authorized to access this page.")
    roll_fetch=rollno.roll_no
    print(roll_fetch)
    return render(request, 'import.html')


def course_selection(request):
    
    stud = preference.objects.values_list('roll',flat=True).distinct()
    stud = list(stud)
    print(stud)
    hon_min = []
    for s in stud:
        distinct_hon_min = student.objects.filter(roll_no=s).values_list('hon_min', flat=True)
        distinct_hon_min = list(distinct_hon_min)
        print(distinct_hon_min)
        if distinct_hon_min[0] not in hon_min:
            hon_min.append(distinct_hon_min[0])
    email = request.user.email
    print(email)
    
    rollno=student.objects.get(email=email)
    roll_fetch=rollno.roll_no
    print(roll_fetch)
    context = {
        'hon_min' : hon_min
    }
    return render(request, 'course_selection.html', context)


def faculty_dashboard(request):
    email = request.user.email
    print(email)
    
    if request.user.is_authenticated:
        # Check if user's email is in the faculty table
        if faculty.objects.filter(fac_email=request.user.email).exists():
            # Display faculty dashboard
            return render(request, 'faculty_dashboard.html')
    return redirect('card')



def register(request):

    email = request.user.email
    print(email)
    
    rollno=student.objects.get(email=email)

    roll_fetch=rollno.roll_no
    print(roll_fetch)
    

    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        stud_name = request.POST.get('stud_name')
        dept = request.POST.get('dept')
        utype = request.POST.get('utype')
        passw = request.POST.get('pass')
        cpassw = request.POST.get('cpass')
        username = request.POST.get('username')
        # admit_year = request.POST.get('admit_year')
        # opt_course = request.POST.get('opt_course')
        # gpa = request.POST.get('gpa')
        
        # Create a new instance of your model with the submitted data
        new_object = student(
            roll_no=roll_no,
            stud_name=stud_name,
            dept=dept,
            utype=utype,
            password=passw,
            cpassw=cpassw,
            username=username
        )
        # Save the new object to the database
        new_object.save()
        # Redirect to a success page
        return render(request, 'index.html')
    # Render the form template if this is a GET request
    return render(request, 'register.html')




def stud_pref(request):
    import random
    import matplotlib.pyplot as plt
    import openpyxl
    from openpyxl.styles import Alignment
    import sys 
    from DB.models import preference
    from DB.models import student,subject
    
    studlist = preference.objects.all().values()
    subjects = subject.objects.filter(sem=6,type='DE').values_list('sub_name',flat=True)
    subjects = list(subjects)
    students = []
    student_data = []
    for stud in studlist:
        preflist = []
        rollno = stud['roll_no']
        print(rollno)
        name = stud['stud_name']
        dept = stud['dept']
        preflist.append(stud['pref1'])
        preflist.append(stud['pref2'])
        preflist.append(stud['pref3'])
        preflist.append(stud['pref4'])
        preflist.append(stud['pref5'])
        preflist.append(stud['pref6'])
        preflist.append(stud['pref7'])
        preflist.append(stud['pref8'])
        ptr = student.objects.filter(roll_no=rollno).values('gpa')
        pointer = ptr[0]['gpa']
        student_data.append([rollno, name, dept, preflist, pointer])
    print(student_data)
    # num_preferences = int(input("Enter the number of preferences for each student: "))

    #print(len(students))
    # # sort students based on pointer value (higher pointer comes first)
    num = int(input("Enter the number of preferences to display: "))
    # count the number of appearances of each preference subject
    preference_subjects_count = {s: 0 for s in subjects}
    for i in range(num):
        preference_subjects = [stud[3][i] for stud in student_data]
        preference_subjects_count = {s: preference_subjects_count[s] + preference_subjects.count(s) for s in subjects}


    subject_preferences_count = {}
    total_appearances = {}
    for s in subjects:
        subject_preferences_count[s] = [0] * num
        total_appearances[s] = 0
    for i in range(num):
        preference_subjects = [stud[3][i] for stud in student_data]
        subject_count = {s: preference_subjects.count(s) for s in subjects}
        for j, (s, count) in enumerate(subject_count.items()):
            subject_preferences_count[s][i] = count
            total_appearances[s] += count
        # fig, ax = plt.subplots()
        # ax.pie(list(subject_count.values()), labels=list(subject_count.keys()), autopct='%1.1f%%', startangle=90)
        # ax.axis('equal')
        # ax.set_title(f"Preference {i+1}")
        # plt.show()
    for s, count in subject_preferences_count.items():
        print(s, count, f"Total Appearances: {total_appearances[s]}")
    # sort subjects based on their total appearances
    sorted_subjects = sorted(total_appearances.items(), key=lambda x: x[1], reverse=True)
    # extract the top `num` subjects
    top_subjects = [s for s, count in sorted_subjects[:num]]
    # extract the count of the top `num` subjects
    top_subjects_count = [total_appearances[s] for s in top_subjects]
    print(f"\nTop {num} subjects by appearances:")
    for i in range(num):
        print(f"{i+1}. {top_subjects[i]}: {top_subjects_count[i]}")
        
    # sort the preferences by their count and extract the top `num` preferences
    sorted_preferences = sorted(preference_subjects_count.items(), key=lambda x: x[1], reverse=True)
    preferences = [preference for preference, count in sorted_preferences[:num]]
    min_batch_size = int(input("Enter minimum batch size: "))
    max_batch_size = int(len(students)) - int((num-1) * min_batch_size); 
    print(max_batch_size)
    # create empty lists for each preference subject
    lists_dict = {}
    for preference in preferences:
        lists_dict[preference] = []
    # iterate over the students and allocate them to their top preference subject
    for student in student_data:
        allocated = False
        for preference in student[2]:
            if preference in preferences and len(lists_dict[preference]) < max_batch_size:
                lists_dict[preference].append(student)
                allocated = True
                break
        if not allocated:
            lists_dict[preferences[0]].append(student)
    # count the number of students in each preference subject list
    subject_student_count = {preference: len(lists_dict[preference]) for preference in preferences}
    # ensure that each preference subject has at least min_batch_size students in it
    for preference in preferences:
        while subject_student_count[preference] < min_batch_size:
            for student in students:
                if preference in student[2] and student not in lists_dict[preference]:
                    lists_dict[preference].append(student)
                    subject_student_count[preference] += 1
                    break
    # print the list of subjects and the students in each subject list
    for preference, students in lists_dict.items():
        print(f"{preference}: {len(students)} students")
        for student in student_data:
            print(f"- {student[0]} ({student[4]})")
    # create a new workbook and select the active worksheet
    import xlsxwriter
    # create a new workbook and add a worksheet
    wb = xlsxwriter.Workbook('D:\Downloads\Excel\student_lists.xlsx')
    sheet = wb.add_worksheet()
    # define the header row and write it to the sheet
    header = ['Total Students', '']
    for subject in lists_dict:
        header.append(f"{subject}")
    sheet.write_row(0, 0, header)
    # define the count row and write it to the sheet
    count_row = [len(students), '']
    for subject in lists_dict:
        count_row.append(len(lists_dict[subject]))
    count_row.append('')
    sheet.write_row(1, 0, count_row)
    # define alignment for the header and count rows
    header_format = wb.add_format({'align': 'center', 'valign': 'vcenter'})
    sheet.set_row(0, None, header_format)
    sheet.set_row(1, None, header_format)
    # add a blank row after the count row
    sheet.merge_range(2, 0, 2, 2, '')
    row_num = 3
    header = ['Roll No','Student Name', 'Department', 'Pointer','Subject','Approved']
    sheet.write_row(row_num, 0, header)
    # iterate over the subjects and write each subject's student list to the sheet
    row_num += 1 # starting row number
    for subject in lists_dict:
        # add a blank row before starting a new subject's list
        if row_num != 3:
            sheet.merge_range(row_num, 0, row_num, 4, '')
            row_num += 1
        # write the subject name to the sheet
        sheet.merge_range(row_num, 0, row_num, 4, subject)
        sheet.write(row_num, 0, subject, header_format)
        row_num += 1
        # write each student's details to the sheet
        for student in lists_dict[subject]:
            rollno,name, department, _, pointer = student
            row_data = [rollno, name, department, pointer, subject]
            sheet.write_row(row_num, 0, row_data)
            row_num += 1
    # adjust column widths and row heights
    # for col in range(num+3):
    #     sheet.set_column(col, col, len(header[col])+2)
    # for row in range(1, row_num):
    #     sheet.set_row(row, 15)
    # close the workbook
    wb.close()
        
        
    # args = sys.argv
    # fake = Faker()

    # department = "Computer"
    # subjects = ["Math", "Physics", "Chemistry", "Computer Science", "Biology", "Geology", "English", "History", "Economics", "Psychology"]
    # pointer_range = (7.0, 10.0)

    # num_preferences = int(input("Enter the number of preferences for each student: "))

    # def generate_student():
    #     name = fake.unique.first_name()
    #     preferences = random.sample(subjects, k=num_preferences)
    #     pointer = round(random.uniform(*pointer_range), 2)
    #     return [name, department, preferences, pointer]

    # # generate a list of 100 students
    # students = [generate_student() for _ in range(100)]
    #print(len(students))
    # sort students based on pointer value (higher pointer comes first)
    # students = sorted(students, key=lambda student: student[3], reverse=True)


    # num = int(input("Enter the number of preferences to display: "))

    # # count the number of appearances of each preference subject
    # preference_subjects_count = {subject: 0 for subject in subjects}
    # for i in range(num):
    #     preference_subjects = [student[2][i] for student in students]
    #     preference_subjects_count = {subject: preference_subjects_count[subject] + preference_subjects.count(subject) for subject in subjects}


    # subject_preferences_count = {}
    # total_appearances = {}
    # for subject in subjects:
    #     subject_preferences_count[subject] = [0] * num
    #     total_appearances[subject] = 0

    # # Create the directory to save the images

    # for i in range(num):
    #     preference_subjects = [student[2][i] for student in students]
    #     subject_count = {subject: preference_subjects.count(subject) for subject in subjects}
    #     for j, (subject, count) in enumerate(subject_count.items()):
    #         subject_preferences_count[subject][i] = count
    #         total_appearances[subject] += count

    #     fig, ax = plt.subplots()
    #     ax.pie(list(subject_count.values()), labels=list(subject_count.keys()), autopct='%1.1f%%', startangle=90)
    #     ax.axis('equal')
    #     ax.set_title(f"Preference {i+1}")
    #     plt.savefig(f'Excel/preference_{i+1}.png')  # Save the image
    #     plt.close()  # Close the figure to free memory

    # for subject, count in subject_preferences_count.items():
    #     print(subject, count, f"Total Appearances: {total_appearances[subject]}")

    # # sort subjects based on their total appearances
    # sorted_subjects = sorted(total_appearances.items(), key=lambda x: x[1], reverse=True)

    # import matplotlib.pyplot as plt
    # import numpy as np

    # # Create a bar graph for sorted_subjects
    # subjects = [subject for subject, _ in sorted_subjects]
    # counts = [count for _, count in sorted_subjects]

    # fig, ax = plt.subplots(figsize=(10,6))
    # ax.bar(subjects, counts, color=[plt.cm.Blues(i/int(len(subjects)*1.5)) for i in reversed(range(2*len(subjects)))])
    # ax.set_title("Total Appearances of Subjects")
    # ax.set_xlabel("Subject")
    # ax.set_ylabel("Total Appearances")
    # ax.tick_params(axis='x', labelrotation=45, pad=10)
    # plt.tight_layout()

    # # Save the image in Excel folder
    # plt.savefig("Excel/total_appearances.png", dpi=300)

    # # Show the image
    # #plt.show()


    # # save the chart as a PNG image in the "Excel" folder
    # fig.savefig("Excel/subject_appearances.png")
    # # extract the top `num` subjects
    # top_subjects = [subject for subject, count in sorted_subjects[:num]]

    # # extract the count of the top `num` subjects
    # top_subjects_count = [total_appearances[subject] for subject in top_subjects]



    # print(f"\nTop {num} subjects by appearances:")
    # for i in range(num):
    #     print(f"{i+1}. {top_subjects[i]}: {top_subjects_count[i]}")
        
    # # sort the preferences by their count and extract the top `num` preferences
    # sorted_preferences = sorted(preference_subjects_count.items(), key=lambda x: x[1], reverse=True)
    # preferences = [preference for preference, count in sorted_preferences[:num]]

    # min_batch_size = int(input("Enter minimum batch size: "))
    # max_batch_size = int(len(students)) - int((num-1) * min_batch_size); 
    # print(max_batch_size)
    # # create empty lists for each preference subject
    # lists_dict = {}
    # for preference in preferences:
    #     lists_dict[preference] = []

    # # iterate over the students and allocate them to their top preference subject
    # for student in students:
    #     allocated = False
    #     for preference in student[2]:
    #         if preference in preferences and len(lists_dict[preference]) < max_batch_size:
    #             lists_dict[preference].append(student)
    #             allocated = True
    #             break
    #     if not allocated:
    #         lists_dict[preferences[0]].append(student)

    # # count the number of students in each preference subject list
    # subject_student_count = {preference: len(lists_dict[preference]) for preference in preferences}

    # # ensure that each preference subject has at least min_batch_size students in it
    # for preference in preferences:
    #     while subject_student_count[preference] < min_batch_size:
    #         for student in students:
    #             if preference in student[2] and student not in lists_dict[preference]:
    #                 lists_dict[preference].append(student)
    #                 subject_student_count[preference] += 1
    #                 break

    # # print the list of subjects and the students in each subject list
    # for preference, students in lists_dict.items():
    #     print(f"{preference}: {len(students)} students")
    #     for student in students:
    #         print(f"- {student[0]} ({student[3]})")


    # # create a new workbook and select the active worksheet
    # import xlsxwriter

    # # create a new workbook and add a worksheet
    # wb = xlsxwriter.Workbook('D:\Downloads\Excel\student_lists.xlsx')
    # sheet = wb.add_worksheet()

    # # define the header row and write it to the sheet
    # header = ['Total Students', '']
    # for subject in lists_dict:
    #     header.append(f"{subject}")
    # sheet.write_row(0, 0, header)

    # # define the count row and write it to the sheet
    # count_row = [len(students), '']
    # for subject in lists_dict:
    #     count_row.append(len(lists_dict[subject]))
    # count_row.append('')
    # sheet.write_row(1, 0, count_row)

    # # define alignment for the header and count rows
    # header_format = wb.add_format({'align': 'center', 'valign': 'vcenter'})
    # sheet.set_row(0, None, header_format)
    # sheet.set_row(1, None, header_format)

    # # add a blank row after the count row
    # sheet.merge_range(2, 0, 2, 2, '')

    # row_num = 3
    # header = ['Student Name', 'Department', 'Pointer','Subject','Approved']
    # sheet.write_row(row_num, 0, header)
    # # iterate over the subjects and write each subject's student list to the sheet
    # row_num += 1 # starting row number

    # for subject in lists_dict:
    #     # add a blank row before starting a new subject's list
    #     if row_num != 3:
    #         sheet.merge_range(row_num, 0, row_num, 4, '')
    #         row_num += 1

    #     # write the subject name to the sheet
    #     sheet.merge_range(row_num, 0, row_num, 4, subject)
    #     sheet.write(row_num, 0, subject, header_format)
    #     row_num += 1

    #     # write each student's details to the sheet
    #     for student in lists_dict[subject]:
    #         name, department, _, pointer = student
    #         row_data = [name, department, pointer, subject]
    #         sheet.write_row(row_num, 0, row_data)
    #         row_num += 1

    # # adjust column widths and row heights
    # # for col in range(num+3):
    # #     sheet.set_column(col, col, len(header[col])+2)
    # # for row in range(1, row_num):
    # #     sheet.set_row(row, 15)

    # # close the workbook
    # wb.close()

    # students = student.objects.all()
    # # student_names = [student.stud_name for student in students]
    # context = {'student_names': students}
    # return render(request, 'student_pref.html', context)
    # # stud_name = student.objects.all()
    # # stud_name = [stud_name for student in student]
    # # context = {'stud_name': stud_name}
    # # return render(request, 'student_pref.html', context)


def student_detail(request, roll_no):
    student = tudent.objects.get(roll_no=roll_no)
    return render(request, 'student_detail.html', {'student': student})