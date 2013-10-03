# -*- coding: utf8 -*-
from django.contrib import admin
from app.models import * 


class NewAdmin(admin.ModelAdmin):
	list_display = ('title', 'html_body',)

admin.site.register(New, NewAdmin)
admin.site.register(WatchNew)
admin.site.register(Statement)
admin.site.register(Album)
admin.site.register(Img)

