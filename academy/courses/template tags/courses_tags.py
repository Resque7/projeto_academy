from django.template import Library
from academy.courses.models import Enrollment


register = Library()


@register.inclusion_tag('cursos/templatetags/my_courses.html')
def my_courses(user):
    enrollments = Enrollment.objects.filter(user=user)
    context = {
        'enrollments': enrollments
    }
    return context


@register.assignment_tag
def load_my_courses(user):
    return Enrollment.objects.filter(user=user)
