from django.shortcuts import render
from .models import Organization, CATEGORY_CHOICES

def organization_list(request):
    organizations = Organization.objects.all()

    context_variables = {}
    context_variables['organizations'] = organizations
    context_variables['categories'] = CATEGORY_CHOICES 

    return render(request, 'organizations/organization_list.html', context_variables)
