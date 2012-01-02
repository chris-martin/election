from election.bills.models import Bill, Politician, Supporter
from django.contrib import admin

class SupporterInline(admin.TabularInline):
  model = Supporter
  extra = 10

class BillAdmin(admin.ModelAdmin):
  inlines = [SupporterInline]

admin.site.register(Bill, BillAdmin)

admin.site.register(Politician)

