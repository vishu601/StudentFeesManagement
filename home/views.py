from django.shortcuts import render
from students.models import Student

def dashboard(request):
    total_students = Student.objects.count()

    return render(request, "dashboard.html", {
        "total_students": total_students,
    })