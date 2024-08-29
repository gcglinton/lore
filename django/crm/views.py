#from django.shortcuts import render
#from django.template import loader
#from django.http import HttpResponse, Http404


from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Experiment

# Create your views here.


# def index(request):
#     template = loader.get_template("crm/index.html")
#     context = {
#         "experiments": Experiment.objects.all(),
#     }
#     return HttpResponse(template.render(context, request))

# def detail(request, spir):
#     try:
#         experiment = Experiment.objects.get(pk=spir)
#     except Experiment.DoesNotExist:
#         raise Http404("Question does not exist")
    

#     template = loader.get_template("crm/detail.html")
#     context = {
#         "experiment": experiment,
#     }
#     return HttpResponse(template.render(context, request))

class IndexView(generic.ListView):
    #template_name = "crm/index.html"
    context_object_name = "experiments"

    def get_queryset(self):
        """Return the last five published questions."""
        return Experiment.objects.order_by("pk")


class DetailView(generic.DetailView):
    model = Experiment
    #template_name = "crm/detail.html"