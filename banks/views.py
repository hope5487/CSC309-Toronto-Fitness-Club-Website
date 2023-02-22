from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, ListView

from banks.forms import BankAddForm, BranchAddForm
from banks.models import Bank, Branch


# Create your views here.
class BankAddFormView(FormView):
    template_name = "bank_add.html"
    form_class = BankAddForm

    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponse('401 UNAUTHORIZED', status=401)
        return FormView.render_to_response(self, context, **response_kwargs)

    def form_valid(self, form):
        bank = Bank.objects.create(**form.cleaned_data, owner=self.request.user)
        return HttpResponseRedirect(reverse_lazy("bank_detail", kwargs = {'bank_id' : bank.id}))

class BankListView(ListView):
    template_name = "bank_list.html"
    model = Bank
    context_object_name = 'banks'

class BankDetailView(DetailView):
    template_name = "bank_detail.html"
    context_object_name = 'bank'

    def get_object(self, queryset=None):
        if not Bank.objects.filter(id=self.kwargs.get('bank_id')).exists():
            raise Http404()
        return Bank.objects.get(id=self.kwargs.get('bank_id'))

class BranchAddFormView(FormView):
    template_name = "branch_add.html"
    form_class = BranchAddForm

    def get_initial(self):
        initial = super(BranchAddFormView, self).get_initial()
        initial.update({'email': "admin@utoronto.ca"})
        return initial

    def render_to_response(self, context, **response_kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponse('401 UNAUTHORIZED', status=401)
        if not Bank.objects.filter(id=self.kwargs.get('bank_id')).exists():
            return HttpResponse('404 NOT FOUND', status=404)
        bank = Bank.objects.get(id=self.kwargs.get('bank_id'))
        if self.request.user != bank.owner:
            return HttpResponse('403 NOT FOUND', status=403)
        return FormView.render_to_response(self, context, **response_kwargs)

    def form_valid(self, form):
        if not self.request.user.is_authenticated:
            return HttpResponse('401 UNAUTHORIZED', status=401)
        if not Bank.objects.filter(id=self.kwargs.get('bank_id')).exists():
            return HttpResponse('404 NOT FOUND', status=404)
        bank = Bank.objects.get(id=self.kwargs.get('bank_id'))
        if self.request.user != bank.owner:
            return HttpResponse('403 NOT FOUND', status=403)
        branch = Branch.objects.create(**form.cleaned_data, bank=bank)
        return HttpResponseRedirect(reverse_lazy("branch_detail", kwargs = {'branch_id' : branch.id}))

def branch_detail_view(request, branch_id):
    if not Branch.objects.filter(id=branch_id).exists():
        return HttpResponse('404 UNAUTHORIZED', status=404)
    branch = Branch.objects.get(id=branch_id)
    return JsonResponse({"id": branch.id, "name": branch.name, "transit_num": branch.transit_num,
                         "address": branch.address, "email": branch.email, "capacity": branch.capacity,
                         "last_modified": branch.last_modified})

def branch_all_view(request, bank_id):
    if not Bank.objects.filter(id=bank_id).exists():
        return HttpResponse('404 UNAUTHORIZED', status=404)
    bank = Bank.objects.get(id=bank_id)
    lst = []
    print(bank.branch_set.all())
    for branch in bank.branch_set.all():
        lst.append({"id": branch.id, "name": branch.name, "transit_num": branch.transit_num,
                         "address": branch.address, "email": branch.email, "capacity": branch.capacity,
                         "last_modified": branch.last_modified})
    return JsonResponse(lst, safe=False)

