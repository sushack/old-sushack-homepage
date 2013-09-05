from django.contrib import admin

from .models import Attendee, Event


class AttendeeAdmin(admin.ModelAdmin):
    list_filter = ['event']
    search_fields = ['name', 'email', 'github_username', 'twitter_username']


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'start', 'current']
    list_editable = ['current']


admin.site.register(Attendee)
admin.site.register(Event, EventAdmin)
