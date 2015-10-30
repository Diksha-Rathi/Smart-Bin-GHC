from django.shortcuts import render
from bins.models import *
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse

# Create your views here.
@login_required
def bins(request):
	result1 = bin_updates.objects.filter(fill_level__range=(71, 100))
	result2 = bin_updates.objects.filter(fill_level__range=(51, 70))
	result3 = bin_updates.objects.filter(fill_level__range=(0, 50))
	return render(request, 'bins.html',{'result1': result1, 'result2': result2, 'result3': result3})

@login_required
def my_json_view(request):
	bins = bin_record.objects.all()
	data = serializers.serialize("json", bins)
	return HttpResponse(data, content_type="application/json")

@login_required
def my_json_view2(request):
	bin_update = bin_updates.objects.all()
	data = serializers.serialize("json",bin_update)
	return HttpResponse(data, content_type="application/json")
