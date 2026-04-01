from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=255, blank=True, default="")
    class_name = models.CharField(max_length=255, blank=True, default="")
    section = models.CharField(max_length=255, blank=True, default="")
    parent_name = models.CharField(max_length=255, blank=True, default="")
    phone = models.CharField(max_length=255, blank=True, default="")
    email = models.EmailField(blank=True, default="")
    status = models.CharField(max_length=50, choices=[("active", "Active"), ("alumni", "Alumni"), ("transferred", "Transferred")], default="active")
    admission_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Classroom(models.Model):
    name = models.CharField(max_length=255)
    grade = models.CharField(max_length=255, blank=True, default="")
    section = models.CharField(max_length=255, blank=True, default="")
    teacher = models.CharField(max_length=255, blank=True, default="")
    capacity = models.IntegerField(default=0)
    students = models.IntegerField(default=0)
    room_number = models.CharField(max_length=255, blank=True, default="")
    schedule = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class Grade(models.Model):
    student_name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, blank=True, default="")
    marks = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    max_marks = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    grade_letter = models.CharField(max_length=50, choices=[("a+", "A+"), ("a", "A"), ("b+", "B+"), ("b", "B"), ("c+", "C+"), ("c", "C"), ("d", "D"), ("f", "F")], default="a+")
    exam_type = models.CharField(max_length=50, choices=[("unit_test", "Unit Test"), ("mid_term", "Mid Term"), ("final", "Final")], default="unit_test")
    term = models.CharField(max_length=255, blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.student_name
