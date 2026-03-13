"""
Skill Gap Analyzer Module
Compares resume skills with job requirements
"""

class SkillGapAnalyzer:
    
    def __init__(self, resume_skills, job_required_skills):
        """
        Initialize with resume skills and job requirements
        resume_skills: list of skills from resume
        job_required_skills: comma-separated string or list of required skills
        """
        self.resume_skills = set([skill.lower().strip() for skill in resume_skills])
        
        if isinstance(job_required_skills, str):
            self.job_skills = set([skill.lower().strip() for skill in job_required_skills.split(',')])
        else:
            self.job_skills = set([skill.lower().strip() for skill in job_required_skills])
    
    def get_matched_skills(self):
        """Get skills that match between resume and job"""
        matched = self.resume_skills.intersection(self.job_skills)
        return sorted(list(matched))
    
    def get_missing_skills(self):
        """Get skills required by job but missing in resume"""
        missing = self.job_skills - self.resume_skills
        return sorted(list(missing))
    
    def get_extra_skills(self):
        """Get skills in resume but not required by job"""
        extra = self.resume_skills - self.job_skills
        return sorted(list(extra))
    
    def calculate_match_percentage(self):
        """Calculate skill match percentage"""
        if not self.job_skills:
            return 0
        
        matched_count = len(self.get_matched_skills())
        total_required = len(self.job_skills)
        
        match_percentage = (matched_count / total_required) * 100
        return int(match_percentage)
    
    def get_skill_gap_report(self):
        """Generate comprehensive skill gap report"""
        matched_skills = self.get_matched_skills()
        missing_skills = self.get_missing_skills()
        extra_skills = self.get_extra_skills()
        match_percentage = self.calculate_match_percentage()
        
        # Determine match level
        if match_percentage >= 80:
            match_level = "Excellent Match"
            recommendation = "You are highly qualified for this role!"
        elif match_percentage >= 60:
            match_level = "Good Match"
            recommendation = "You meet most requirements. Consider learning the missing skills."
        elif match_percentage >= 40:
            match_level = "Moderate Match"
            recommendation = "You have some relevant skills. Focus on acquiring missing skills."
        else:
            match_level = "Low Match"
            recommendation = "Significant skill gap. Consider upskilling before applying."
        
        return {
            'matched_skills': matched_skills,
            'missing_skills': missing_skills,
            'extra_skills': extra_skills,
            'matched_count': len(matched_skills),
            'missing_count': len(missing_skills),
            'total_required': len(self.job_skills),
            'match_percentage': match_percentage,
            'match_level': match_level,
            'recommendation': recommendation
        }
    
    @staticmethod
    def analyze_multiple_jobs(resume_skills, jobs_list):
        """
        Analyze skill gaps for multiple jobs
        jobs_list: list of job objects with required_skills attribute
        """
        results = []
        
        for job in jobs_list:
            analyzer = SkillGapAnalyzer(resume_skills, job.required_skills)
            gap_report = analyzer.get_skill_gap_report()
            
            results.append({
                'job': job,
                'gap_report': gap_report
            })
        
        # Sort by match percentage (highest first)
        results.sort(key=lambda x: x['gap_report']['match_percentage'], reverse=True)
        
        return results
    
    @staticmethod
    def get_learning_priority(missing_skills, industry_demand=None):
        """
        Prioritize missing skills based on industry demand
        """
        # High-demand skills (can be customized based on industry)
        high_priority_skills = [
            'python', 'javascript', 'react', 'aws', 'docker', 'kubernetes',
            'machine learning', 'sql', 'git', 'rest api', 'microservices'
        ]
        
        priority_list = []
        
        for skill in missing_skills:
            priority = "High" if skill.lower() in high_priority_skills else "Medium"
            priority_list.append({
                'skill': skill,
                'priority': priority
            })
        
        # Sort by priority
        priority_list.sort(key=lambda x: x['priority'], reverse=True)
        
        return priority_list
