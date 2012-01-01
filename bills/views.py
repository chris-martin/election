from django.shortcuts import render_to_response
from election.bills.models import Bill
from django.http import HttpResponse

def index(request):
  bill_list = Bill.objects.all().order_by('-nick')[:5]
  return render_to_response('bills/index.html', {'bill_list': bill_list})

