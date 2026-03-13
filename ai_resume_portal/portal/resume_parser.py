"""
Resume Parser Module
Extracts text, skills, education, experience and calculates ATS score
"""
import re
import PyPDF2
from docx import Document
from datetime import datetime

class ResumeParser:
    
    COMMON_SKILLS = [
        'python', 'java', 'javascript', 'typescript', 'react', 'angular', 'vue',
        'django', 'flask', 'fastapi', 'nodejs', 'express', 'spring', 'hibernate',
        'sql', 'postgresql', 'mysql', 'mongodb', 'redis', 'elasticsearch',
        'aws', 'azure', 'gcp', 'docker', 'kubernetes', 'jenkins', 'git',
        'html', 'css', 'bootstrap', 'tailwind', 'sass', 'webpack',
        'tensorflow', 'pytorch', 'scikit-learn', 'pandas', 'numpy',
        'rest api', 'graphql', 'microservices', 'agile', 'scrum',
        'machine learning', 'deep learning', 'nlp', 'computer vision',
        'ci/cd', 'devops', 'linux', 'bash', 'terraform', 'ansible',
        'c++', 'c#', 'php', 'ruby', 'go', 'rust', 'kotlin', 'swift',
        'android', 'ios', 'flutter', 'react native', 'unity',
        'photoshop', 'illustrator', 'figma', 'ui/ux', 'design'
    ]
    
    ACTION_VERBS = [
        'developed', 'managed', 'led', 'created', 'designed', 'implemented',
        'achieved', 'improved', 'increased', 'reduced', 'optimized',
        'built', 'launched', 'delivered', 'coordinated', 'analyzed'
    ]
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = ""
        self.parsed_data = {}
        
    def extract_text(self):
        """Extract text from PDF or DOCX"""
        if self.file_path.endswith('.pdf'):
            return self._extract_from_pdf()
        elif self.file_path.endswith('.docx'):
            return self._extract_from_docx()
        return ""
    
    def _extract_from_pdf(self):
        """Extract text from PDF file"""
        try:
            with open(self.file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = ''
                for page in pdf_reader.pages:
                    text += page.extract_text()
                return text
        except Exception as e:
            print(f"Error extracting PDF: {e}")
            return ""
    
    def _extract_from_docx(self):
        """Extract text from DOCX file"""
        try:
            doc = Document(self.file_path)
            text = '\n'.join([para.text for para in doc.paragraphs])
            return text
        except Exception as e:
            print(f"Error extracting DOCX: {e}")
            return ""
    
    def extract_email(self, text):
        """Extract email address"""
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(email_pattern, text)
        return emails[0] if emails else None
    
    def extract_phone(self, text):
        """Extract phone number"""
        phone_pattern = r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]'
        phones = re.findall(phone_pattern, text)
        return phones[0] if phones else None
    
    def extract_skills(self, text):
        """Extract technical skills"""
        text_lower = text.lower()
        found_skills = []
        
        for skill in self.COMMON_SKILLS:
            if skill in text_lower:
                found_skills.append(skill.title())
        
        return list(set(found_skills))
    
    def extract_education(self, text):
        """Extract education information"""
        education_keywords = ['bachelor', 'master', 'phd', 'b.tech', 'm.tech', 
                             'bca', 'mca', 'mba', 'degree', 'university', 'college']
        
        lines = text.split('\n')
        education_lines = []
        
        for line in lines:
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in education_keywords):
                education_lines.append(line.strip())
        
        return '\n'.join(education_lines[:5]) if education_lines else "Not specified"
    
    def extract_experience(self, text):
        """Extract work experience"""
        experience_keywords = ['experience', 'work history', 'employment', 
                              'professional experience', 'career']
        
        lines = text.split('\n')
        experience_section = []
        capture = False
        
        for line in lines:
            line_lower = line.lower()
            if any(keyword in line_lower for keyword in experience_keywords):
                capture = True
            if capture and line.strip():
                experience_section.append(line.strip())
                if len(experience_section) > 10:
                    break
        
        return '\n'.join(experience_section) if experience_section else "Not specified"
    
    def calculate_ats_score(self, text):
        """Calculate ATS compatibility score (0-100)"""
        score = 0
        text_lower = text.lower()
        
        # Contact Information (20 points)
        if self.extract_email(text):
            score += 10
        if self.extract_phone(text):
            score += 10
        
        # Skills Section (30 points)
        skills = self.extract_skills(text)
        if len(skills) > 0:
            score += min(len(skills) * 2, 30)
        
        # Action Verbs (20 points)
        action_verb_count = sum(1 for verb in self.ACTION_VERBS if verb in text_lower)
        score += min(action_verb_count * 2, 20)
        
        # Education Section (10 points)
        education_keywords = ['bachelor', 'master', 'degree', 'university']
        if any(keyword in text_lower for keyword in education_keywords):
            score += 10
        
        # Experience Section (10 points)
        if 'experience' in text_lower or 'work' in text_lower:
            score += 10
        
        # Length Check (10 points)
        word_count = len(text.split())
        if 300 <= word_count <= 1000:
            score += 10
        elif word_count > 200:
            score += 5
        
        return min(score, 100)
    
    def get_resume_strength(self, text):
        """Calculate resume strength and provide suggestions"""
        text_lower = text.lower()
        strengths = []
        weaknesses = []
        suggestions = []
        
        # Check skills
        skills = self.extract_skills(text)
        if len(skills) >= 8:
            strengths.append("Strong technical skills portfolio")
        elif len(skills) >= 5:
            strengths.append("Good technical skills")
        else:
            weaknesses.append("Limited technical skills mentioned")
            suggestions.append("Add more relevant technical skills")
        
        # Check action verbs
        action_verb_count = sum(1 for verb in self.ACTION_VERBS if verb in text_lower)
        if action_verb_count >= 10:
            strengths.append("Strong use of action verbs")
        else:
            weaknesses.append("Limited use of action verbs")
            suggestions.append("Use more action verbs (developed, managed, led, etc.)")
        
        # Check quantifiable achievements
        numbers = re.findall(r'\d+%|\d+\+', text)
        if len(numbers) >= 3:
            strengths.append("Includes quantifiable achievements")
        else:
            weaknesses.append("Lacks quantifiable achievements")
            suggestions.append("Add measurable achievements with numbers and percentages")
        
        # Check education
        if 'bachelor' in text_lower or 'master' in text_lower or 'degree' in text_lower:
            strengths.append("Education clearly mentioned")
        else:
            weaknesses.append("Education section unclear")
            suggestions.append("Clearly mention your educational qualifications")
        
        # Check certifications
        if 'certification' in text_lower or 'certified' in text_lower:
            strengths.append("Includes certifications")
        else:
            suggestions.append("Add relevant certifications if available")
        
        # Check projects
        if 'project' in text_lower:
            strengths.append("Includes project experience")
        else:
            suggestions.append("Add project descriptions with technologies used")
        
        # Calculate overall strength
        total_checks = len(strengths) + len(weaknesses)
        strength_percentage = int((len(strengths) / total_checks) * 100) if total_checks > 0 else 50
        
        return {
            'strength_percentage': strength_percentage,
            'strengths': strengths,
            'weaknesses': weaknesses,
            'suggestions': suggestions
        }
    
    def parse(self):
        """Main parsing method"""
        self.text = self.extract_text()
        
        self.parsed_data = {
            'text': self.text,
            'email': self.extract_email(self.text),
            'phone': self.extract_phone(self.text),
            'skills': self.extract_skills(self.text),
            'education': self.extract_education(self.text),
            'experience': self.extract_experience(self.text),
            'ats_score': self.calculate_ats_score(self.text),
            'resume_strength': self.get_resume_strength(self.text),
            'word_count': len(self.text.split())
        }
        
        return self.parsed_data
