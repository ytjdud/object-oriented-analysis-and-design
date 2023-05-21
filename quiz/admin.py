from django.contrib import admin

# Register your models here.
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
    list_display = ["subject", "create_date"]


admin.site.register(Question, QuestionAdmin)

