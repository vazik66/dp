from django.contrib import admin
from .models import Question


# Register your models here.
@admin.register(Question)
class QuestionAdminView(admin.ModelAdmin):
    list_display = [
        "question_text",
        "product",
        "author_name",
        "author_url",
        "question_url",
        "created_at",
        "updated_at",
    ]
