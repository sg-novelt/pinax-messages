from django.contrib import admin

from .models import Message, UserThread


@admin.register(UserThread)
class UserThreadAdmin(admin.ModelAdmin):
    list_display = ("thread", "user", "unread", "deleted")
    list_filter = ("unread", "deleted")
    raw_id_fields = ("user",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("thread", "sender", "sent_at")
    list_filter = ("sent_at", "thread")
    raw_id_fields = ("sender",)
