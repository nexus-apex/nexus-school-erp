import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import Student, Classroom, Grade


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['student_count'] = Student.objects.count()
    ctx['student_active'] = Student.objects.filter(status='active').count()
    ctx['student_alumni'] = Student.objects.filter(status='alumni').count()
    ctx['student_transferred'] = Student.objects.filter(status='transferred').count()
    ctx['classroom_count'] = Classroom.objects.count()
    ctx['grade_count'] = Grade.objects.count()
    ctx['grade_a+'] = Grade.objects.filter(grade_letter='a+').count()
    ctx['grade_a'] = Grade.objects.filter(grade_letter='a').count()
    ctx['grade_b+'] = Grade.objects.filter(grade_letter='b+').count()
    ctx['grade_total_marks'] = Grade.objects.aggregate(t=Sum('marks'))['t'] or 0
    ctx['recent'] = Student.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def student_list(request):
    qs = Student.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'student_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def student_create(request):
    if request.method == 'POST':
        obj = Student()
        obj.name = request.POST.get('name', '')
        obj.roll_number = request.POST.get('roll_number', '')
        obj.class_name = request.POST.get('class_name', '')
        obj.section = request.POST.get('section', '')
        obj.parent_name = request.POST.get('parent_name', '')
        obj.phone = request.POST.get('phone', '')
        obj.email = request.POST.get('email', '')
        obj.status = request.POST.get('status', '')
        obj.admission_date = request.POST.get('admission_date') or None
        obj.save()
        return redirect('/students/')
    return render(request, 'student_form.html', {'editing': False})


@login_required
def student_edit(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.roll_number = request.POST.get('roll_number', '')
        obj.class_name = request.POST.get('class_name', '')
        obj.section = request.POST.get('section', '')
        obj.parent_name = request.POST.get('parent_name', '')
        obj.phone = request.POST.get('phone', '')
        obj.email = request.POST.get('email', '')
        obj.status = request.POST.get('status', '')
        obj.admission_date = request.POST.get('admission_date') or None
        obj.save()
        return redirect('/students/')
    return render(request, 'student_form.html', {'record': obj, 'editing': True})


@login_required
def student_delete(request, pk):
    obj = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/students/')


@login_required
def classroom_list(request):
    qs = Classroom.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = ''
    return render(request, 'classroom_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def classroom_create(request):
    if request.method == 'POST':
        obj = Classroom()
        obj.name = request.POST.get('name', '')
        obj.grade = request.POST.get('grade', '')
        obj.section = request.POST.get('section', '')
        obj.teacher = request.POST.get('teacher', '')
        obj.capacity = request.POST.get('capacity') or 0
        obj.students = request.POST.get('students') or 0
        obj.room_number = request.POST.get('room_number', '')
        obj.schedule = request.POST.get('schedule', '')
        obj.save()
        return redirect('/classrooms/')
    return render(request, 'classroom_form.html', {'editing': False})


@login_required
def classroom_edit(request, pk):
    obj = get_object_or_404(Classroom, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.grade = request.POST.get('grade', '')
        obj.section = request.POST.get('section', '')
        obj.teacher = request.POST.get('teacher', '')
        obj.capacity = request.POST.get('capacity') or 0
        obj.students = request.POST.get('students') or 0
        obj.room_number = request.POST.get('room_number', '')
        obj.schedule = request.POST.get('schedule', '')
        obj.save()
        return redirect('/classrooms/')
    return render(request, 'classroom_form.html', {'record': obj, 'editing': True})


@login_required
def classroom_delete(request, pk):
    obj = get_object_or_404(Classroom, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/classrooms/')


@login_required
def grade_list(request):
    qs = Grade.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(student_name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(grade_letter=status_filter)
    return render(request, 'grade_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def grade_create(request):
    if request.method == 'POST':
        obj = Grade()
        obj.student_name = request.POST.get('student_name', '')
        obj.subject = request.POST.get('subject', '')
        obj.marks = request.POST.get('marks') or 0
        obj.max_marks = request.POST.get('max_marks') or 0
        obj.grade_letter = request.POST.get('grade_letter', '')
        obj.exam_type = request.POST.get('exam_type', '')
        obj.term = request.POST.get('term', '')
        obj.save()
        return redirect('/grades/')
    return render(request, 'grade_form.html', {'editing': False})


@login_required
def grade_edit(request, pk):
    obj = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        obj.student_name = request.POST.get('student_name', '')
        obj.subject = request.POST.get('subject', '')
        obj.marks = request.POST.get('marks') or 0
        obj.max_marks = request.POST.get('max_marks') or 0
        obj.grade_letter = request.POST.get('grade_letter', '')
        obj.exam_type = request.POST.get('exam_type', '')
        obj.term = request.POST.get('term', '')
        obj.save()
        return redirect('/grades/')
    return render(request, 'grade_form.html', {'record': obj, 'editing': True})


@login_required
def grade_delete(request, pk):
    obj = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/grades/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['student_count'] = Student.objects.count()
    data['classroom_count'] = Classroom.objects.count()
    data['grade_count'] = Grade.objects.count()
    return JsonResponse(data)
