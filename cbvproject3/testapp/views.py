from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Company

class list_info(ListView):
    model = Company
    template_name = 'testapp/list.html'
    context_object_name = 'company'

class detail_info(DetailView):
    model = Company
    template_name = 'testapp/detail.html'
    context_object_name = 'company'

class create_info(CreateView):
    model = Company
    fields =  '__all__'
    template_name = 'testapp/create.html'
    context_object_name = 'company'

class update_info(UpdateView):
    model = Company
    fields = '__all__'
    template_name = 'testapp/update.html'

from django.urls import reverse_lazy
class delete_info(DeleteView):
    model = Company
    fields= '__all__'
    template_name = 'testapp/delete.html'
    success_url = reverse_lazy('delete')
