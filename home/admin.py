from django.contrib import admin
from .models import Room, RoomImage


class RoomImageAdmin(admin.StackedInline):
    model = RoomImage


class RoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('room',)}
    list_display = ('room', 'number_of_guests', 'price', 'tag')
    search_fields = ('room', 'tag', 'created_at')
    list_filter = ('room', 'tag', 'created_at')
    inlines = [RoomImageAdmin]


admin.site.register(Room, RoomAdmin)



