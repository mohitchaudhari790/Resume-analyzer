"""
Job Recommender Module
Recommends jobs based on resume skills, experience, and education
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class JobRecommender:
    
    def __init__(self, resume_data, jobs_list):
        """
        Initialize with resume data and list of jobs
        resume_data: dict with skills, experience, education
        jobs_list: list of job objects
        """
        self.resume_data = resume_data
        self.jobs_list = jobs_list
        self.recommendations = []
    
    def calculate_skill_match_score(self, resume_skills, job_skills):
        """Calculate skill match score (0-100)"""
        if isinstance(job_skills, str):
            job_skills_list = [s.strip().lower() for s in job_skills.split(',')]
        else:
            job_skills_list = [s.lower() for s in job_skills]
        
        resume_skills_set = set([s.lower() for s in resume_skills])
        job_skills_set = set(job_skills_list)
        
        if not job_skills_set:
            return 0
        
        matched = resume_skills_set.intersection(job_skills_set)
        score = (len(matched) / len(job_skills_set)) * 100
        
        return int(score)
    
    def calculate_text_similarity(self, resume_text, job_description):
        """Calculate text similarity using TF-IDF"""
        try:
            vectorizer = TfidfVectorizer(stop_words='english')
            vectors = vectorizer.fit_transform([resume_text, job_description])
            similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
            return int(similarity * 100)
        except:
            return 0
    
    def calculate_experience_match(self, resume_experience, job_experience_level):
        """Calculate experience level match"""
        # Extract years from resume experience
        import re
        years_pattern = r'(\d+)\s*(?:year|yr)'
        years_found = re.findall(years_pattern, resume_experience.lower())
        
        total_years = sum([int(y) for y in years_found]) if years_found else 0
        
        # Match with job requirements
        if job_experience_level == 'entry' and total_years <= 2:
            return 100
        elif job_experience_level == 'mid' and 2 <= total_years <= 5:
            return 100
        elif job_experience_level == 'senior' and total_years >= 5:
            return 100
        elif job_experience_level == 'entry' and total_years <= 3:
            return 80
        elif job_experience_level == 'mid' and 1 <= total_years <= 7:
            return 80
        else:
            return 50
    
    def calculate_relevance_score(self, job):
        """Calculate overall relevance score for a job"""
        # Skill match (50% weight)
        skill_score = self.calculate_skill_match_score(
            self.resume_data.get('skills', []),
            job.required_skills
        )
        
        # Text similarity (30% weight)
        text_score = self.calculate_text_similarity(
            self.resume_data.get('text', ''),
            job.description
        )
        
        # Experience match (20% weight)
        experience_score = self.calculate_experience_match(
            self.resume_data.get('experience', ''),
            job.experience_level
        )
        
        # Weighted average
        relevance_score = (
            skill_score * 0.5 +
            text_score * 0.3 +
            experience_score * 0.2
        )
        
        return int(relevance_score)
    
    def get_recommendations(self, top_n=10):
        """Get top N job recommendations"""
        recommendations = []
        
        for job in self.jobs_list:
            relevance_score = self.calculate_relevance_score(job)
            
            # Get matched and missing skills
            resume_skills = set([s.lower() for s in self.resume_data.get('skills', [])])
            job_skills = set([s.strip().lower() for s in job.required_skills.split(',')])
            
            matched_skills = list(resume_skills.intersection(job_skills))
            missing_skills = list(job_skills - resume_skills)
            
            recommendations.append({
                'job': job,
                'relevance_score': relevance_score,
                'matched_skills': matched_skills,
                'missing_skills': missing_skills,
                'skill_match_percentage': self.calculate_skill_match_score(
                    self.resume_data.get('skills', []),
                    job.required_skills
                )
            })
        
        # Sort by relevance score
        recommendations.sort(key=lambda x: x['relevance_score'], reverse=True)
        
        return recommendations[:top_n]
    
    def get_recommendations_by_category(self):
        """Get recommendations categorized by match level"""
        all_recommendations = self.get_recommendations(top_n=100)
        
        categorized = {
            'perfect_match': [],  # 80-100%
            'good_match': [],     # 60-79%
            'moderate_match': [], # 40-59%
            'low_match': []       # 0-39%
        }
        
        for rec in all_recommendations:
            score = rec['relevance_score']
            if score >= 80:
                categorized['perfect_match'].append(rec)
            elif score >= 60:
                categorized['good_match'].append(rec)
            elif score >= 40:
                categorized['moderate_match'].append(rec)
            else:
                categorized['low_match'].append(rec)
        
        return categorized
    
    @staticmethod
    def get_career_path_suggestions(current_skills, target_role):
        """Suggest career path based on current skills and target role"""
        career_paths = {
            'backend_developer': {
                'required_skills': ['python', 'django', 'sql', 'rest api', 'docker'],
                'next_steps': ['Learn microservices', 'Master cloud platforms (AWS/Azure)', 'Study system design']
            },
            'frontend_developer': {
                'required_skills': ['javascript', 'react', 'html', 'css', 'typescript'],
                'next_steps': ['Learn state management (Redux)', 'Master responsive design', 'Study web performance']
            },
            'fullstack_developer': {
                'required_skills': ['javascript', 'react', 'nodejs', 'sql', 'rest api'],
                'next_steps': ['Learn DevOps basics', 'Master both frontend and backend', 'Study architecture patterns']
            },
            'data_scientist': {
                'required_skills': ['python', 'machine learning', 'pandas', 'sql', 'statistics'],
                'next_steps': ['Learn deep learning', 'Master data visualization', 'Study big data tools']
            },
            'devops_engineer': {
                'required_skills': ['docker', 'kubernetes', 'ci/cd', 'linux', 'aws'],
                'next_steps': ['Learn infrastructure as code', 'Master monitoring tools', 'Study security practices']
            }
        }
        
        return career_paths.get(target_role.lower().replace(' ', '_'), {
            'required_skills': [],
            'next_steps': ['Research the role requirements', 'Identify skill gaps', 'Create learning plan']
        })
