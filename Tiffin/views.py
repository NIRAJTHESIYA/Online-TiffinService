from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.html import strip_spaces_between_tags
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.template.loader import render_to_string
from django.views.generic.list import ListView
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.utils import timezone 
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.conf import settings
from Tiffin.models import *
from django import forms
import datetime
import random
import re   



def send_mail_to_user_forgot_password(recipient, subject, name, otp):
    try:
        # Render the HTML content from the template
        html_content = render_to_string('otp_email_template.html', {'name': name, 'otp': otp})
        # Remove HTML tags for the plain text version
        plain_text_content = strip_tags(html_content)
        send_mail(
            subject,
            plain_text_content,  # Plain text content for email clients that don't support HTML
            'darshakribadiya333@gmail.com',
            [recipient],
            html_message=html_content,
        )
    except Exception as e:
        print(e)


def is_valid_email(email):
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    match = email_pattern.match(email)
    return bool(match)


def is_valid_contact(contact):
    mobile_pattern = re.compile("(0|91)?[-\s]?[6-9][0-9]{9}")
    match = mobile_pattern.match(contact)
    return bool(match)


def generate_otp():
    # Generate a 6-digit random number
    return ''.join(random.choices('0123456789', k=6))


#validation for forgot password
def validationforgotpassword(email,myuseremail):
    error = None
    if(not email):
        error = "Please enter E-mail address"
    elif email:
        if(email != myuseremail):
            error = "Please enter valid E-mail address"
            
    return error



# Create your views here.

# view for Index Page


# Index Page
def index(request):
    return render(request,'index.html')

    return render(request,'index.html')


# Header Page 
def header(request):
    return render(request, 'header.html')

    return render(request, 'header.html')


# Footer Page 
def footer(request):
    return render(request, 'footer.html')

    return render(request, 'footer.html')
    

# Registration Page
def reg(request):
    if request.method == "POST":
        Firstname = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        Password = request.POST['password']
        ConfirmPassword = request.POST['cpassword']
        if not is_valid_email(email):
            messages.success(request,'Invalid email format..')
            return redirect("reg")
        elif Password!=ConfirmPassword:
            messages.success(request,'Password Dosen\'t match..')
            return redirect("reg")
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('reg')
        elif not is_valid_contact(contact):
            messages.success(request,'Invalid Contact Number')
            return redirect("reg")
        elif(not contact):
            messages.error = (request, "Phone Number is required!")
            return redirect('reg')
        elif(len(contact)>10):
                messages.error = (request, "Enter valid Phone number")
                return redirect('reg')
        else:
            if is_valid_email(email):
                name=Firstname
                otp = generate_otp()
                # send_mail_to_user_forgot_password(email, f'Message from Tiffin service {name}. ', name, otp)
                # messages.success(request,'Email send successfully... ')
                new_user = User(first_name=Firstname.title(),contact=contact, email=email, password=make_password(Password),registration_date=timezone.now())
                new_user.save()
                messages.success(request,'Your Account Created Successfully')
                return redirect("login")
    return render(request,"reg.html")


# Login Page
def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            users = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password, user not exist')
            return redirect('login')
        if not check_password(password, users.password):
            messages.warning(request, 'Invalid email or password, password dose not match')
            return redirect('login')
        
        if User.status == False:
            messages.warning(request, 'You can\'t login in this site!!')
            return redirect('login')
        request.session['user_id'] = users.iduser
        request.session['first_name'] = users.first_name
        request.session['email'] = users.email
        request.session['login'] = True
        return redirect('index')  
    return render(request,"login.html")


# Forgot Password
def forgot_password(request):
    if request.method == "POST":
        uEmail = request.POST.get('email')
    

        #validation
        myuseremail = None
        mypassword = None
        myname = None
        error = None
        success = None
    
        c1 = User.objects.all()

        for item in c1:
            if(item.email == uEmail):
                myuseremail = item.email
                myname = item.first_name
                mypassword = item.password
                break
    
        #value Dictionary
        value = {
        'email':uEmail
        }
        # error = validationforgotpassword(uEmail,myuseremail)
        error = "Invalid email..."
        
    
        if not error:
            success = "Your password is sent to your email ID"
            subject = "Welcome to "
            mymessage = f"Hello {myname} Your password is: {mypassword}, thank you for visiting our site"
            email_from = "njthesiya111@gmail.com"
            recipient_list = [myuseremail,]
            data = {
            'success' :success
            }
            send_mail(subject, mymessage ,email_from, recipient_list)
            return render(request, 'forgot_password.html',data)
    
        else:
            data = {
            'error': error,
            'values':value
            }
            return render(request, 'forgot_password.html',data)
    
    return render(request,'forgot_password.html')


# Profile Page 
def profile(request):
    try:
        email=request.session.get('email')
        Users = User.objects.get(email=email)
        return render(request,'profile.html', {'user': Users}) 
    except User.DoesNotExist:
            messages.error(request, 'Invalid crediatonals..')
            return render(request,'profile.html')


# Update User Profile
def update_profile(request):
    if request.method == "POST":
        address=request.POST['address']            
        contact=request.POST['contact']            
        code=request.POST['code']            
        city=request.POST['city']
        area=request.POST['area']
        about=request.POST['about']
        try:
            email=request.session.get('email')
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Invalid crediatonals..')
            return redirect('update_profile') 
        user.city = city
        user.contact = contact
        user.address = address
        user.area = area
        # user.city = city
        user.code = code
        user.about = about
        user.save()
        request.session['user_id'] = user.iduser
        request.session['first_name'] = user.first_name
        messages.success(request,'Your Profile Updated Successfully..')
        return redirect("profile")
    try:
        email=request.session.get('email')
        user = User.objects.get(email=email)
        area_name = Area.objects.all()
        return render(request,'update_profile.html', {'user': user, 'area_name' : area_name})
    except User.DoesNotExist:
        messages.error(request, 'Invalid crediatonals..')
        return render(request,'update_profile.html')

# LogOut Page
def logout(request):
    request.session.flush()
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login') 

# Meal Page 
def meal(request):
    return render(request, 'meal.html')

    return render(request, 'meal.html')


# About Page
def about(request):
    return render(request, 'about.html')

    return render(request, 'about.html')


# Contact Page
def contact(request):
    return render(request, 'contact.html')
  
    return render(request, 'contact.html') 


# OTP Page
def otp(request):
    return render(request, 'otp.html')
  
    return render(request, 'otp.html') 


# Privacy Page
def privacy(request):
    return render(request, 'privacy.html')
  
    return render(request, 'privacy.html') 


# Terms Page
def terms(request):
    return render(request, 'terms.html')
  
    return render(request, 'terms.html') 


# Menu Page
def menu(request):
    return render(request, 'menu.html')
  
    return render(request, 'menu.html') 

# def menu_view(request):
#     days = Day.objects.all()
#     selected_date = request.GET.get('date')
#     menu_items = None

#     if selected_date:
#         selected_day = Day.objects.get(id=selected_date)
#         menu_items = Day_Menu.objects.filter(day=selected_day)

#     return render(request, 'menu.html', {'days': days, 'menu_items': menu_items, 'selected_date': selected_date})

