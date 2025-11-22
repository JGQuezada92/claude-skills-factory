#!/usr/bin/env python3
"""
Quiz Generator for Universal Learning Tutor
Generates balanced pre-assessment quizzes from key concepts
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from enum import Enum
import random


class DifficultyLevel(Enum):
    """Question difficulty levels"""
    EASY = "Easy"
    MEDIUM = "Medium"
    HARD = "Hard"


@dataclass
class QuizOption:
    """Represents a multiple-choice option"""
    letter: str
    text: str
    is_correct: bool


@dataclass
class QuizQuestion:
    """Represents a quiz question"""
    number: int
    question_text: str
    options: List[QuizOption]
    correct_answer: str
    explanation: str
    difficulty: DifficultyLevel
    concept_tested: str


class QuizGenerator:
    """Generates pre-assessment quizzes from key concepts"""
    
    def __init__(self, topic: str):
        self.topic = topic
        self.questions: List[QuizQuestion] = []
    
    def add_question(
        self,
        question_text: str,
        correct_answer_text: str,
        distractor_options: List[str],
        explanation: str,
        difficulty: DifficultyLevel,
        concept_tested: str
    ) -> None:
        """Add a question to the quiz"""
        
        # Create options (1 correct + 3 distractors)
        all_options = [
            (correct_answer_text, True),
            *[(d, False) for d in distractor_options[:3]]
        ]
        
        # Shuffle to randomize correct answer position
        random.shuffle(all_options)
        
        # Assign letters
        letters = ['a', 'b', 'c', 'd']
        options = []
        correct_letter = ''
        
        for idx, (text, is_correct) in enumerate(all_options):
            letter = letters[idx]
            options.append(QuizOption(letter=letter, text=text, is_correct=is_correct))
            if is_correct:
                correct_letter = letter
        
        question = QuizQuestion(
            number=len(self.questions) + 1,
            question_text=question_text,
            options=options,
            correct_answer=correct_letter,
            explanation=explanation,
            difficulty=difficulty,
            concept_tested=concept_tested
        )
        
        self.questions.append(question)
    
    def balance_difficulty(self) -> None:
        """Ensure balanced difficulty distribution (recommended: 40% easy, 40% medium, 20% hard)"""
        easy_count = sum(1 for q in self.questions if q.difficulty == DifficultyLevel.EASY)
        medium_count = sum(1 for q in self.questions if q.difficulty == DifficultyLevel.MEDIUM)
        hard_count = sum(1 for q in self.questions if q.difficulty == DifficultyLevel.HARD)
        
        total = len(self.questions)
        if total == 0:
            return
        
        easy_pct = (easy_count / total) * 100
        medium_pct = (medium_count / total) * 100
        hard_pct = (hard_count / total) * 100
        
        print(f"Difficulty Distribution:")
        print(f"  Easy: {easy_count} ({easy_pct:.1f}%) - Target: 40%")
        print(f"  Medium: {medium_count} ({medium_pct:.1f}%) - Target: 40%")
        print(f"  Hard: {hard_count} ({hard_pct:.1f}%) - Target: 20%")
        
        # Recommend adjustments if needed
        if easy_pct < 30 or easy_pct > 50:
            print(f"  ⚠️ Consider adjusting Easy questions")
        if medium_pct < 30 or medium_pct > 50:
            print(f"  ⚠️ Consider adjusting Medium questions")
        if hard_pct < 10 or hard_pct > 30:
            print(f"  ⚠️ Consider adjusting Hard questions")
    
    def validate_quiz(self) -> List[str]:
        """Validate quiz quality and return warnings"""
        warnings = []
        
        if len(self.questions) < 10:
            warnings.append(f"Quiz has only {len(self.questions)} questions. Recommend 10 questions.")
        
        if len(self.questions) > 15:
            warnings.append(f"Quiz has {len(self.questions)} questions. May be too long for pre-assessment.")
        
        # Check for duplicate concepts
        concepts_tested = [q.concept_tested for q in self.questions]
        if len(concepts_tested) != len(set(concepts_tested)):
            warnings.append("Multiple questions test the same concept. Consider broader coverage.")
        
        # Check that all questions have explanations
        for q in self.questions:
            if not q.explanation or len(q.explanation) < 20:
                warnings.append(f"Question {q.number} has insufficient explanation.")
        
        return warnings
    
    def format_question_markdown(self, question: QuizQuestion) -> str:
        """Format a single question for markdown output"""
        output = f"**Question {question.number}**: {question.question_text}\n"
        
        for option in question.options:
            output += f"{option.letter}) {option.text}\n"
        
        output += f"\n**Answer**: {question.correct_answer.upper()} - **Explanation**: {question.explanation}\n\n"
        output += f"*Difficulty: {question.difficulty.value} | Concept: {question.concept_tested}*\n"
        
        return output
    
    def generate_quiz_markdown(self) -> str:
        """Generate complete quiz in markdown format"""
        output = f"# {self.topic} - Pre-Assessment Quiz\n\n"
        output += "Test your baseline knowledge before diving in:\n\n"
        output += "---\n\n"
        
        for question in self.questions:
            output += self.format_question_markdown(question)
            output += "\n---\n\n"
        
        return output
    
    def generate_answer_key(self) -> str:
        """Generate quick answer key"""
        output = "## Answer Key\n\n"
        
        for question in self.questions:
            output += f"{question.number}. {question.correct_answer.upper()} - {question.concept_tested}\n"
        
        return output
    
    def get_statistics(self) -> Dict:
        """Get quiz statistics"""
        return {
            'total_questions': len(self.questions),
            'difficulty_distribution': {
                'easy': sum(1 for q in self.questions if q.difficulty == DifficultyLevel.EASY),
                'medium': sum(1 for q in self.questions if q.difficulty == DifficultyLevel.MEDIUM),
                'hard': sum(1 for q in self.questions if q.difficulty == DifficultyLevel.HARD)
            },
            'concepts_covered': list(set(q.concept_tested for q in self.questions)),
            'avg_explanation_length': sum(len(q.explanation) for q in self.questions) / len(self.questions) if self.questions else 0
        }


def example_usage():
    """Example of how to use the QuizGenerator"""
    
    # Create quiz for Machine Learning topic
    quiz = QuizGenerator(topic="Introduction to Machine Learning")
    
    # Add questions
    quiz.add_question(
        question_text="What is the primary difference between supervised and unsupervised learning?",
        correct_answer_text="Supervised learning uses labeled data, while unsupervised learning works with unlabeled data",
        distractor_options=[
            "Supervised learning is faster to train than unsupervised learning",
            "Unsupervised learning always produces more accurate models",
            "Supervised learning can only handle numerical data"
        ],
        explanation="The key distinction is that supervised learning algorithms learn from labeled examples (input-output pairs), while unsupervised learning algorithms find patterns in data without predefined labels.",
        difficulty=DifficultyLevel.EASY,
        concept_tested="Learning paradigms"
    )
    
    quiz.add_question(
        question_text="Which algorithm would be most appropriate for predicting house prices based on features like size, location, and age?",
        correct_answer_text="Linear Regression",
        distractor_options=[
            "K-Means Clustering",
            "Principal Component Analysis",
            "Apriori Algorithm"
        ],
        explanation="Linear regression is a supervised learning algorithm designed for continuous value prediction, making it ideal for predicting house prices. The other options are unsupervised learning or association rule mining techniques.",
        difficulty=DifficultyLevel.MEDIUM,
        concept_tested="Algorithm selection"
    )
    
    # Validate and generate
    warnings = quiz.validate_quiz()
    if warnings:
        print("Validation Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
    
    quiz.balance_difficulty()
    
    # Generate markdown
    markdown = quiz.generate_quiz_markdown()
    print("\n" + markdown)
    
    # Show statistics
    stats = quiz.get_statistics()
    print(f"\nQuiz Statistics: {stats}")


if __name__ == "__main__":
    example_usage()

