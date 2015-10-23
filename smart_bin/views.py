from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def home(request):
    return render_to_response('index.html', context_instance=RequestContext(request))

def bins(request):
    return render_to_response('bins.html', context_instance=RequestContext(request))

def bins(request):
    return render_to_response('bins.html', context_instance=RequestContext(request))

def optimalRoute(request):
    return render_to_response('optimal-route.html', context_instance=RequestContext(request))

def analytics(request):
    return render_to_response('analytics.html', context_instance=RequestContext(request))