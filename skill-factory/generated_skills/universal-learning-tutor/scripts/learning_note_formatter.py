#!/usr/bin/env python3
"""
Learning Note Formatter for Universal Learning Tutor
Formats comprehension notes into standardized template structure
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass
class Concept:
    """Represents a key concept"""
    name: str
    explanation: str


@dataclass
class Framework:
    """Represents a mental model or framework"""
    name: str
    description: str
    when_to_use: str
    how_it_works: str
    example_application: str


@dataclass
class WorkedExample:
    """Represents a worked example"""
    title: str
    problem_scenario: str
    steps: List[tuple[str, str]]  # (action, reasoning) pairs
    solution: str
    key_takeaway: str


@dataclass
class Pitfall:
    """Represents a common pitfall"""
    what_goes_wrong: str
    why_it_happens: str
    how_to_avoid: str


@dataclass
class SpacedRepetitionPrompt:
    """Represents a spaced repetition prompt"""
    day: str  # e.g., "Day 1", "Week 1"
    prompt: str
    type: str  # e.g., "Recall", "Application", "Synthesis", "Teaching"


@dataclass
class SubtopicNotes:
    """Complete learning notes for a subtopic"""
    name: str
    core_definition: str
    key_concepts: List[Concept]
    frameworks: List[Framework]
    worked_examples: List[WorkedExample]
    pitfalls: List[Pitfall]
    expert_insights: List[str]
    spaced_repetition_prompts: List[SpacedRepetitionPrompt]


class LearningNoteFormatter:
    """Formats learning notes into standardized template"""
    
    def __init__(self, topic: str):
        self.topic = topic
        self.subtopics: List[SubtopicNotes] = []
    
    def add_subtopic(self, subtopic: SubtopicNotes) -> None:
        """Add a subtopic's learning notes"""
        self.subtopics.append(subtopic)
    
    def format_worked_example(self, example: WorkedExample) -> str:
        """Format a worked example"""
        output = f"**WORKED EXAMPLE: {example.title}**\n\n"
        output += f"Problem/Scenario: {example.problem_scenario}\n\n"
        
        for idx, (action, reasoning) in enumerate(example.steps, start=1):
            output += f"Step {idx}: {action}\n"
            output += f"*Reasoning: {reasoning}*\n\n"
        
        output += f"**Solution**: {example.solution}\n\n"
        output += f"**Key Takeaway**: {example.key_takeaway}\n"
        
        return output
    
    def format_subtopic_notes(self, subtopic: SubtopicNotes) -> str:
        """Format complete notes for a subtopic"""
        output = f"### Subtopic: {subtopic.name}\n\n"
        
        # Core Definition
        output += "**CORE DEFINITION**\n\n"
        output += f"{subtopic.core_definition}\n\n"
        
        # Key Concepts
        output += "**KEY CONCEPTS**\n\n"
        for concept in subtopic.key_concepts:
            output += f"- **{concept.name}**: {concept.explanation}\n"
        output += "\n"
        
        # Mental Models & Frameworks
        if subtopic.frameworks:
            output += "**MENTAL MODELS & FRAMEWORKS**\n\n"
            for framework in subtopic.frameworks:
                output += f"- **{framework.name}**: {framework.description}\n"
                output += f"  - When to use: {framework.when_to_use}\n"
                output += f"  - How it works: {framework.how_it_works}\n"
                output += f"  - Example application: {framework.example_application}\n\n"
        
        # Worked Examples
        for example in subtopic.worked_examples:
            output += self.format_worked_example(example) + "\n"
        
        # Common Pitfalls
        if subtopic.pitfalls:
            output += "**COMMON PITFALLS & HOW TO AVOID THEM**\n\n"
            for pitfall in subtopic.pitfalls:
                output += f"- **{pitfall.what_goes_wrong}**\n"
                output += f"  - Why it happens: {pitfall.why_it_happens}\n"
                output += f"  - How to avoid: {pitfall.how_to_avoid}\n\n"
        
        # Expert Insights
        if subtopic.expert_insights:
            output += "**EXPERT INSIGHTS**\n\n"
            for idx, insight in enumerate(subtopic.expert_insights, start=1):
                output += f"{idx}. {insight}\n"
            output += "\n"
        
        # Spaced Repetition Prompts
        output += "**SPACED REPETITION PROMPTS**\n\n"
        for prompt in subtopic.spaced_repetition_prompts:
            output += f"- **{prompt.day}** ({prompt.type}): {prompt.prompt}\n"
        output += "\n"
        
        return output
    
    def generate_spaced_repetition_schedule(self, concept_name: str) -> List[SpacedRepetitionPrompt]:
        """Generate default spaced repetition prompts for a concept"""
        return [
            SpacedRepetitionPrompt(
                day="Day 1",
                prompt=f"What is {concept_name}? Define it in your own words.",
                type="Recall"
            ),
            SpacedRepetitionPrompt(
                day="Day 3",
                prompt=f"How would you apply {concept_name} to solve a real-world problem in your field?",
                type="Application"
            ),
            SpacedRepetitionPrompt(
                day="Week 1",
                prompt=f"How does {concept_name} relate to other concepts you've learned in this topic?",
                type="Synthesis"
            ),
            SpacedRepetitionPrompt(
                day="Week 2",
                prompt=f"Explain {concept_name} to someone who has never heard of it. What analogy would you use?",
                type="Teaching"
            )
        ]
    
    def generate_complete_notes(self) -> str:
        """Generate complete learning notes for all subtopics"""
        output = f"# {self.topic} - Comprehensive Learning Notes\n\n"
        output += "## PHASE 3: COMPREHENSION\n\n"
        output += "---\n\n"
        
        for subtopic in self.subtopics:
            output += self.format_subtopic_notes(subtopic)
            output += "---\n\n"
        
        return output
    
    def validate_notes(self) -> List[str]:
        """Validate learning notes completeness"""
        warnings = []
        
        if not self.subtopics:
            warnings.append("No subtopics added to notes")
            return warnings
        
        for subtopic in self.subtopics:
            # Check core components
            if not subtopic.core_definition:
                warnings.append(f"Subtopic '{subtopic.name}' missing core definition")
            
            if not subtopic.key_concepts:
                warnings.append(f"Subtopic '{subtopic.name}' has no key concepts")
            elif len(subtopic.key_concepts) < 3:
                warnings.append(f"Subtopic '{subtopic.name}' has fewer than 3 key concepts")
            
            if not subtopic.worked_examples:
                warnings.append(f"Subtopic '{subtopic.name}' has no worked examples")
            elif len(subtopic.worked_examples) < 2:
                warnings.append(f"Subtopic '{subtopic.name}' should have at least 2 worked examples")
            
            if not subtopic.spaced_repetition_prompts:
                warnings.append(f"Subtopic '{subtopic.name}' missing spaced repetition prompts")
            elif len(subtopic.spaced_repetition_prompts) < 4:
                warnings.append(f"Subtopic '{subtopic.name}' should have 4 spaced repetition prompts (Day 1, 3, Week 1, 2)")
        
        return warnings
    
    def get_word_count(self) -> int:
        """Get approximate word count of generated notes"""
        complete_notes = self.generate_complete_notes()
        return len(complete_notes.split())
    
    def ensure_audio_friendly(self, text: str) -> str:
        """Ensure text is optimized for audio consumption"""
        # Add clear transitions
        audio_text = text.replace("**", "")  # Remove bold markers for audio
        
        # Add verbal cues
        audio_text = audio_text.replace("### Subtopic:", "Next, let's explore")
        audio_text = audio_text.replace("**CORE DEFINITION**", "First, here's the core definition:")
        audio_text = audio_text.replace("**KEY CONCEPTS**", "Now, let's cover the key concepts:")
        audio_text = audio_text.replace("**WORKED EXAMPLE", "Let's work through an example:")
        audio_text = audio_text.replace("**EXPERT INSIGHTS**", "Here are some expert insights:")
        
        return audio_text


def example_usage():
    """Example of how to use the LearningNoteFormatter"""
    
    formatter = LearningNoteFormatter(topic="Introduction to Machine Learning")
    
    # Create example subtopic notes
    subtopic = SubtopicNotes(
        name="Supervised Learning Fundamentals",
        core_definition="Supervised learning is a machine learning paradigm where algorithms learn from labeled training data to make predictions on unseen data. The algorithm learns a mapping function from input features to output labels through exposure to example input-output pairs.",
        key_concepts=[
            Concept(
                name="Training Data",
                explanation="A dataset containing input features and their corresponding correct outputs (labels), used to teach the algorithm the relationship between inputs and outputs."
            ),
            Concept(
                name="Features",
                explanation="Individual measurable properties or characteristics of the data that serve as inputs to the model (e.g., in house price prediction: square footage, number of bedrooms, location)."
            ),
            Concept(
                name="Labels",
                explanation="The correct outputs or target values that the model aims to predict (e.g., in house price prediction: the actual sale price)."
            )
        ],
        frameworks=[
            Framework(
                name="Train-Test Split",
                description="A fundamental approach to validate model performance by dividing data into training and testing sets",
                when_to_use="Always use when building supervised learning models to assess generalization",
                how_it_works="Randomly split data (typically 70-30 or 80-20 ratio), train model on training set, evaluate on test set",
                example_application="When building a spam classifier, use 80% of emails for training and hold out 20% to test accuracy on unseen emails"
            )
        ],
        worked_examples=[
            WorkedExample(
                title="Building a Simple House Price Predictor",
                problem_scenario="Predict house prices using square footage and number of bedrooms",
                steps=[
                    ("Collect labeled training data with features (sq ft, bedrooms) and prices", "Need examples to learn the pattern"),
                    ("Choose linear regression as the algorithm", "Appropriate for continuous value prediction"),
                    ("Train model on training data", "Model learns coefficients for features"),
                    ("Test on unseen houses", "Validate model can generalize")
                ],
                solution="Model learns: Price = 150 × sq_ft + 50000 × bedrooms + base_price",
                key_takeaway="Supervised learning finds mathematical relationships between features and labels from examples"
            )
        ],
        pitfalls=[
            Pitfall(
                what_goes_wrong="Overfitting: Model performs well on training data but poorly on new data",
                why_it_happens="Model memorizes training examples instead of learning general patterns",
                how_to_avoid="Use train-test split, cross-validation, and regularization techniques"
            )
        ],
        expert_insights=[
            "Start simple: Often a basic linear model outperforms complex models on small datasets",
            "Feature quality matters more than model complexity: Spend time engineering good features",
            "Always visualize your data before modeling to understand patterns and potential issues"
        ],
        spaced_repetition_prompts=formatter.generate_spaced_repetition_schedule("supervised learning")
    )
    
    formatter.add_subtopic(subtopic)
    
    # Validate and generate
    warnings = formatter.validate_notes()
    if warnings:
        print("Validation Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
    
    print(f"\nWord Count: {formatter.get_word_count()}")
    
    # Generate markdown
    notes = formatter.generate_complete_notes()
    print("\n" + notes)


if __name__ == "__main__":
    example_usage()

