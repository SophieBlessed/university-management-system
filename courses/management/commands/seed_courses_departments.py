from django.core.management.base import BaseCommand
from courses.models import Course, Department

class Command(BaseCommand):
    help = "Seed the database with sample courses and departments"

    def handle(self, *args, **kwargs):
        departments = [
            "Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering",
            "Business Administration", "Psychology", "Mathematics", "Physics", "Chemistry", "Environmental Science"
        ]

        courses = [
            ("Introduction to Computer Science", "CS101", "Basics of CS", 3),
            ("Data Structures and Algorithms", "CS102", "Algorithms and Data Structures", 4),
            ("Database Systems", "CS103", "Introduction to Databases", 3),
            ("Software Engineering", "CS104", "Software development methodologies", 3),
            ("Operating Systems", "CS105", "OS concepts", 4),
            ("Computer Networks", "CS106", "Networking fundamentals", 3),
            ("Web Development", "CS107", "Building web applications", 3),
            ("Artificial Intelligence", "CS108", "AI concepts", 4),
            ("Machine Learning", "CS109", "ML fundamentals", 4),
            ("Mobile Application Development", "CS110", "Apps for mobile devices", 3),
            ("Cybersecurity Fundamentals", "CS111", "Security basics", 3),
            ("Cloud Computing", "CS112", "Cloud services and architecture", 3),
            ("Human-Computer Interaction", "CS113", "User interface design", 3),
            ("Computer Graphics", "CS114", "Graphics programming", 3),
            ("Programming Languages", "CS115", "Language concepts", 3),
            ("Distributed Systems", "CS116", "Distributed computing", 4),
            ("Big Data Analytics", "CS117", "Data analysis techniques", 3),
            ("Internet of Things (IoT)", "CS118", "IoT technologies", 3),
            ("Digital Signal Processing", "CS119", "DSP fundamentals", 3),
            ("Embedded Systems", "CS120", "Embedded programming", 4),
        ]

        # Seed departments
        for dept_name in departments:
            dept, created = Department.objects.get_or_create(name=dept_name, defaults={'head': 'TBD'})
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created department: {dept_name}"))
            else:
                self.stdout.write(f"Department already exists: {dept_name}")

        # Seed courses
        for name, code, desc, credits in courses:
            course, created = Course.objects.get_or_create(
                code=code,
                defaults={'name': name, 'description': desc, 'credits': credits}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created course: {name}"))
            else:
                self.stdout.write(f"Course already exists: {name}")

        self.stdout.write(self.style.SUCCESS("Seeding complete!"))
