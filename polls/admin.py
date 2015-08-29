from django.contrib import admin

# Register your models here.
from polls.models import Question ,Choice

class ChoiceInline(admin.TabularInline):
	model = Choice 

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date')
	inlines = [ChoiceInline]


admin.site.register(Question,QuestionAdmin)
