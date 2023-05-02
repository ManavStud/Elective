#from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from student.models import student
from django.conf import settings
from subject.models import subject,Exposure_Courses
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
from student.models import faculty
from student.models import student
from django import template
from preference.models import preference

# register = template.Library()

# @register.filter(name='get_range')
# def get_range(min_val, max_val):
#     return range(min_val, max_val + 1)


# def user_info(request):
#     # Retrieve the access token from the session
#     access_token = request.session.get('access_token')
#     # Check if access_token is present in the session
#     if access_token:
#         try:
#             # Build the Google Drive API client
#             credentials = Credentials.from_authorized_user_info(info=access_token)
#             service = build('drive', 'v3', credentials=credentials)
#             # Get the user's storage information
#             about = service.about().get(fields='storageQuota').execute()
#             total_storage = about['storageQuota']['limit']
#             used_storage = about['storageQuota']['usage']
#             # Render the user_info.html template with the retrieved storage details
#             context = {'total_storage': total_storage, 'used_storage': used_storage}
#             return render(request, 'user_info.html', context)
#         except HttpError as error:
#             # Handle any errors that occur while accessing the Google Drive API
#             print(f'An error occurred: {error}')
#             return render(request, 'error.html', {'error': 'Failed to retrieve user information.'})
#     else:
#         # Redirect to the login page if access_token is not present in the session
#         return redirect('google_login')

# def google_callback(request):
#     # Get the authorization code from the query parameter
#     code = request.GET.get('code', None)
#     if code:
#         try:
#             # Exchange authorization code for access token
#             credentials = Credentials.from_authorized_user_code(
#                 code,
#                 scopes=['https://www.googleapis.com/auth/userinfo.profile',
#                         'https://www.googleapis.com/auth/userinfo.email',
#                         'https://www.googleapis.com/auth/drive.metadata.readonly']
#             )
#             # Call the People API to retrieve user information
#             people_service = build('people', 'v1', credentials=credentials)
#             person = people_service.people().get(resourceName='people/me', personFields='names,emailAddresses,photos').execute()
#             # Extract relevant user information
#             user_name = person['names'][0]['displayName']
#             user_email = person['emailAddresses'][0]['value']
#             user_profile_picture = person['photos'][0]['url']
            
#             # Call the Drive API to retrieve storage information
#             drive_service = build('drive', 'v3', credentials=credentials)
#             about = drive_service.about().get(fields='storageQuota').execute()
#             total_storage = about['storageQuota']['limit']
#             used_storage = about['storageQuota']['usage']
            
#             # Pass user and storage information to template and render HTML page
#             return render(request, 'user_info.html', {'user_name': user_name, 'user_email': user_email, 'user_profile_picture': user_profile_picture, 'total_storage': total_storage, 'used_storage': used_storage})
#         except Exception as e:
#             # Handle any exceptions that may occur
#             print(f'Error: {e}')
#     return HttpResponseRedirect('/login')  # Redirect to login page if authorization code is not present
# def google_auth(request):
#     if not request.user.is_authenticated:
#         return redirect('login')

#     try:
#         social = UserSocialAuth.objects.get(user=request.user)
#         extra_data = social.extra_data
#         # Extract the profile information from the extra_data
#         profile_info = {
#             'name': extra_data.get('name', ''),
#             'email': extra_data.get('email', ''),
#             'picture': extra_data.get('picture', ''),
#         }
#     except UserSocialAuth.DoesNotExist:
#         profile_info = {}
#     return render(request, 'profile.html', {'profile_info': profile_info})

def login(request):
    # context={
    #     'google_client_id': settings.GOOGLE_CLIENT_ID,
    #     'google_client_secret': settings.GOOGLE_CLIENT_SECRET
    # }
    
    return render(request,'login.html')

def nav(request):
    return render(request, 'nav.html')

def index(request):
    if request.user.is_authenticated:
        # Check if user's email is in the faculty table
        if faculty.objects.filter(fac_email=request.user.email).exists():
            # Redirect user to faculty_dashboard page
            return redirect('faculty_dashboard')
    
    exp1 = Exposure_Courses.objects.filter(sem=1).values_list('course_name',flat=True)
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

@login_required
def sem2(request):
    email = request.user.email
    print(email)
    
    try:
        rollno=student.objects.get(email=email)
    except student.DoesNotExist:
        return HttpResponse("You are not authorized to access this page.")
    roll_fetch=rollno.roll_no
    print(roll_fetch)


    exp2 = Exposure_Courses.objects.filter(sem=2).values_list('course_name',flat=True)
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
# if 

# def sem2_submit(request):
    
#     #gpa=request.POST.get(gpa)
#     roll=request.POST.get(roll)
#     pref1=request.POST.get()
#     try:
#         preference_obj = preference.objects.get(roll=roll)
#         print("Preference row already exists for roll number:", roll)
#     except preference.DoesNotExist:
#     # Create a new row with the given roll number and preferences
#         preference_obj = preference.objects.create(roll=roll, preference=preference)
#         print("Preference row created for roll number:", roll)
    
#     # You can now use preference_obj to access the preferences and other fields of the row
#     # For example, to get the preferences list, you can do:
#     preference_list = preference_obj.preference
    
#     return 


@login_required
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
    
@login_required
def sem4(request):
    email = request.user.email
    print(email)
    
    try:
        rollno=student.objects.get(email=email)
    except student.DoesNotExist:
        return HttpResponse("You are not authorized to access this page.")
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

@login_required
def sem5(request):
    email = request.user.email
    print(email)
    
    try:
        rollno=student.objects.get(email=email)
    except student.DoesNotExist:
        return HttpResponse("You are not authorized to access this page.")
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
        name_str = student.objects.filter(roll_no=16010121003).values()
        P.name = name_str[0]['stud_name']
        P.roll = roll
        P.sem = 2
        P.dept = name_str[0]['dept']
        P.pref1 = pref1
        P.pref2 = pref2
        P.pref3 = pref3
        P.pref4 = pref4
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

@login_required
def sem6(request):
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

@login_required
def sem7(request):
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

@login_required
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


@login_required
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
    
    exp1 = Exposure_Courses.objects.filter(sem=1).values_list('course_name',flat=True)
    exposure1 = list(exp1)
    #print(exposure2)
    for s1 in opt_courses_flat:
        for s2 in exposure1:
            if(s1 == s2):
                exp1 = s1
                break
    
    exp2 = Exposure_Courses.objects.filter(sem=2).values_list('course_name',flat=True)
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

@login_required
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

@login_required
def course_selection(request):
    email = request.user.email
    print(email)
    
    try:
        rollno=student.objects.get(email=email)
    except student.DoesNotExist:
        return HttpResponse("You are not authorized to access this page.")
    roll_fetch=rollno.roll_no
    print(roll_fetch)

    return render(request, 'course_selection.html')

@login_required
def faculty_dashboard(request):
    email = request.user.email
    print(email)
    
    try:
        rollno=student.objects.get(email=email)
    except student.DoesNotExist:
        return HttpResponse("You are not authorized to access this page.")
    roll_fetch=rollno.roll_no
    print(roll_fetch)
    
    if request.user.is_authenticated:
        # Check if user's email is in the faculty table
        if faculty.objects.filter(fac_email=request.user.email).exists():
            # Display faculty dashboard
            return render(request, 'faculty_dashboard.html')
    return redirect('card')


@login_required
def register(request):
    # compulsory_list = subject.objects.filter(sem=1,type='N').values_list('sub_name',flat=True)
    # compulsory_sem1 = list(compulsory_list)
    # print("Sem1: = ",compulsory_sem1)
    
    # compulsory_list = subject.objects.filter(sem=2,type='N').values_list('sub_name',flat=True)
    # compulsory_sem2 = list(compulsory_list)
    # print("Sem2: = ",compulsory_sem2)
    
    # compulsory_list = subject.objects.filter(sem=3,type='N').values_list('sub_name',flat=True)
    # compulsory_sem3 = list(compulsory_list)
    # print("Sem3: = ",compulsory_sem3)
    
    # compulsory_list = subject.objects.filter(sem=4,type='N').values_list('sub_name',flat=True)
    # compulsory_sem4 = list(compulsory_list)
    # print("Sem4: = ",compulsory_sem4)
    
    # compulsory_list = subject.objects.filter(sem=5,type='N').values_list('sub_name',flat=True)
    # compulsory_sem5 = list(compulsory_list)
    # print("Sem5: = ",compulsory_sem5)
    
    # compulsory_list = subject.objects.filter(sem=6,type='N').values_list('sub_name',flat=True)
    # compulsory_sem6 = list(compulsory_list)
    # print("Sem6: = ",compulsory_sem6)
    
    # compulsory_list = subject.objects.filter(sem=7,type='N').values_list('sub_name',flat=True)
    # compulsory_sem7 = list(compulsory_list)
    # print("Sem7: = ",compulsory_sem7)
    
    # compulsory_list = subject.objects.filter(sem=8,type='N').values_list('sub_name',flat=True)
    # compulsory_sem8 = list(compulsory_list)
    # print("Sem8: = ",compulsory_sem8)
    # name_str = student.objects.filter(roll_no=16010121813).values('stud_name')
    # name = name_str[0]['stud_name']
    # print("Name = ",name)
    
    # dept_str = student.objects.filter(roll_no=16010121813).values('dept')
    # dept = dept_str[0]['dept']
    # print("Department = ",dept)


    # subjects = subject.objects.filter(sem=5,type='DE').values('sub_id','sub_name')
    # s5e = [subject['sub_name'] for subject in subjects]
    # students = student.objects.filter(roll_no=16010121813).values('opt_course')
    # # opt_courses = students[0]['opt_course'].split(',')
    # opt_courses_flat = [course.strip() for course in opt_courses]
    # sem5_elective = ""
    # for s1 in opt_courses_flat:
    #     for s2 in s5e:
    #         if(s1 == s2):
    #             sem5_elective = s1
    #             break
    # print("Sem5 Elective = ",sem5_elective)
    
    
    # subjects = subject.objects.filter(sem=6,type='DE').values('sub_id','sub_name')
    # s5e = [subject['sub_name'] for subject in subjects]
    # sem6_elective = ""
    # for s1 in opt_courses_flat:
    #     for s2 in s5e:
    #         if(s1 == s2):
    #             sem6_elective = s1
    #             break
    # print("Sem6 Elective = ",sem6_elective)
    
    # subjects = subject.objects.filter(sem=7,type='DE').values('sub_id','sub_name')
    # s5e = [subject['sub_name'] for subject in subjects]
    # sem7_elective = []
    # for s1 in opt_courses_flat:
    #     for s2 in s5e:
    #         if(s1 == s2):
    #             sem7_elective.append(s1)
    # print("Sem7 Elective = ",sem7_elective)
    
    # subjects = subject.objects.filter(sem=8,type='DE').values('sub_id','sub_name')
    # s5e = [subject['sub_name'] for subject in subjects]
    # sem8_elective = []
    # for s1 in opt_courses_flat:
    #     for s2 in s5e:
    #         if(s1 == s2):
    #             sem8_elective.append(s1)
    # print("Sem8 Elective = ",sem8_elective)
    

    
    # exp2 = Exposure_Courses.objects.filter(sem=2).values_list('course_name',flat=True)
    # exposure2 = list(exp2)
    # #print(exposure2)
    # for s1 in opt_courses_flat:
    #     for s2 in exposure2:
    #         if(s1 == s2):
    #             exp2 = s1
    #             break
    # print("Sem2 Exposure Course = ",exp2)
    
    # unique_entries = list(student.objects.values_list('hon_min', flat=True).distinct())
    # print(unique_entries)
    email = request.user.email
    print(email)
    
    try:
        rollno=student.objects.get(email=email)
    except student.DoesNotExist:
        return HttpResponse("You are not authorized to access this page.")
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





















# #from django.shortcuts import render
# from django.http import HttpResponse,HttpResponseRedirect
# from student.models import student
# from django.conf import settings
# from subject.models import subject,Exposure_Courses
# from google.oauth2.credentials import Credentials
# from googleapiclient.discovery import build

# from django.shortcuts import render, redirect
# from social_django.models import UserSocialAuth
# from student.models import faculty


# def user_info(request):
#     # Retrieve the access token from the session
#     access_token = request.session.get('access_token')
#     # Check if access_token is present in the session
#     if access_token:
#         try:
#             # Build the Google Drive API client
#             credentials = Credentials.from_authorized_user_info(info=access_token)
#             service = build('drive', 'v3', credentials=credentials)
#             # Get the user's storage information
#             about = service.about().get(fields='storageQuota').execute()
#             total_storage = about['storageQuota']['limit']
#             used_storage = about['storageQuota']['usage']
#             # Render the user_info.html template with the retrieved storage details
#             context = {'total_storage': total_storage, 'used_storage': used_storage}
#             return render(request, 'user_info.html', context)
#         except HttpError as error:
#             # Handle any errors that occur while accessing the Google Drive API
#             print(f'An error occurred: {error}')
#             return render(request, 'error.html', {'error': 'Failed to retrieve user information.'})
#     else:
#         # Redirect to the login page if access_token is not present in the session
#         return redirect('google_login')

# def google_callback(request):
#     # Get the authorization code from the query parameter
#     code = request.GET.get('code', None)
#     if code:
#         try:
#             # Exchange authorization code for access token
#             credentials = Credentials.from_authorized_user_code(
#                 code,
#                 scopes=['https://www.googleapis.com/auth/userinfo.profile',
#                         'https://www.googleapis.com/auth/userinfo.email',
#                         'https://www.googleapis.com/auth/drive.metadata.readonly']
#             )
#             # Call the People API to retrieve user information
#             people_service = build('people', 'v1', credentials=credentials)
#             person = people_service.people().get(resourceName='people/me', personFields='names,emailAddresses,photos').execute()
#             # Extract relevant user information
#             user_name = person['names'][0]['displayName']
#             user_email = person['emailAddresses'][0]['value']
#             user_profile_picture = person['photos'][0]['url']
            
#             # Call the Drive API to retrieve storage information
#             drive_service = build('drive', 'v3', credentials=credentials)
#             about = drive_service.about().get(fields='storageQuota').execute()
#             total_storage = about['storageQuota']['limit']
#             used_storage = about['storageQuota']['usage']
            
#             # Pass user and storage information to template and render HTML page
#             return render(request, 'user_info.html', {'user_name': user_name, 'user_email': user_email, 'user_profile_picture': user_profile_picture, 'total_storage': total_storage, 'used_storage': used_storage})
#         except Exception as e:
#             # Handle any exceptions that may occur
#             print(f'Error: {e}')
#     return HttpResponseRedirect('/login')  # Redirect to login page if authorization code is not present
# # def google_auth(request):
# #     if not request.user.is_authenticated:
# #         return redirect('login')

# #     try:
# #         social = UserSocialAuth.objects.get(user=request.user)
# #         extra_data = social.extra_data
# #         # Extract the profile information from the extra_data
# #         profile_info = {
# #             'name': extra_data.get('name', ''),
# #             'email': extra_data.get('email', ''),
# #             'picture': extra_data.get('picture', ''),
# #         }
# #     except UserSocialAuth.DoesNotExist:
# #         profile_info = {}
# #     return render(request, 'profile.html', {'profile_info': profile_info})

# def login(request):
#     # context={
#     #     'google_client_id': settings.GOOGLE_CLIENT_ID,
#     #     'google_client_secret': settings.GOOGLE_CLIENT_SECRET
#     # }
    
#     return render(request,'login.html')

# def nav(request):
#     return render(request, 'nav.html')

def stud_pref(request):
    return render(request, "student_pref.html")

# def index(request):
#     if request.user.is_authenticated:
#         # Check if user's email is in the faculty table
#         if faculty.objects.filter(fac_email=request.user.email).exists():
#             # Redirect user to faculty_dashboard page
#             return redirect('faculty_dashboard')
    
#     exp1 = Exposure_Courses.objects.filter(sem=1).values_list('course_name',flat=True)
#     exposure1 = list(exp1)
#     # for s1 in opt_courses_flat:
#     #     for s2 in exposure1:
#     #         if(s1 == s2):
#     #             exp1 = s1
#     #             break
#     print("Sem1 Exposure Course = ",exp1)
#     compulsory_list = subject.objects.filter(sem=1,type='N').values_list('sub_name',flat=True)
#     compulsory_sem1 = list(compulsory_list)
#     context = {
#         'my_list': exposure1,
#         'compulsory_sem1':compulsory_sem1,
#         }
#     return render(request, 'index.html', context)

# def sem2(request):
#     exp2 = Exposure_Courses.objects.filter(sem=2).values_list('course_name',flat=True)
#     exposure2 = list(exp2)
#     compulsory_list = subject.objects.filter(sem=2,type='N').values_list('sub_name',flat=True)
#     compulsory_sem2 = list(compulsory_list)
#     print(compulsory_sem2)
#     context = {
#         'my_list': exposure2,
#         'compulsory_sem2':compulsory_sem2
#         }
#     return render(request, 'sem2.html', context)


# def sem3(request):
#     my_list = ['AI', 'ML', 'DSIP','IS','CC']
#     context = {'my_list': my_list}
#     compulsory_list = subject.objects.filter(sem=3,type='N').values_list('sub_name',flat=True)
#     compulsory_sem3 = list(compulsory_list)
#     print("Sem3: = ",compulsory_sem3)
#     context = {
#         'my_list': my_list,
#         'compulsory_sem3':compulsory_sem3
#         }
#     return render(request, 'sem3.html', context)

# def sem4(request):
#     my_list = ['AI', 'ML', 'DSIP','IS','CC']
#     context = {'my_list': my_list}
#     compulsory_list = subject.objects.filter(sem=3,type='N').values_list('sub_name',flat=True)
#     compulsory_sem4 = list(compulsory_list)
#     print("Se43: = ",compulsory_sem4)
#     context = {
#         'my_list': my_list,
#         'compulsory_sem4':compulsory_sem4
#         }
#     return render(request, 'sem4.html', context)

# def sem5(request):
#     name_str = student.objects.filter(roll_no=16010121003).values('stud_name')
#     name = name_str[0]['stud_name']
#     print("Name = ",name)
#     dept_str = student.objects.filter(roll_no=16010121003).values('dept')
#     dept = dept_str[0]['dept']
#     print("Department = ",dept)
#     my_list = subject.objects.filter(type='DE',sem=5).values_list('sub_name',flat=True)
#     my_list = list(my_list)
#     context = {'my_list': my_list}
#     compulsory_list = subject.objects.filter(sem=3,type='N').values_list('sub_name',flat=True)
#     compulsory_sem5 = list(compulsory_list)
#     print("Sem5: = ",compulsory_sem5)
#     context = {
#         'my_list': my_list,
#         'compulsory_sem5':compulsory_sem5
#         }
#     return render(request, 'sem5.html', context)

# def sem6(request):
#     name_str = student.objects.filter(roll_no=16010121003).values('stud_name')
#     name = name_str[0]['stud_name']
#     print("Name = ",name)

#     dept_str = student.objects.filter(roll_no=16010121003).values('dept')
#     dept = dept_str[0]['dept']
#     print("Department = ",dept)

#     my_list = subject.objects.filter(type='DE',sem=6).values_list('sub_name',flat=True)
#     my_list = list(my_list)    
#     compulsory_list = subject.objects.filter(sem=3,type='N').values_list('sub_name',flat=True)
#     compulsory_sem6 = list(compulsory_list)
#     print("Sem6: = ",compulsory_sem6)
#     context = {
#         'my_list': my_list,
#         'compulsory_sem6':compulsory_sem6
#         }
#     return render(request, 'sem6.html', context)

# def sem7(request):
#     name_str = student.objects.filter(roll_no=16010121003).values('stud_name')
#     name = name_str[0]['stud_name']
#     print("Name = ",name)
    
#     dept_str = student.objects.filter(roll_no=16010121003).values('dept')
#     dept = dept_str[0]['dept']
#     print("Department = ",dept)
    
#     my_list = ['AI', 'ML', 'DSIP','IS','CC']
#     context = {'my_list': my_list}
#     compulsory_list = subject.objects.filter(sem=3,type='N').values_list('sub_name',flat=True)
#     compulsory_sem7 = list(compulsory_list)
#     print("Sem3: = ",compulsory_sem7)
#     context = {
#         'my_list': my_list,
#         'compulsory_sem7':compulsory_sem7
#         }
#     return render(request, 'sem7.html', context)

# def sem8(request):
#     name_str = student.objects.filter(roll_no=16010121003).values('stud_name')
#     name = name_str[0]['stud_name']
#     print("Name = ",name)
    
#     dept_str = student.objects.filter(roll_no=16010121003).values('dept')
#     dept = dept_str[0]['dept']
#     print("Department = ",dept)
#     #kumbalitrance
#     my_list = ['AI', 'ML', 'DSIP','IS','CC']
#     context = {'my_list': my_list}
#     compulsory_list = subject.objects.filter(sem=3,type='N').values_list('sub_name',flat=True)
#     compulsory_sem8 = list(compulsory_list)
#     print("Sem3: = ",compulsory_sem8)
#     context = {
#         'my_list': my_list,
#         'compulsory_sem8':compulsory_sem8
#         }
#     return render(request, 'sem8.html', context)

# def card(request):
#     #Student: Name, Department, HonorMinor, Sempass
#     #Subjects
#     return render(request, 'card.html')

# def importt(request):
#     return render(request, 'import.html')

# def course_selection(request):
#     return render(request, 'course_selection.html')

# def faculty_dashboard(request):
#     if request.user.is_authenticated:
#         # Check if user's email is in the faculty table
#         if faculty.objects.filter(fac_email=request.user.email).exists():
#             # Display faculty dashboard
#             return render(request, 'faculty_dashboard.html')
#     return redirect('card')


# def register(request):
#     # compulsory_list = subject.objects.filter(sem=1,type='N').values_list('sub_name',flat=True)
#     # compulsory_sem1 = list(compulsory_list)
#     # print("Sem1: = ",compulsory_sem1)
    
#     # compulsory_list = subject.objects.filter(sem=2,type='N').values_list('sub_name',flat=True)
#     # compulsory_sem2 = list(compulsory_list)
#     # print("Sem2: = ",compulsory_sem2)
    
#     # compulsory_list = subject.objects.filter(sem=3,type='N').values_list('sub_name',flat=True)
#     # compulsory_sem3 = list(compulsory_list)
#     # print("Sem3: = ",compulsory_sem3)
    
#     # compulsory_list = subject.objects.filter(sem=4,type='N').values_list('sub_name',flat=True)
#     # compulsory_sem4 = list(compulsory_list)
#     # print("Sem4: = ",compulsory_sem4)
    
#     # compulsory_list = subject.objects.filter(sem=5,type='N').values_list('sub_name',flat=True)
#     # compulsory_sem5 = list(compulsory_list)
#     # print("Sem5: = ",compulsory_sem5)
    
#     # compulsory_list = subject.objects.filter(sem=6,type='N').values_list('sub_name',flat=True)
#     # compulsory_sem6 = list(compulsory_list)
#     # print("Sem6: = ",compulsory_sem6)
    
#     # compulsory_list = subject.objects.filter(sem=7,type='N').values_list('sub_name',flat=True)
#     # compulsory_sem7 = list(compulsory_list)
#     # print("Sem7: = ",compulsory_sem7)
    
#     # compulsory_list = subject.objects.filter(sem=8,type='N').values_list('sub_name',flat=True)
#     # compulsory_sem8 = list(compulsory_list)
#     # print("Sem8: = ",compulsory_sem8)
#     # name_str = student.objects.filter(roll_no=16010121813).values('stud_name')
#     # name = name_str[0]['stud_name']
#     # print("Name = ",name)
    
#     # dept_str = student.objects.filter(roll_no=16010121813).values('dept')
#     # dept = dept_str[0]['dept']
#     # print("Department = ",dept)


#     # subjects = subject.objects.filter(sem=5,type='DE').values('sub_id','sub_name')
#     # s5e = [subject['sub_name'] for subject in subjects]
#     # students = student.objects.filter(roll_no=16010121813).values('opt_course')
#     # # opt_courses = students[0]['opt_course'].split(',')
#     # opt_courses_flat = [course.strip() for course in opt_courses]
#     # sem5_elective = ""
#     # for s1 in opt_courses_flat:
#     #     for s2 in s5e:
#     #         if(s1 == s2):
#     #             sem5_elective = s1
#     #             break
#     # print("Sem5 Elective = ",sem5_elective)
    
    
#     # subjects = subject.objects.filter(sem=6,type='DE').values('sub_id','sub_name')
#     # s5e = [subject['sub_name'] for subject in subjects]
#     # sem6_elective = ""
#     # for s1 in opt_courses_flat:
#     #     for s2 in s5e:
#     #         if(s1 == s2):
#     #             sem6_elective = s1
#     #             break
#     # print("Sem6 Elective = ",sem6_elective)
    
#     # subjects = subject.objects.filter(sem=7,type='DE').values('sub_id','sub_name')
#     # s5e = [subject['sub_name'] for subject in subjects]
#     # sem7_elective = []
#     # for s1 in opt_courses_flat:
#     #     for s2 in s5e:
#     #         if(s1 == s2):
#     #             sem7_elective.append(s1)
#     # print("Sem7 Elective = ",sem7_elective)
    
#     # subjects = subject.objects.filter(sem=8,type='DE').values('sub_id','sub_name')
#     # s5e = [subject['sub_name'] for subject in subjects]
#     # sem8_elective = []
#     # for s1 in opt_courses_flat:
#     #     for s2 in s5e:
#     #         if(s1 == s2):
#     #             sem8_elective.append(s1)
#     # print("Sem8 Elective = ",sem8_elective)
    

    
#     # exp2 = Exposure_Courses.objects.filter(sem=2).values_list('course_name',flat=True)
#     # exposure2 = list(exp2)
#     # #print(exposure2)
#     # for s1 in opt_courses_flat:
#     #     for s2 in exposure2:
#     #         if(s1 == s2):
#     #             exp2 = s1
#     #             break
#     # print("Sem2 Exposure Course = ",exp2)
    
#     # unique_entries = list(student.objects.values_list('hon_min', flat=True).distinct())
#     # print(unique_entries)
    
#     if request.method == 'POST':
#         roll_no = request.POST.get('roll_no')
#         stud_name = request.POST.get('stud_name')
#         dept = request.POST.get('dept')
#         utype = request.POST.get('utype')
#         passw = request.POST.get('pass')
#         cpassw = request.POST.get('cpass')
#         username = request.POST.get('username')
#         # admit_year = request.POST.get('admit_year')
#         # opt_course = request.POST.get('opt_course')
#         # gpa = request.POST.get('gpa')
        
#         # Create a new instance of your model with the submitted data
#         new_object = student(
#             roll_no=roll_no,
#             stud_name=stud_name,
#             dept=dept,
#             utype=utype,
#             password=passw,
#             cpassw=cpassw,
#             username=username
#         )
#         # Save the new object to the database
#         new_object.save()
#         # Redirect to a success page
#         return render(request, 'index.html')
#     # Render the form template if this is a GET request
#     return render(request, 'register.html')