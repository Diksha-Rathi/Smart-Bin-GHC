from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from bins.models import *
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse
from datetime import date
<<<<<<< HEAD
from bins.forms import ToDoForm
from django.template.loader import get_template
from django.template import RequestContext
#from weasyprint import HTML, CSS
from django.http import HttpResponse
=======
from django.template.loader import get_template
from django.template import RequestContext
#from weasyprint import HTML, CSS
#from django.http import HttpResponse
>>>>>>> fcfcb272d77a31ee8ace091a85de1ea360cc651e
from django.template import loader, Context
import djqscsv

# Create your views here.
@login_required
def bins(request):
	result1 = bin_updates.objects.filter(fill_level__range=(71, 100), date=date.today())
	result2 = bin_updates.objects.filter(fill_level__range=(51, 70), date=date.today())
	result3 = bin_updates.objects.filter(fill_level__range=(0, 50), date=date.today())
	return render(request, 'bins.html',{'result1': result1, 'result2': result2, 'result3': result3})

@login_required
def details_curr(request):
    return render_to_response('details_curr.html', context_instance=RequestContext(request))

@login_required
def details_custom(request):
    if request.method == 'GET':
        form = ToDoForm()
    else:
        form = ToDoForm(request.POST)
        return HttpResponseRedirect('/detail_graph.html')
    return render(request,
                  "details_custom.html",
                  dict(form=form))

@login_required
def detail_graph(request):
    return render_to_response('detail_graph.html', context_instance=RequestContext(request))

@login_required
def optimalRoute(request):
    return render_to_response('optimal-route.html', context_instance=RequestContext(request))

@login_required
def analytics(request):
    if request.method == 'GET':
        form = ToDoForm()
    else:
        form = ToDoForm(request.POST)
        return HttpResponseRedirect('/export.html')
    result1 = bin_updates.objects.filter(fill_level__range=(71, 100), date=date.today())
    result2 = bin_updates.objects.filter(fill_level__range=(51, 70), date=date.today())
    result3 = bin_updates.objects.filter(fill_level__range=(0, 50), date=date.today())
    dict(form=form)
    data={'result1': result1, 'result2': result2, 'result3': result3, 'form': form}
    return render(request,'analytics.html',data)  

@login_required
def export(request):
    return render_to_response('export.html', context_instance=RequestContext(request))

@login_required
def confirmation(request):
    return render_to_response('confirmation.html', context_instance=RequestContext(request))

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
<<<<<<< HEAD

#def edit(request):
#    if request.method == 'GET':
#        form = ToDoForm()
#    else:
#        form = ToDoForm(request.POST)
#    return render(request,
#                  "todo_app/template.html",
#                  dict(form=form))

=======
	
>>>>>>> fcfcb272d77a31ee8ace091a85de1ea360cc651e
###----------------------------------pip install django-queryset-csv-------------------###
@login_required
def get_csv(request):
    qs = bin_updates.objects.all()
    return djqscsv.render_to_csv_response(qs)


# @login_required
# def get_report(request):
#     html_template = get_template('bins.html')
#     bin_data= bin_record.objects.all()
#     rendered_html = html_template.render(RequestContext(request, {'bin':bin_data})).encode(encoding="UTF-8")
#     pdf_file = HTML(string=rendered_html).write_pdf(stylesheets=[CSS(settings.STATIC_ROOT +  'css/bootstrap.css')])
#     http_response = HttpResponse(pdf_file, content_type='application/pdf')
#     http_response['Content-Disposition'] = 'filename="report.pdf"'
#     return response

# def get_report(request):
#     template = get_template("bins.html")
#     context = {
#      'bin':bin_record.objects.all()
#      }
#     html = template.render(RequestContext(request, context))
#     response = HttpResponse(content_type="application/pdf")
#     weasyprint.HTML(string=html, base_url=request.build_absolute_uri(), url_fetcher=request).write_pdf(response)
#     return response


# def some_view(request):
#     # Create the HttpResponse object with the appropriate CSV header.
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

#     # The data is hard-coded here, but you could load it from a database or
#     # some other source.
#     csv_data = (
#         ('First row', 'Foo', 'Bar', 'Baz'),
#         ('Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"),
#     )

#     t = loader.get_template('my_template_name.txt')
#     c = Context({
#         'data': csv_data,
#     })
#     response.write(t.render(c))
<<<<<<< HEAD
#     return response   
=======
#     return response	
>>>>>>> fcfcb272d77a31ee8ace091a85de1ea360cc651e
