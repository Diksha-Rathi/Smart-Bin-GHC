from django.shortcuts import render
from bins.models import *

# Create your views here.
def bins(request):
	result1 = bin_info.objects.filter(fill_level__range=(71, 100))
	result2 = bin_info.objects.filter(fill_level__range=(51, 70))
	result3 = bin_info.objects.filter(fill_level__range=(0, 50))
	return render(request, 'bins.html',{'result1': result1, 'result2': result2, 'result3': result3})