from django.shortcuts import render, redirect
from .models import *
import pandas as pd


def base(request):
    return render(request, 'dashboard.html')

from django.shortcuts import render
from .models import fund_raising_form

def dashboard(request):
    fundraisers = fund_raising_form.objects.all().order_by('-id')[:4]  # latest 4 trending
    return render(request, 'dashboard.html', {'fundraisers': fundraisers})
 

# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Signup


def fund_raising(request):
    if request.method == 'POST':
        fund_purpose = request.POST.get('fund_purpose')
        fund_raise_amount = request.POST.get('fund_raise_amount')
        fund_title = request.POST.get('fund_title')
        fund_for = request.POST.get('fund_for')
        user_qualification = request.POST.get('user_qualification')
        user_emp_status = request.POST.get('user_emp_status')
        how_to_know = request.POST.get('how_to_know')


        raising_fund_info.objects.create(
            fund_purpose=fund_purpose,
            fund_raise_amount=fund_raise_amount,
            fund_title=fund_title,
            fund_for=fund_for,
            user_qualification=user_qualification,
            user_emp_status=user_emp_status,
            how_to_know=how_to_know
        )

        messages.success(request, 'Fund information submitted successfully!')
        return redirect('dashboard') 

    return render(request, 'fund_raising.html')



from django.shortcuts import render, redirect
from .models import fund_raising_form
from datetime import date

def fund_raising_form_view(request):
    if request.method == "POST":
        category = request.POST.get("category", "")
        fund_raising_amount = request.POST.get("fund_raising_amount", "0")
        try:
            fund_raising_amount = int(fund_raising_amount)
        except ValueError:
            fund_raising_amount = 0

        common_fields = {
            "user_info": "John Doe",
            "user_id": 123,
            "category": category,
            "fund_raising_amount": fund_raising_amount,
            "amount_raised": 0,
            "status": "Pending",
            "attachments": request.FILES.get("attachments"),
            "medical_documents": request.FILES.get("medical_documents"),
            "start_date": date.today(),
            "end_date": date.today(),
            "created_date": date.today(),
            "created_by": "system",
            "last_created_date": date.today(),
            "last_created_by": "system"
        }

        # Apply form-specific logic
        if category == "medical":
            common_fields.update({
                "fund_for": request.POST.get("fund_for", ""),
                "patienet_full_name": request.POST.get("patienet_full_name", ""),
                "patienet_age": request.POST.get("patienet_age", 0),
                "hospital_name": request.POST.get("hospital_name", ""),
                "hospital_location": request.POST.get("hospital_location", ""),
                "hospitalization_status": request.POST.get("hospitalization_status", ""),
                "fund_purpose": request.POST.get("fund_purpose", ""),
            })

        elif category == "ngo":
            common_fields.update({
                "fund_title": request.POST.get("fund_title", ""),
                "ngo_name": request.POST.get("ngo_name", ""),
                "ngo_registration_number": request.POST.get("ngo_registration_number", ""),
                "ngo_website_url": request.POST.get("ngo_website_url", ""),
                "user_qualification": request.POST.get("user_qualification", ""),
                "user_employed_status": request.POST.get("user_employed_status", ""),
                "how_to_know": request.POST.get("how_to_know", "")
            })

        elif category == "other":
            common_fields.update({
                "fund_title": request.POST.get("fund_title", ""),
                "fund_for": request.POST.get("fund_for", ""),
                "user_qualification": request.POST.get("user_qualification", ""),
                "user_employed_status": request.POST.get("user_employed_status", ""),
                "how_to_know": request.POST.get("how_to_know", ""),
                "fund_purpose": request.POST.get("fund_purpose", "")
            })

        form_data = fund_raising_form(**common_fields)
        form_data.save()
        return redirect('dashboard')

    return render(request, 'fund_raising_form.html')



# ------------------------------------------------------------------------------------


from django.shortcuts import render, redirect
from .models import fund_raising_form
from datetime import date

def select_form_category(request):
    return render(request, 'select_category.html')

import base64

from datetime import date
from django.shortcuts import render, redirect
from .models import fund_raising_form

def medical_form(request):
    if request.method == 'POST':
        form_data = fund_raising_form(
            category=request.POST.get("category"),
            fund_for=request.POST.get("fund_for"),
            fund_title=request.POST.get("fund_title"),
            patienet_full_name=request.POST.get("patienet_full_name"),
            patienet_age=request.POST.get("patienet_age"),
            hospital_name=request.POST.get("hospital_name"),
            hospital_location=request.POST.get("hospital_location"),
            hospitalization_status=request.POST.get("hospitalization_status"),
            fund_raising_amount=request.POST.get("fund_raising_amount"),
            fund_purpose=request.POST.get("fund_purpose"),
            start_date=date.today(),
            end_date=date.today(),
            created_date=date.today(),
            user_id=123,
            user_info="Unknown",
            created_by="system",
        )

        # Convert image file to base64 string
        if request.FILES.get("attachments"):
            image_file = request.FILES.get("attachments")
            image_data = image_file.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')
            form_data.patienet_image = encoded_image

        form_data.save()
        return redirect('dashboard')

    return render(request, 'medical_form.html')


from datetime import date
from django.shortcuts import render, redirect
from .models import fund_raising_form

def ngo_form(request):
    if request.method == 'POST':
        form_data = fund_raising_form(
            category=request.POST.get("category"),
            fund_title=request.POST.get("fund_title", ""),
            ngo_name=request.POST.get("ngo_name", ""),
            ngo_registration_number=request.POST.get("ngo_registration_number", ""),
            ngo_website_url=request.POST.get("ngo_website_url", ""),
            user_qualification=request.POST.get("user_qualification", ""),
            user_employed_status=request.POST.get("user_employed_status", ""),
            how_to_know=request.POST.get("how_to_know", ""),
            fund_raising_amount=request.POST.get("fund_raising_amount", 0),
            start_date=date.today(),
            end_date=date.today(),
            created_date=date.today(),
            user_id=123,
            user_info="Unknown",
            created_by="system",
        )
        form_data.save()
        return redirect('dashboard')

    return render(request, 'ngo_form.html')

import base64
from datetime import date
from django.shortcuts import render, redirect
from .models import fund_raising_form

def other_form(request):
    if request.method == 'POST':
        form_data = fund_raising_form(
            category=request.POST.get("category"),
            fund_title=request.POST.get("fund_title", ""),
            fund_for=request.POST.get("fund_for", ""),
            fund_raising_amount=request.POST.get("fund_raising_amount", 0),
            user_qualification=request.POST.get("user_qualification", ""),
            user_employed_status=request.POST.get("user_employed_status", ""),
            how_to_know=request.POST.get("how_to_know", ""),
            fund_purpose=request.POST.get("fund_purpose", ""),
            start_date=date.today(),
            end_date=date.today(),
            created_date=date.today(),
            user_id=123,
            user_info="Unknown",
            created_by="system",
        )

        # Convert image file to base64 string if uploaded
        if request.FILES.get("attachments"):
            image_file = request.FILES.get("attachments")
            image_data = image_file.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')
            form_data.patienet_image = encoded_image

        # Save medical_documents file normally if your model allows it (optional)
        if request.FILES.get("medical_documents"):
            form_data.medical_documents = request.FILES.get("medical_documents")

        form_data.save()
        return redirect('dashboard')

    return render(request, 'other_form.html')


from .models import fund_raising_form
from django.http import HttpResponse

def excel(request):
    data = []
    if 'show' in request.GET:
        data = fund_raising_form.objects.all()
        return render(request, 'excel.html', {'data': data})
    return HttpResponse("Excel data or file here")

def patientinfo(request):
    if request.method == 'POST':
        request.session['patient_data'] = {
            'lead_generate_by': request.POST.get('lead_generate_by'),
            'lead_purpose': request.POST.get('lead_purpose'),
            'patient_name': request.POST.get('name'),
            'patient_age':request.POST.get('age'),
            'patient_case': request.POST.get('case'),
            'patient_education': request.POST.get('edu'),
            'patient_occupation': request.POST.get('occu'),
            'estimate_amount': request.POST.get('amount'),
            'estimate_date': request.POST.get('date'),
            'claim_amount': request.POST.get('claim'),
            'admit_date': request.POST.get('admit'),
            'patient_address': request.POST.get('address'),
            'patient_pic_2': request.FILES.get('photo').name if request.FILES.get('photo') else None,
            'patient_id': request.FILES.get('id').name if request.FILES.get('id') else None,
        }
        request.session['patient_files']= {
            'patient_id': request.FILES.get('id'),
            'patient_pic_2': request.FILES.get('photo')
        }               
        return redirect('guardianinfo') 
    return render(request, 'patientinfo.html')

def cards(request):
    lead = MedicalLead.objects.last()
    return render(request, 'cards.html', {'lead': lead})
        

def guardianinfo(request):
    if request.method == 'POST':
        request.session['guardian_data'] = {
            'guardian_name': request.POST.get('name'),
            'guardian_phone': request.POST.get('phone'),
        }
        return redirect('doctorinfo')
    return render(request, 'guardianinfo.html')

def doctorinfo(request):
    if request.method == 'POST':
        request.session['doctor_Data'] = {
            'hospital_name': request.POST.get('name'),
            'doctor_phone': request.POST.get('phone'),
            'case_type': request.POST.get('case'),
            'lead_source': request.POST.get('source'),
        }
        
        final_submit(request)
        
        request.session.flush()
        
        return redirect('success_page')
    return render(request, 'doctorinfo.html')
    
    
def final_submit(request):
        patient_data = request.session.get('patient_data', {})
        guardian_data = request.session.get('guardian_data', {})
        doctor_data = request.session.get('doctor_data', {})
        patient_files = request.session.get('patient_files', {})
        
        prescription_file = request.FILES.get('prescription'),
        description_file = request.FILES.get('description'),
        
        all_data = {
            **patient_data,
            **guardian_data,
            **doctor_data,
            **patient_files,
            'prescription_documents': prescription_file,
            'description_documents':  description_file,
        }
        
        MedicalLead.objects.create(**all_data)
        
def success_page(request):
            return render(request, 'success.html')
        
import openpyxl
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def download_excel_page(request):
    return render(request, 'download_medicalleads.html')
    
def download_medicalleads_excel(request):
    # Create workbook and sheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "MedicalLeads"

    # Header row – must match model fields (excluding files/images)
    headers = [
        'lead_generate_by', 'lead_purpose', 'patient_name', 'patient_address', 'patient_age',
        'patient_case', 'claim_amount', 'estimate_amount', 'estimate_date', 'patient_education',
        'patient_occupation', 'guardian_name', 'guardian_number', 'hospital_name',
        'doctor_number', 'case_type', 'lead_source'
    ]
    ws.append(headers)

    # Data rows
    for lead in MedicalLead.objects.all():
        ws.append([
            lead.lead_generate_by,
            lead.lead_purpose,
            lead.patient_name,
            lead.patient_address,
            lead.patient_age,
            lead.patient_case,
            lead.claim_amount,
            lead.estimate_amount,
            lead.estimate_date,
            lead.patient_education,
            lead.patient_occupation,
            lead.guardian_name,
            lead.guardian_number,
            lead.hospital_name,
            lead.doctor_number,
            lead.case_type,
            lead.lead_source
        ])

    # Send Excel as downloadable response
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=medicalleads.xlsx'

    wb.save(response)
    return response
