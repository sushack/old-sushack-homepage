from django.contrib import admin

from .models import Attendee, Event, Sponsor


class AttendeeAdmin(admin.ModelAdmin):
    list_filter = ['event']
    list_display = ['name', 'email', 'github_username', 'twitter_username', 'project']
    search_fields = ['name', 'email', 'github_username', 'twitter_username']


class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'start', 'current']
    list_editable = ['current']


admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Sponsor)
