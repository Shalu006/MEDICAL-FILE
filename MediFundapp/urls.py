
from django.urls import path
from . import views
from django.urls import path, include
# from .views import download_students_excel
from .views import download_medicalleads_excel

urlpatterns = [
    # path('', views.base, name='base'),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('patientinfo/', views.patientinfo, name='patientinfo'),
    path('guardianinfo/',views.guardianinfo, name='guardianinfo'),
    path('doctorinfo/',views.doctorinfo, name='doctorinfo'),
    # path('studentinfo/',views.studentinfo, name='studentinfo'),
    # path('success/',views.success, name='success'),
    path('login/',views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/',views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('fund_raising/', views.fund_raising, name='fund_raising'),
    path('fund_raising_form/', views.fund_raising_form_view, name='fund_raising_form'),
    path('fundraising/', views.select_form_category, name='fundraising_category'),
    path('fundraising/medical/', views.medical_form, name='medical_form'),
    path('fundraising/ngo/', views.ngo_form, name='ngo_form'),
    path('fundraising/other/', views.other_form, name='other_form'),
    path('accounts/', include('allauth.urls')),
    # path('students/download/', download_students_excel, name='download_students_excel'),
    path('medicalleads_excel/', views.download_excel_page, name='excel_download_page'),
    path('download_excel/', views.download_medicalleads_excel, name='download_medicalleads_excel'),
    path('api/medicalleads/', views.medicallead_list, name='medicallead-list'),
    path('api/medicalleads/<int:pk>/', views.medicallead_detail, name='medicallead-detail'),
    
]
