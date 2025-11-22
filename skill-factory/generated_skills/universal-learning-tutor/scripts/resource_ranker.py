#!/usr/bin/env python3
"""
Resource Ranker for Universal Learning Tutor
Scores and ranks learning resources based on multiple quality criteria
"""

from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum


class ResourceType(Enum):
    """Types of learning resources"""
    COURSE = "Course"
    ARTICLE = "Article"
    VIDEO = "Video"
    BOOK = "Book"
    PAPER = "Paper"
    PODCAST = "Podcast"
    INTERACTIVE = "Interactive"


class AccessLevel(Enum):
    """Resource accessibility"""
    FREE = "FREE"
    PAID = "PAID"
    FREEMIUM = "FREEMIUM"


class DifficultyLevel(Enum):
    """Target audience difficulty level"""
    BEGINNER = "Beginner"
    INTERMEDIATE = "Intermediate"
    ADVANCED = "Advanced"
    ALL_LEVELS = "All Levels"


@dataclass
class LearningResource:
    """Represents a learning resource with metadata"""
    name: str
    type: ResourceType
    platform: str
    url: str
    access_level: AccessLevel
    difficulty: DifficultyLevel
    time_investment: str  # e.g., "10 hours", "300 pages", "30 minutes"
    description: str
    
    # Quality metrics (0-10 scale)
    content_quality: float = 0.0
    pedagogical_value: float = 0.0
    depth: float = 0.0
    uniqueness: float = 0.0
    user_ratings: float = 0.0
    
    # Calculated
    composite_score: float = 0.0
    rank: int = 0


class ResourceRanker:
    """Ranks learning resources based on quality criteria"""
    
    # Weights for composite score calculation
    WEIGHTS = {
        'content_quality': 0.25,
        'pedagogical_value': 0.30,
        'depth': 0.20,
        'uniqueness': 0.15,
        'user_ratings': 0.10
    }
    
    def __init__(self):
        self.resources: List[LearningResource] = []
    
    def add_resource(self, resource: LearningResource) -> None:
        """Add a resource to the ranking pool"""
        self.resources.append(resource)
    
    def calculate_composite_score(self, resource: LearningResource) -> float:
        """Calculate weighted composite quality score"""
        score = (
            resource.content_quality * self.WEIGHTS['content_quality'] +
            resource.pedagogical_value * self.WEIGHTS['pedagogical_value'] +
            resource.depth * self.WEIGHTS['depth'] +
            resource.uniqueness * self.WEIGHTS['uniqueness'] +
            resource.user_ratings * self.WEIGHTS['user_ratings']
        )
        return round(score, 2)
    
    def rank_resources(self) -> List[LearningResource]:
        """Calculate scores and rank all resources"""
        # Calculate composite scores
        for resource in self.resources:
            resource.composite_score = self.calculate_composite_score(resource)
        
        # Sort by composite score (descending)
        sorted_resources = sorted(
            self.resources,
            key=lambda r: r.composite_score,
            reverse=True
        )
        
        # Assign ranks
        for idx, resource in enumerate(sorted_resources, start=1):
            resource.rank = idx
        
        return sorted_resources
    
    def get_top_resources(self, n: int = 15) -> List[LearningResource]:
        """Get top N ranked resources"""
        ranked = self.rank_resources()
        return ranked[:n]
    
    def categorize_by_progression(self, resources: List[LearningResource]) -> Dict[str, List[LearningResource]]:
        """Categorize resources into learning progression paths"""
        categories = {
            'foundation': [],  # Top 3 for beginners
            'building_depth': [],  # Next 4 for intermediate
            'advanced_mastery': [],  # Next 3 for advanced
            'supplementary': []  # Remaining for deep dives
        }
        
        for idx, resource in enumerate(resources):
            if idx < 3:
                categories['foundation'].append(resource)
            elif idx < 7:
                categories['building_depth'].append(resource)
            elif idx < 10:
                categories['advanced_mastery'].append(resource)
            else:
                categories['supplementary'].append(resource)
        
        return categories
    
    def format_resource_markdown(self, resource: LearningResource) -> str:
        """Format a resource for markdown output"""
        return f"""**{resource.rank}. {resource.name}** [{resource.access_level.value}]
- Type: {resource.type.value}
- Platform: {resource.platform}
- Why This Matters: {resource.description}
- Best For: {resource.difficulty.value}
- Time Investment: {resource.time_investment}
- Link: {resource.url}
- Quality Score: {resource.composite_score}/10.0
"""
    
    def generate_ranked_list_markdown(self, top_n: int = 15) -> str:
        """Generate complete ranked resource list in markdown"""
        top_resources = self.get_top_resources(top_n)
        
        output = "### Top-Tier Resources (Ranked by Quality)\n\n"
        
        for resource in top_resources:
            output += self.format_resource_markdown(resource) + "\n"
        
        # Add progression path
        categories = self.categorize_by_progression(top_resources)
        
        output += "\n### Resource Progression Path\n\n"
        output += f"- **Foundation (Start Here)**: Resources 1-{len(categories['foundation'])}\n"
        output += f"- **Building Depth**: Resources {len(categories['foundation'])+1}-{len(categories['foundation'])+len(categories['building_depth'])}\n"
        output += f"- **Advanced Mastery**: Resources {len(categories['foundation'])+len(categories['building_depth'])+1}-{len(categories['foundation'])+len(categories['building_depth'])+len(categories['advanced_mastery'])}\n"
        
        if categories['supplementary']:
            output += f"- **Supplementary Deep Dives**: Resources {len(categories['foundation'])+len(categories['building_depth'])+len(categories['advanced_mastery'])+1}-{top_n}\n"
        
        return output


def example_usage():
    """Example of how to use the ResourceRanker"""
    ranker = ResourceRanker()
    
    # Example: Adding resources for "Machine Learning" topic
    ranker.add_resource(LearningResource(
        name="Introduction to Machine Learning (Stanford)",
        type=ResourceType.COURSE,
        platform="Coursera",
        url="https://www.coursera.org/learn/machine-learning",
        access_level=AccessLevel.FREE,
        difficulty=DifficultyLevel.BEGINNER,
        time_investment="60 hours",
        description="Foundational course by Andrew Ng covering core ML algorithms and theory",
        content_quality=9.5,
        pedagogical_value=10.0,
        depth=8.5,
        uniqueness=7.0,
        user_ratings=9.8
    ))
    
    ranker.add_resource(LearningResource(
        name="Deep Learning Specialization",
        type=ResourceType.COURSE,
        platform="Coursera",
        url="https://www.coursera.org/specializations/deep-learning",
        access_level=AccessLevel.PAID,
        difficulty=DifficultyLevel.INTERMEDIATE,
        time_investment="120 hours",
        description="Comprehensive deep learning curriculum covering neural networks, CNNs, RNNs, and more",
        content_quality=9.8,
        pedagogical_value=9.5,
        depth=9.5,
        uniqueness=8.5,
        user_ratings=9.7
    ))
    
    # Generate output
    markdown_output = ranker.generate_ranked_list_markdown(top_n=10)
    print(markdown_output)


if __name__ == "__main__":
    example_usage()

