from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=15, unique=True)
    pan_details = models.CharField(max_length=10, unique=True)
    gender = models.CharField(max_length=1,blank=True)


class Signup(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=False)
    password = models.TextField(max_length=35)
    mobile_number = models.BigIntegerField(unique=False)
    creation_purpose = models.CharField(max_length=255)

class raising_fund_info(models.Model):
    fund_purpose = models.CharField(null=False, max_length=255)
    fund_raising_amount = models.IntegerField(null=False,max_length=999999999999999)
    fund_title = models.CharField(null=False, unique=True)
    fund_for = models.CharField(null=False, max_length=35, unique=True)
    user_qualification = models.CharField(null=False, max_length=35, unique=True)
    user_emp_status = models.CharField(null=False, max_length=255)
    how_to_know = models.CharField(null=False, max_length=255)
    attachments = models.TextField(null=False)

class patienet_info(models.Model):
    paitient_full_name = models.CharField(null=False, max_length=255)
    paitient_age = models.IntegerField(null=False,max_length=999999999999999)
    hospitalisation_status = models.CharField(null=False, unique=True)
    hospital = models.CharField(null=False, max_length=35, unique=True)
    enter_city = models.CharField(null=False, max_length=35, unique=True)
    user_emp_status = models.CharField(null=False, max_length=255)
    how_to_know = models.CharField(null=False, max_length=255)

class patienet_story_info(models.Model):
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
