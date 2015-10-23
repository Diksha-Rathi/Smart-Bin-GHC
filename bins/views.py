from django.shortcuts import render

# Create your views here.
def bins(request):
	result = bin_info.objects.filter(location_id='Location 1')
        return render(request, 'bins.html',{'result': result})