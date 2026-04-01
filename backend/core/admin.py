from django.contrib import admin
from .models import Student, Classroom, Grade

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "roll_number", "class_name", "section", "parent_name", "created_at"]
    list_filter = ["status"]
    search_fields = ["name", "roll_number", "class_name"]

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ["name", "grade", "section", "teacher", "capacity", "created_at"]
    search_fields = ["name", "grade", "section"]

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ["student_name", "subject", "marks", "max_marks", "grade_letter", "created_at"]
    list_filter = ["grade_letter", "exam_type"]
    search_fields = ["student_name", "subject", "term"]
