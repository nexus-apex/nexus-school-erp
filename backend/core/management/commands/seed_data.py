from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Student, Classroom, Grade
from datetime import date, timedelta
import random


class Command(BaseCommand):
    help = 'Seed NexusSchoolERP with demo data'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@nexusschoolerp.com', 'Admin@2024')
            self.stdout.write(self.style.SUCCESS('Admin user created'))

        if Student.objects.count() == 0:
            for i in range(10):
                Student.objects.create(
                    name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    roll_number=f"Sample {i+1}",
                    class_name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    section=f"Sample {i+1}",
                    parent_name=["Rajesh Kumar","Priya Sharma","Amit Patel","Deepa Nair","Vikram Singh","Ananya Reddy","Suresh Iyer","Meera Joshi","Karthik Rao","Fatima Khan"][i],
                    phone=f"+91-98765{43210+i}",
                    email=f"demo{i+1}@example.com",
                    status=random.choice(["active", "alumni", "transferred"]),
                    admission_date=date.today() - timedelta(days=random.randint(0, 90)),
                )
            self.stdout.write(self.style.SUCCESS('10 Student records created'))

        if Classroom.objects.count() == 0:
            for i in range(10):
                Classroom.objects.create(
                    name=f"Sample Classroom {i+1}",
                    grade=f"Sample {i+1}",
                    section=f"Sample {i+1}",
                    teacher=f"Sample {i+1}",
                    capacity=random.randint(1, 100),
                    students=random.randint(1, 100),
                    room_number=f"Sample {i+1}",
                    schedule=f"Sample schedule for record {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Classroom records created'))

        if Grade.objects.count() == 0:
            for i in range(10):
                Grade.objects.create(
                    student_name=f"Sample Grade {i+1}",
                    subject=f"Sample Grade {i+1}",
                    marks=round(random.uniform(1000, 50000), 2),
                    max_marks=round(random.uniform(1000, 50000), 2),
                    grade_letter=random.choice(["a+", "a", "b+", "b", "c+", "c", "d", "f"]),
                    exam_type=random.choice(["unit_test", "mid_term", "final"]),
                    term=f"Sample {i+1}",
                )
            self.stdout.write(self.style.SUCCESS('10 Grade records created'))
