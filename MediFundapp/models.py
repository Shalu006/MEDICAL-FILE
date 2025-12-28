from django.db import models

class MedicalLead(models.Model):
      #patient info
    lead_generate_by = models.CharField(max_length=255)
    lead_purpose = models.TextField()
    patient_name = models.CharField(max_length=255)
    patient_address = models.TextField()
    patient_age = models.IntegerField()
    patient_case = models.TextField()
    claim_amount = models.DecimalField(max_digits=10, decimal_places=2)
    estimate_amount = models.DecimalField(max_digits=10, decimal_places=2)
    estimate_date = models.DateField()
    patient_education = models.CharField(max_length=255)
    patient_occupation = models.CharField(max_length=255)
    patient_pic_2 = models.ImageField(upload_to='patients/', null=True, blank=True)
    patient_id = models.FileField(upload_to='proofs/', null=True, blank=True)
    
    # Guardian Info
    
    guardian_name = models.CharField(max_length=255)
    guardian_number = models.CharField(max_length=15)
    
    # Doctor info
    hospital_name = models.CharField(max_length=255)
    doctor_number = models.CharField(max_length=15)
    prescription_documents = models.FileField(upload_to='prescriptions/', null=True, blank=True)
    description_documents = models.FileField(upload_to='descriptions/', null=True, blank=True)
    case_type = models.CharField(max_length=100)
    lead_source = models.CharField(max_length=101)

class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    pan_details = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=1,blank=True)

class raising_fund_info(models.Model):
    fund_purpose = models.CharField(null=False, max_length=255)
    fund_raising_amount = models.IntegerField(null=False)
    fund_title = models.CharField(null=False, unique=True)
    fund_for = models.CharField(null=False, max_length=35, unique=True)
    user_qualification = models.CharField(null=False, max_length=35, unique=True)
    user_emp_status = models.CharField(null=False, max_length=255)
    how_to_know = models.CharField(null=False, max_length=255)
    attachments = models.TextField(null=False)

class patient_info(models.Model):
    paitient_full_name = models.CharField(null=False, max_length=255)
    paitient_age = models.IntegerField(null=False)
    hospitalisation_status = models.CharField(null=False, unique=True)
    hospital = models.CharField(null=False, max_length=35, unique=True)
    enter_city = models.CharField(null=False, max_length=35, unique=True)
    user_emp_status = models.CharField(null=False, max_length=255)
    how_to_know = models.CharField(null=False, max_length=255)

class patient_story_info(models.Model):
    patienet_story = models.TextField(null=False)
    attachments = models.TextField(null=False, default='zxcvbnm')


class fund_raising_form(models.Model):
    user_info = models.CharField(max_length=255, blank=True)
    user_id = models.IntegerField()
    user_qualification = models.CharField(max_length=255, blank=True)
    user_employed_status = models.CharField(max_length=255, blank=True)
    how_to_know = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=50)
    fund_title = models.CharField(max_length=255, blank=True)
    fund_purpose = models.TextField(blank=True)
    fund_for = models.CharField(max_length=255, blank=True)
    fund_raising_amount = models.IntegerField()
    amount_raised = models.IntegerField(default=0)
    status = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=255, blank=True)
    ngo_name = models.CharField(max_length=255, blank=True)
    ngo_registration_number = models.CharField(max_length=255, blank=True)
    ngo_website_url = models.URLField(blank=True)
    patienet_full_name = models.CharField(max_length=255, blank=True)
    patienet_age = models.IntegerField(blank=True, null=True)
    hospitalization_status = models.CharField(max_length=255, blank=True)
    hospital_name = models.CharField(max_length=255, blank=True)
    hospital_location = models.CharField(max_length=255, blank=True)
    animal_type = models.CharField(max_length=255, blank=True)
    animal_name = models.CharField(max_length=255, blank=True)
    animal_age = models.IntegerField(blank=True, null=True)
    treatment_reason = models.TextField(blank=True)
    vetnairy_name = models.CharField(max_length=255, blank=True)
    vetnairy_clinic_name = models.CharField(max_length=255, blank=True)
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)
    medical_documents = models.FileField(upload_to='documents/', blank=True, null=True)
    patienet_image = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_date = models.DateField()
    created_by = models.CharField(max_length=255)
    last_created_date = models.DateField( null=True )
    last_created_by = models.CharField(max_length=255)
