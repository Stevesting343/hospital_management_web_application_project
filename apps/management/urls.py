from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login_view'),
    path('index/', views.home, name='index'),
    path('pharmacy/', views.pharmacy, name='pharmacy'),

    # path('add_doctor/', views.add_doctor, name='add_doctor'),

    path('display_doctor', views.display_doctor, name='display_doctor'),


    # path('add_patient/', views.add_patient, name='add_patient'),
    path('display_patient/', views.display_patient, name='display_patient'),

    path('login_view/', views.login_view, name='login_view'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),

    path('edit_user/<int:pk>', views.edit_user, name='edit_user'),
    path('edit_user_d/<int:pk>', views.edit_user_d, name='edit_user_d'),
    path('delete_doctor/<int:pk>', views.delete_doctor, name='delete_doctor'),

    path('appointment/<int:pk>', views.appointment, name='appointment'),
    path('display_appointment/<int:pk>', views.display_appointment, name='display_appointment'),
    path('save_accepted_appointment/<str:name>/<str:mobile_no>/<int:age>/<str:gender>/<str:disease>/<str:d_name>/<str:speciality>/<int:d_id>/<int:p_id>/<int:pk>', views.save_accepted_appointment, name='save_accepted_appointment'),
    path('app_dis_to_pa/<int:pk>', views.app_dis_to_pa, name='app_dis_to_pa'),

    path('patient_history/', views.patient_history, name='patient_history'),

]
