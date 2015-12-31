from django.contrib import admin

from .models import Podfic


class PodficAdmin(admin.ModelAdmin):
	pass
	
	
admin.site.register(Podfic, PodficAdmin)
