from django.contrib import admin
from .models import Language, Student, Mentor, Course


# Register your models here.

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = ('name', 'main_work', 'phone_number', 'level',)
    search_fields = ('language', 'mentor',)

    @admin.display(description='experience')
    def level(self, obj):
        a = 2022 - obj.experience.year
        if a <= 3:
            return 'strong junior'
        if a >= 3:
            return 'middle'


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'data_started', 'student', 'mentor', 'language',)
    search_fields = ('name', )
