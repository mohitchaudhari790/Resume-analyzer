from django.core.management.base import BaseCommand
from portal.models import Job
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Populate sample jobs for testing'

    def handle(self, *args, **options):
        # Get or create admin user
        admin_user = User.objects.filter(is_staff=True).first()
        if not admin_user:
            admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Created admin user: admin/admin123'))
        
        jobs_data = [
            {
                'title': 'Senior Python Django Developer',
                'company': 'TechCorp',
                'location': 'Remote',
                'salary_min': 120000,
                'salary_max': 160000,
                'required_skills': 'Python, Django, PostgreSQL, REST API, Docker',
                'experience_level': 'senior',
                'description': 'Build scalable web applications using Django and Python. Experience with PostgreSQL and Docker required.',
                'deadline': timezone.now() + timedelta(days=30),
                'posted_by': admin_user,
            },
            {
                'title': 'Frontend React Developer',
                'company': 'InnovateUI',
                'location': 'New York',
                'salary_min': 90000,
                'salary_max': 130000,
                'required_skills': 'React, JavaScript, TypeScript, Tailwind CSS, Next.js',
                'experience_level': 'mid',
                'description': 'Develop modern React applications with TypeScript and Tailwind CSS.',
                'deadline': timezone.now() + timedelta(days=15),
                'posted_by': admin_user,
            },
            {
                'title': 'AI/ML Engineer',
                'company': 'DataSci Labs',
                'location': 'San Francisco',
                'salary_min': 140000,
                'salary_max': 200000,
                'required_skills': 'Python, TensorFlow, PyTorch, scikit-learn, NLP, Computer Vision',
                'experience_level': 'senior',
                'description': 'Work on cutting-edge AI projects using deep learning frameworks.',
                'deadline': timezone.now() + timedelta(days=45),
                'posted_by': admin_user,
            },
            {
                'title': 'Full Stack Developer Intern',
                'company': 'StartupX',
                'location': 'Remote',
                'salary_min': 0,
                'salary_max': 20000,
                'required_skills': 'JavaScript, React, Node.js, MongoDB, Git',
                'experience_level': 'entry',
                'description': 'Internship opportunity for full stack development. Perfect for freshers.',
                'deadline': timezone.now() + timedelta(days=10),
                'posted_by': admin_user,
            },
            {
                'title': 'DevOps Engineer',
                'company': 'CloudScale',
                'location': 'London',
                'salary_min': 110000,
                'salary_max': 150000,
                'required_skills': 'AWS, Kubernetes, Docker, Terraform, CI/CD, Jenkins',
                'experience_level': 'mid',
                'description': 'Manage cloud infrastructure with AWS and Kubernetes.',
                'deadline': timezone.now() + timedelta(days=25),
                'posted_by': admin_user,
            },
            {
                'title': 'Data Scientist',
                'company': 'Analytics Pro',
                'location': 'Boston',
                'salary_min': 100000,
                'salary_max': 140000,
                'required_skills': 'Python, SQL, Machine Learning, Pandas, NumPy, Tableau',
                'experience_level': 'mid',
                'description': 'Analyze data and build predictive models for business insights.',
                'deadline': timezone.now() + timedelta(days=20),
                'posted_by': admin_user,
            },
        ]

        created = 0
        for data in jobs_data:
            job, created_new = Job.objects.get_or_create(
                title=data['title'],
                company=data['company'],
                defaults=data
            )
            if created_new:
                created += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created} new jobs')
        )
