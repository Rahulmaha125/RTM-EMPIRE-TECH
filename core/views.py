from django.shortcuts import render
from .models import Internship, Job, Application
from .models import Contact

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')
def services(request):
    return render(request, 'pages/services.html')
def portfolio(request):
    return render(request, 'pages/portfolio.html')


from django.shortcuts import render, redirect
from .models import Internship, Job, Application


def careers(request):

    if request.method == "POST":

        Application.objects.create(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            mobile=request.POST.get('mobile'),
            qualification=request.POST.get('qualification'),
            skills=request.POST.get('skills'),
            application_type=request.POST.get('application_type'),
            applied_for='General Application',
            resume=request.FILES.get('resume')
        )

        return redirect('careers')

    internships = Internship.objects.filter(status='Open')
    jobs = Job.objects.filter(status='Open')

    context = {
        'internships': internships,
        'jobs': jobs,
    }

    return render(request, 'pages/careers.html', context)

from django.shortcuts import render, redirect

def contact(request):

    if request.method == "POST":

        Contact.objects.create(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            subject=request.POST.get('subject'),
            message=request.POST.get('message')
        )

        return redirect('contact')

    return render(request, 'pages/contact.html')

from django.shortcuts import render, redirect
from .models import Quote, SiteStats

def quote(request):

    if request.method == "POST":

        Quote.objects.create(
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            company=request.POST.get('company'),
            service=request.POST.get('service'),
            budget=request.POST.get('budget'),
            timeline=request.POST.get('timeline'),
            project_details=request.POST.get('project_details')
        )

        return redirect('quote')

    # GET request साठी नेहमी stats घ्या
    stats = SiteStats.objects.first()

    return render(
        request,
        'pages/quote.html',
        {
            'stats': stats
        }
    )


from .models import Testimonial

def quote(request):

    stats = SiteStats.objects.first()

    testimonials = Testimonial.objects.filter(approved=True)

    context = {
        'stats': stats,
        'testimonials': testimonials,
    }

    return render(request, 'pages/quote.html', context)