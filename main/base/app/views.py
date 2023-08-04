from typing import Any, Dict
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicantForm
from .models import Applicant
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    return render(request, 'home.html')

def submissions(request):
    applicants = Applicant.objects.all()
    return render(request, 'submissions.html', {'applicants':applicants})

def submit_form(request):
    if request.method == 'POST':
        print("Form data recieved: ", request.POST)
        form = ApplicantForm(request.POST, request.FILES)
        print("Form errors: ",form.errors)
        if form.is_valid():
            form.save()
            print("Created applicant")
            messages.success(request, 'Form submitted successfully!')
            return render(request, 'home.html')
        else:
            
            return render(request, 'home.html', {'form': form})
    else:
        form = ApplicantForm()
    return render(request, 'home.html')
    
def upload_file(request):
    if request.method == 'POST' and request.FILES.get('fileUpload'):
        # Handle file upload here, e.g., save the file to the server
        file = request.FILES['fileUpload']
        # Process the file as needed (e.g., saving to the database or disk)

        # Return a JSON response indicating success
        return JsonResponse({'success': True})
    else:
        # Return a JSON response indicating failure
        return JsonResponse({'success': False})
    
# user registration and sign up:
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as dj_login
from django.views.generic.edit import FormView
from django.views.generic import TemplateView

class RegisterPage(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('submissions')

    def form_valid(self, form):
        user = form.save()

        if user is not None:
            dj_login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('submissions')
        return super(RegisterPage, self).get(*args, **kwargs)
    
    def form_invalid(self, form):
        error_messages = []
        for field, errors in form.errors.items():
            if field!= '__all__':
                error_messages.extend(errors)
        error_message = error_messages[0] if error_messages else 'invalid signup credentials'

        return redirect(reverse_lazy('home', kwargs={'message':str(error_message)}))
    
class Submissions(LoginRequiredMixin, TemplateView):
    template_name = 'submissions.html'
    login_url = '/login/'  # Replace with the URL of your login page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['applicants'] = Applicant.objects.all()
        return context


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('submissions')
    
    def form_invalid(self, form):
        error_message = form.non_field_errors()[0] if form.non_field_errors() else 'Invalid login credentials'
        return redirect(reverse_lazy('home', kwargs={'message':str(error_message)}))
