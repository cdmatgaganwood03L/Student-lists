

# Create your views here.
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

# View all students
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

# Create new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

# Update student
def student_update(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

# Delete student
def student_delete(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_delete.html', {'student': student})
