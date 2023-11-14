from django.contrib import admin
from .models import Question, Choice
from hijack.contrib.admin import HijackUserAdminMixin

from . import models

admin.site.register(Choice)

admin.site.register(Question)

# @admin.register(models.Post)
# class PostAdmin(HijackUserAdminMixin, admin.ModelAdmin):
#     def get_hijack_user(self, obj):
#         return obj.author  # or any other attribute that points to a user