from django.contrib import admin
from crime.models import Inmate, Inmatewatchlist, Offense

class InmateAdmin(admin.ModelAdmin):
    list_display = ('jailid', 'lastname', 'firstname')
    list_filter = ('active','sex','in_time','last_seen')
    search_fields = ('lastname','firstname','offense')

admin.site.register(Inmate, InmateAdmin)

class InmatewatchlistAdmin(admin.ModelAdmin):
    list_display = ('name', 'reason', 'departmentid', 'active')
    list_filter = ('active','departmentid')
    search_fields = ('name',)


admin.site.register(Inmatewatchlist, InmatewatchlistAdmin)

class OffenseAdmin(admin.ModelAdmin):
    list_display = ('warrantno', 'jailid', 'offense')
    list_filter = ('offenselevel',)
    search_fields = ('warrantno','offense')


admin.site.register(Offense, OffenseAdmin)
