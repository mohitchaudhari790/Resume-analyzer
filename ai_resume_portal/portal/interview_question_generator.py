"""
Interview Question Generator Module
Generates role-specific and skill-based interview questions
"""
import random

class InterviewQuestionGenerator:
    
    # Question bank organized by skill/technology
    QUESTION_BANK = {
        'python': [
            "What is the difference between list and tuple in Python?",
            "Explain Python decorators with an example.",
            "What is the difference between @staticmethod and @classmethod?",
            "How does memory management work in Python?",
            "Explain the concept of generators in Python.",
            "What are Python's magic methods?",
            "Difference between deep copy and shallow copy?",
            "Explain list comprehension with examples.",
            "What is the Global Interpreter Lock (GIL)?",
            "How do you handle exceptions in Python?"
        ],
        'django': [
            "Explain Django ORM and its advantages.",
            "What is the difference between Django's select_related and prefetch_related?",
            "How does Django's middleware work?",
            "Explain Django's MVT architecture.",
            "What are Django signals and when to use them?",
            "How do you optimize Django queries?",
            "Explain Django's authentication system.",
            "What is the purpose of Django migrations?",
            "How do you implement caching in Django?",
            "Explain Django's template inheritance."
        ],
        'javascript': [
            "What is the difference between var, let, and const?",
            "Explain closures in JavaScript.",
            "What is event bubbling and event capturing?",
            "Explain promises and async/await.",
            "What is the difference between == and ===?",
            "Explain the concept of hoisting.",
            "What are arrow functions and how are they different?",
            "Explain the 'this' keyword in JavaScript.",
            "What is the event loop in JavaScript?",
            "Explain prototypal inheritance."
        ],
        'react': [
            "What is the Virtual DOM and how does it work?",
            "Explain the difference between state and props.",
            "What are React Hooks? Explain useState and useEffect.",
            "What is the purpose of keys in React lists?",
            "Explain the component lifecycle methods.",
            "What is Redux and when should you use it?",
            "Explain the concept of Higher-Order Components.",
            "What is the difference between controlled and uncontrolled components?",
            "How do you optimize React application performance?",
            "Explain React Context API."
        ],
        'sql': [
            "What is the difference between INNER JOIN and OUTER JOIN?",
            "Explain database normalization and its types.",
            "What are indexes and how do they improve performance?",
            "Difference between WHERE and HAVING clause?",
            "Explain ACID properties in databases.",
            "What are stored procedures and triggers?",
            "How do you optimize slow SQL queries?",
            "Explain the difference between DELETE, TRUNCATE, and DROP.",
            "What are database transactions?",
            "Explain primary key vs foreign key."
        ],
        'docker': [
            "What is Docker and how is it different from virtual machines?",
            "Explain Docker images and containers.",
            "What is a Dockerfile and how do you write one?",
            "Explain Docker Compose and its use cases.",
            "What are Docker volumes and why are they important?",
            "How do you optimize Docker images?",
            "Explain Docker networking.",
            "What is the difference between CMD and ENTRYPOINT?",
            "How do you handle secrets in Docker?",
            "Explain multi-stage Docker builds."
        ],
        'aws': [
            "What is EC2 and when would you use it?",
            "Explain the difference between S3 and EBS.",
            "What is AWS Lambda and serverless computing?",
            "Explain VPC and its components.",
            "What is the difference between RDS and DynamoDB?",
            "How does AWS IAM work?",
            "Explain AWS CloudFormation.",
            "What is the purpose of AWS CloudWatch?",
            "Explain AWS load balancing options.",
            "What is AWS Auto Scaling?"
        ],
        'machine learning': [
            "What is the difference between supervised and unsupervised learning?",
            "Explain overfitting and underfitting.",
            "What is cross-validation and why is it important?",
            "Explain the bias-variance tradeoff.",
            "What is the difference between classification and regression?",
            "Explain decision trees and random forests.",
            "What is gradient descent?",
            "Explain precision, recall, and F1-score.",
            "What is feature engineering?",
            "Explain the difference between bagging and boosting."
        ],
        'rest api': [
            "What is REST and what are its principles?",
            "Explain HTTP methods (GET, POST, PUT, DELETE, PATCH).",
            "What is the difference between PUT and PATCH?",
            "Explain HTTP status codes (200, 201, 400, 401, 404, 500).",
            "What is API authentication and authorization?",
            "Explain JWT tokens and how they work.",
            "What is API versioning and why is it important?",
            "How do you handle API rate limiting?",
            "Explain CORS and why it's needed.",
            "What is the difference between REST and GraphQL?"
        ],
        'git': [
            "What is the difference between git pull and git fetch?",
            "Explain git merge vs git rebase.",
            "What is a git branch and how do you create one?",
            "How do you resolve merge conflicts?",
            "Explain git stash and when to use it.",
            "What is the difference between git reset and git revert?",
            "Explain git cherry-pick.",
            "What are git hooks?",
            "How do you undo the last commit?",
            "Explain the git workflow (feature branch workflow)."
        ]
    }
    
    # General interview questions by category
    GENERAL_QUESTIONS = {
        'behavioral': [
            "Tell me about yourself and your background.",
            "Why do you want to work for our company?",
            "Describe a challenging project you worked on.",
            "How do you handle tight deadlines?",
            "Tell me about a time you failed and what you learned.",
            "How do you stay updated with new technologies?",
            "Describe your ideal work environment.",
            "How do you handle conflicts in a team?",
            "What are your career goals for the next 5 years?",
            "Why should we hire you?"
        ],
        'problem_solving': [
            "How do you approach debugging a complex issue?",
            "Describe your problem-solving process.",
            "How do you prioritize tasks when working on multiple projects?",
            "Explain a time when you optimized code or improved performance.",
            "How do you handle learning a new technology quickly?",
            "Describe how you would design a scalable system.",
            "How do you ensure code quality?",
            "Explain your approach to testing.",
            "How do you handle technical debt?",
            "Describe a time you had to make a technical decision with limited information."
        ],
        'system_design': [
            "Design a URL shortening service like bit.ly.",
            "How would you design a social media feed?",
            "Design a file storage system like Dropbox.",
            "How would you design a chat application?",
            "Design a rate limiter for an API.",
            "How would you design a notification system?",
            "Design a caching system.",
            "How would you design a search engine?",
            "Design a video streaming platform.",
            "How would you design a distributed task scheduler?"
        ]
    }
    
    def __init__(self, skills, job_role=None):
        """
        Initialize with user skills and optional job role
        skills: list of skills from resume
        job_role: target job role (optional)
        """
        self.skills = [skill.lower().strip() for skill in skills]
        self.job_role = job_role.lower() if job_role else None
    
    def generate_skill_based_questions(self, questions_per_skill=3):
        """Generate questions based on user's skills"""
        questions = []
        
        for skill in self.skills:
            skill_lower = skill.lower()
            if skill_lower in self.QUESTION_BANK:
                skill_questions = random.sample(
                    self.QUESTION_BANK[skill_lower],
                    min(questions_per_skill, len(self.QUESTION_BANK[skill_lower]))
                )
                questions.extend([{
                    'skill': skill.title(),
                    'question': q,
                    'difficulty': 'Medium'
                } for q in skill_questions])
        
        return questions
    
    def generate_role_based_questions(self, job_role=None):
        """Generate questions based on job role"""
        role = (job_role or self.job_role or '').lower()
        questions = []
        
        role_skill_mapping = {
            'backend developer': ['python', 'django', 'sql', 'rest api'],
            'frontend developer': ['javascript', 'react', 'html', 'css'],
            'fullstack developer': ['javascript', 'react', 'python', 'sql', 'rest api'],
            'data scientist': ['python', 'machine learning', 'sql'],
            'devops engineer': ['docker', 'aws', 'linux', 'git'],
            'software engineer': ['python', 'javascript', 'sql', 'git']
        }
        
        relevant_skills = role_skill_mapping.get(role, [])
        
        for skill in relevant_skills:
            if skill in self.QUESTION_BANK:
                skill_questions = random.sample(
                    self.QUESTION_BANK[skill],
                    min(2, len(self.QUESTION_BANK[skill]))
                )
                questions.extend([{
                    'skill': skill.title(),
                    'question': q,
                    'difficulty': 'Medium'
                } for q in skill_questions])
        
        return questions
    
    def generate_general_questions(self, category='behavioral', count=5):
        """Generate general interview questions"""
        if category in self.GENERAL_QUESTIONS:
            selected = random.sample(
                self.GENERAL_QUESTIONS[category],
                min(count, len(self.GENERAL_QUESTIONS[category]))
            )
            return [{
                'category': category.title(),
                'question': q,
                'difficulty': 'General'
            } for q in selected]
        return []
    
    def generate_complete_interview_set(self):
        """Generate a complete set of interview questions"""
        questions = {
            'technical_questions': self.generate_skill_based_questions(questions_per_skill=2),
            'behavioral_questions': self.generate_general_questions('behavioral', count=5),
            'problem_solving_questions': self.generate_general_questions('problem_solving', count=3),
            'system_design_questions': self.generate_general_questions('system_design', count=2)
        }
        
        if self.job_role:
            questions['role_specific_questions'] = self.generate_role_based_questions()
        
        return questions
    
    @staticmethod
    def get_question_tips(skill):
        """Get tips for answering questions about a specific skill"""
        tips = {
            'python': "Focus on practical examples, explain concepts clearly, and mention real-world use cases.",
            'django': "Discuss ORM, middleware, and how you've used Django in projects. Mention performance optimization.",
            'javascript': "Explain with code examples, discuss ES6+ features, and mention browser compatibility.",
            'react': "Discuss component lifecycle, hooks, and state management. Mention performance optimization techniques.",
            'sql': "Write clean queries, explain indexing strategies, and discuss query optimization.",
            'docker': "Explain containerization benefits, discuss real-world usage, and mention orchestration.",
            'aws': "Discuss specific services you've used, cost optimization, and security best practices.",
            'machine learning': "Explain algorithms clearly, discuss when to use each, and mention evaluation metrics.",
            'rest api': "Discuss RESTful principles, proper HTTP methods, and API design best practices.",
            'git': "Explain workflows, branching strategies, and collaboration practices."
        }
        return tips.get(skill.lower(), "Provide clear examples and explain your thought process.")
