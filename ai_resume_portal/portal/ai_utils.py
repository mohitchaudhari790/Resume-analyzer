import re
import PyPDF2
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

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
    'android', 'ios', 'flutter', 'react native', 'unity', 'unreal',
    'photoshop', 'illustrator', 'figma', 'sketch', 'ui/ux', 'design'
]

def parse_resume(file_path):
    """Parse resume and extract text and skills"""
    text = ""
    
    if file_path.endswith('.pdf'):
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
    elif file_path.endswith('.docx'):
        doc = Document(file_path)
        text = '\n'.join([para.text for para in doc.paragraphs])
    
    text_lower = text.lower()
    detected_skills = [skill for skill in COMMON_SKILLS if skill in text_lower]
    
    return {
        'text': text,
        'skills': list(set(detected_skills))
    }

def analyze_resume(resume):
    """Analyze resume and provide ATS score and suggestions"""
    text = resume.parsed_text.lower()
    
    detected_skills = [skill for skill in COMMON_SKILLS if skill in text]
    
    important_keywords = ['experience', 'project', 'developed', 'managed', 'led', 
                          'achieved', 'implemented', 'designed', 'created']
    keyword_count = sum(1 for kw in important_keywords if kw in text)
    
    ats_score = min(100, len(detected_skills) * 5 + keyword_count * 3)
    
    missing_skills = ['communication', 'teamwork', 'problem solving', 'leadership']
    grammar_suggestions = [
        'Use action verbs at the start of bullet points',
        'Quantify achievements with numbers and metrics',
        'Keep resume concise (1-2 pages)',
        'Use consistent formatting throughout'
    ]
    
    keyword_suggestions = [skill for skill in COMMON_SKILLS[:15] if skill not in detected_skills]
    
    return {
        'ats_score': ats_score,
        'detected_skills': detected_skills[:20],
        'missing_skills': missing_skills,
        'grammar_suggestions': grammar_suggestions,
        'keyword_suggestions': keyword_suggestions[:10]
    }

def calculate_job_match(resume, job):
    """Calculate match percentage between resume and job"""
    resume_text = resume.parsed_text.lower()
    job_skills = job.required_skills.lower()
    
    resume_skills = set([skill for skill in COMMON_SKILLS if skill in resume_text])
    required_skills = set([skill.strip() for skill in job_skills.split(',')])
    
    if not required_skills:
        return 0
    
    matched_skills = resume_skills.intersection(set([s.lower() for s in required_skills]))
    skill_match = (len(matched_skills) / len(required_skills)) * 100 if required_skills else 0
    
    try:
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_text, job.description.lower()])
        similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        text_match = similarity * 100
    except:
        text_match = 0
    
    final_score = int((skill_match * 0.7) + (text_match * 0.3))
    return min(100, final_score)

def get_job_recommendations(resume, all_jobs):
    """Get job recommendations based on resume skills with match scores and missing skills"""
    resume_text = resume.parsed_text.lower()
    resume_skills = set([skill for skill in COMMON_SKILLS if skill in resume_text])
    
    recommendations = []
    
    for job in all_jobs:
        match_score = calculate_job_match(resume, job)
        
        # Get required skills for this job
        job_required_skills = set([skill.strip().lower() for skill in job.required_skills.split(',')])
        
        # Find matched skills
        matched_skills = resume_skills.intersection(job_required_skills)
        
        # Find missing skills
        missing_skills = job_required_skills - resume_skills
        
        recommendations.append({
            'job': job,
            'match_score': match_score,
            'matched_skills': list(matched_skills),
            'missing_skills': list(missing_skills),
            'total_required': len(job_required_skills),
            'total_matched': len(matched_skills)
        })
    
    # Sort by match score (highest first)
    recommendations.sort(key=lambda x: x['match_score'], reverse=True)
    
    return recommendations

def get_missing_skills_for_job(resume, job):
    """Get skills missing from resume for a specific job"""
    resume_text = resume.parsed_text.lower()
    resume_skills = set([skill for skill in COMMON_SKILLS if skill in resume_text])
    
    job_required_skills = set([skill.strip().lower() for skill in job.required_skills.split(',')])
    missing_skills = job_required_skills - resume_skills
    
    return list(missing_skills)
