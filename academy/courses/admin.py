from django.contrib import admin
from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'created_at']
    search_fields = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


#colocou as expecificações dos cursos na aba e criou um campo de pesquisa


admin.site.register(Course, CourseAdmin)
