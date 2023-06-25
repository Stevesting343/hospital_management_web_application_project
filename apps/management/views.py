from django.shortcuts import render, redirect, HttpResponseRedirect, reverse, HttpResponse

from .forms import LoginForm, SignUpForm, EditUserprofileForm
from django.contrib.auth import authenticate, login, logout as auth_logout
from .models import Doctor, Patient, User, Appointment, Accepted_Data
from django.contrib.auth.forms import UserChangeForm

from datetime import date


# Create your views here.


def home(request):
    return render(request, 'index.html')


def pharmacy(request):
    return render(request, 'pharmacy.html')


# Doctor section
def store_doctor(request):
    d = Doctor()
    d.name = request.POST.get('d_name')
    d.category = request.POST.get('d_category')
    d.email = request.POST.get('d_email')
    # d.age = request.POST.get('d_age')
    d.gender = request.POST.get('d_gender')
    d.save()
    # print(d.name, d.email)

    # return render(request, 'add_doctor.html')
    return redirect('index')


# def add_doctor(request):
#     return render(request, 'add_doctor.html')


def display_doctor(request):
    show = User.objects.filter(type_user="Doctor")
    return render(request, 'display_doctor.html', {'data': show})


# ----------------------

# Patient section
def store_patient(request):
    p = Patient()
    p.name = request.POST.get('p_name')
    p.email = request.POST.get('p_email')
    p.age = request.POST.get('p_age')
    p.gender = request.POST.get('p_gender')
    p.mobile_no = request.POST.get('p_mobile')
    p.save()

    return redirect('index')


# def add_patient(request):
#     return render(request, 'add_patient.html')


def display_patient(request):
    show = User.objects.filter(type_user='Patient')
    return render(request, 'display_patient.html', {'data': show})

    # ----------------------


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = LoginForm(request.POST or None)
        msg = None
        if request.method == 'POST':
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                # print('User name :', user.username)
                # return redirect('index')
                # print('department :', user.department)
                if user is not None and user.type_user == "Patient":
                    login(request, user)
                    return redirect('index')
                elif user is not None and user.type_user == "Doctor":
                    login(request, user)
                    return redirect('index')
                elif user is not None and user.username == "admin1":
                    login(request, user)
                    return redirect('display_patient')
                else:
                    msg = 'invalid credentials'
            else:
                msg = 'error validating form'

    return render(request, 'login.html', {'form': form, 'msg': msg})


  # RameshSharma@2001
    # gaurav cha code working

    # if request.method == 'POST':
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('index')
    #
    # return render(request, 'login.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'msg': msg})


def edit_user_d(request, pk):  # edit button not working because we add
    msg = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        # override
        user = User.objects.get(id=pk)
        user.username = username
        user.email = email
        user.first_name = firstname             # it is a speciality in database assign first_name
        user.save()

    show = User.objects.filter(type_user="Doctor")
    return render(request, 'display_doctor.html', {'data': show})


def edit_user(request, pk):
    show = User.objects.get(id=pk)
    return render(request, 'edit_doctor.html', {'data': show})


def edit_user_p(request, pk):
    msg = None
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        # override
        user = User.objects.get(id=pk)
        user.username = username
        user.email = email
        user.first_name = firstname
        user.save()
    show = User.objects.filter(type_user="Patient")
    return render(request, 'display_patient.html', {'data': show})


# def edit_user_d(request, pk):
#     user = User.objects.get(id=pk)
#     user.name = request.POST.get('d_name')
#     user.first_name = request.POST.get('d_category')
#     user.email = request.POST.get('d_email')
#     # d.age = request.POST.get('d_age')
#     user.save()
#     return redirect('edit_details')


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return HttpResponseRedirect(reverse('login_view'))


def delete_doctor(request, pk):
    d = User.objects.get(id=pk)
    d.delete()
    return redirect('display_doctor')


def appointment(request, pk):
    d = User.objects.get(id=pk)
    if request.method == 'POST':
        full_name_a = request.POST.get('a_enter_full_name')
        mobile_a = request.POST.get('a_mobile')
        age_a = request.POST.get('a_age')
        gender_a = request.POST.get('a_gender')
        disease_a = request.POST.get('a_disease')

        d_id_a = request.POST.get('d_id')
        doctor_name_a = request.POST.get('username')
        speciality_a = request.POST.get('speciality')
        p_id_a = request.POST.get('p_id')
        data = Appointment(enter_full_name=full_name_a,
                           mobile_no=mobile_a,
                           age=age_a,
                           gender=gender_a,
                           disease=disease_a,
                           doctor_name=doctor_name_a,
                           speciality=speciality_a,
                           d_id=d_id_a,
                           p_id=p_id_a)
        data.save()
        d = Appointment.objects.filter(p_id=p_id_a)
        return render(request, 'display_appointment.html', {'data': d})
    return render(request, 'appointment.html', {'data': d})


def display_appointment(request, pk):
    if request.user.type_user == "Patient":  # display appointement by p_id
        d = Appointment.objects.filter(p_id=pk)
        return render(request, 'display_appointment.html', {'data': d})
    else:
        d = Appointment.objects.all()
        print(len(d))
        return render(request, 'display_appointment.html', {'data': d})


def save_accepted_appointment(request, name, mobile_no, age, gender, disease, d_name, speciality, d_id, p_id, pk):
    data = Accepted_Data(enter_full_name=name,
                         mobile_no=mobile_no,
                         age=age,
                         gender=gender,
                         disease=disease,
                         doctor_name=d_name,
                         speciality=speciality,
                         d_id=d_id,
                         p_id=p_id,
                         date=date.today())
    data.save()
    d = Appointment.objects.filter(id=pk)
    d.delete()
    data = Accepted_Data.objects.all()

    return render(request, 'accept.html', {'data': data})   # accept page is for appointement accepted data


def app_dis_to_pa(request, pk):
    if request.user.type_user == "Patient":
        data = Accepted_Data.objects.filter(p_id=pk)
    else:
        data = Accepted_Data.objects.all()
    return render(request, 'accept.html', {'data': data})


def patient_history(request):
    d = Accepted_Data.objects.all()

    if request.method == 'POST':
        val = request.POST.get('val')
        show = Accepted_Data.objects.filter(enter_full_name__contains=val)
        return render(request, 'dis_patient_histroy.html', {'data': show})
    return render(request, 'dis_patient_histroy.html', {'data': d})

































































































































































































































































































































































