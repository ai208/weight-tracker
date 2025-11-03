from django.shortcuts import render

# Create your views here.
def bmi_view(request):
    return render(request, 'bmi.html')
