#!/usr/bin/env python3
"""
Multimodal Optimizer for Universal Learning Tutor
Optimizes learning content for both visual reading and audio conversion
"""

import re
from typing import List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class AudioTransition:
    """Audio transition phrases for different contexts"""
    section_start: List[str]
    section_end: List[str]
    list_intro: List[str]
    example_intro: List[str]
    emphasis: List[str]


class MultimodalOptimizer:
    """Optimizes content for visual and audio consumption"""
    
    # Audio transition phrases
    TRANSITIONS = AudioTransition(
        section_start=[
            "Let's begin with",
            "Next, we'll explore",
            "Now, let's dive into",
            "Moving on to",
            "First, let's look at"
        ],
        section_end=[
            "That completes",
            "This concludes",
            "We've now covered",
            "That wraps up"
        ],
        list_intro=[
            "Here are the key points:",
            "Let's go through these one by one:",
            "There are several important aspects:",
            "Consider the following:"
        ],
        example_intro=[
            "Let's work through an example:",
            "Here's a practical example:",
            "To illustrate this concept:",
            "Consider this scenario:"
        ],
        emphasis=[
            "This is particularly important:",
            "Pay special attention to this:",
            "Here's the key takeaway:",
            "Remember this:"
        ]
    )
    
    def __init__(self):
        self.audio_cues_added = 0
        self.formatting_changes = 0
    
    def add_audio_transitions(self, content: str) -> str:
        """Add conversational transitions for audio listening"""
        
        # Add transitions for major sections
        content = re.sub(
            r'^## (.*?)$',
            lambda m: f'## {m.group(1)}\n\n*{self.TRANSITIONS.section_start[0]} {m.group(1).lower()}:*\n',
            content,
            flags=re.MULTILINE
        )
        
        # Add transitions before lists
        content = re.sub(
            r'\n(- |\d+\. )',
            lambda m: f'\n\n*Here are the key points:*\n\n{m.group(1)}',
            content,
            count=10  # Limit to avoid over-adding
        )
        
        self.audio_cues_added += content.count('*Here are')
        
        return content
    
    def convert_to_conversational(self, content: str) -> str:
        """Convert formal writing to conversational style for audio"""
        
        conversational_replacements = {
            # Make it sound more spoken
            'Additionally,': 'Also,',
            'Furthermore,': 'Plus,',
            'Therefore,': 'So,',
            'Consequently,': 'As a result,',
            'Subsequently,': 'Then,',
            'In order to': 'To',
            'It is important to note that': 'Note that',
            'It should be emphasized that': 'Remember,',
            
            # Simplify structures
            'Which means that': 'This means',
            'As a result of': 'Because of',
            'Due to the fact that': 'Because',
            'In spite of': 'Despite',
            
            # Add verbal markers
            '**CORE DEFINITION**': "First, here's the core definition:",
            '**KEY CONCEPTS**': "Now, let's cover the key concepts:",
            '**MENTAL MODELS & FRAMEWORKS**': "Next, here are the mental models and frameworks you should know:",
            '**WORKED EXAMPLE': "Let's work through an example:",
            '**COMMON PITFALLS': "Watch out for these common pitfalls:",
            '**EXPERT INSIGHTS**': "Here are some expert insights:",
            '**SPACED REPETITION PROMPTS**': "To help you remember this, here are some questions to revisit:",
        }
        
        for formal, conversational in conversational_replacements.items():
            if formal in content:
                content = content.replace(formal, conversational)
                self.formatting_changes += 1
        
        return content
    
    def optimize_for_notebooklm(self, content: str) -> str:
        """Optimize content specifically for NotebookLM podcast conversion"""
        
        # Remove excessive markdown formatting that doesn't translate well to audio
        # Keep: headers, emphasis for tone, lists
        # Remove: excessive bold, tables, complex formatting
        
        # Convert bold markers to emphasis markers (better for TTS)
        content = re.sub(r'\*\*([^*]+?)\*\*', r'*\1*', content)
        
        # Add pauses (using punctuation) for better audio pacing
        content = re.sub(r'([.!?])\s+([A-Z])', r'\1\n\n\2', content)
        
        # Convert lists to more conversational format
        content = re.sub(
            r'^- \*\*(.*?)\*\*: (.*?)$',
            r'- \1. \2',
            content,
            flags=re.MULTILINE
        )
        
        return content
    
    def add_section_markers(self, content: str) -> str:
        """Add clear section markers for podcast segmentation"""
        
        # Add horizontal rules before major sections for clear breaks
        content = re.sub(
            r'^(## .*?)$',
            r'---\n\n\1',
            content,
            flags=re.MULTILINE
        )
        
        return content
    
    def preserve_visual_formatting(self, content: str) -> str:
        """Ensure visual formatting remains clear for readers"""
        
        # Ensure proper spacing around headers
        content = re.sub(r'(^#{1,3} .*?$)', r'\n\1\n', content, flags=re.MULTILINE)
        
        # Ensure list items have proper spacing
        content = re.sub(r'\n(- |\d+\. )', r'\n\n\1', content)
        
        # Remove excessive blank lines (more than 2)
        content = re.sub(r'\n{4,}', '\n\n\n', content)
        
        return content
    
    def optimize_complete_guide(self, content: str, prioritize: str = 'both') -> str:
        """
        Complete optimization pipeline
        
        Args:
            content: The learning guide content
            prioritize: 'visual', 'audio', or 'both' (default)
        """
        
        if prioritize in ['audio', 'both']:
            content = self.add_audio_transitions(content)
            content = self.convert_to_conversational(content)
            content = self.optimize_for_notebooklm(content)
        
        if prioritize in ['visual', 'both']:
            content = self.preserve_visual_formatting(content)
        
        content = self.add_section_markers(content)
        
        return content
    
    def generate_audio_script(self, content: str) -> str:
        """Generate a separate audio-optimized script from visual content"""
        
        # Create audio version with more explicit verbal cues
        audio_script = content
        
        # Remove markdown entirely for pure audio script
        audio_script = re.sub(r'#{1,6} ', '', audio_script)  # Remove header markers
        audio_script = re.sub(r'\*\*?([^*]+?)\*\*?', r'\1', audio_script)  # Remove emphasis markers
        audio_script = re.sub(r'\[([^\]]+?)\]\([^\)]+?\)', r'\1', audio_script)  # Convert links to plain text
        
        # Add explicit verbal transitions
        audio_script = audio_script.replace('\n## ', '\n\n[NEW SECTION]\n\n')
        audio_script = audio_script.replace('\n### ', '\n\n[SUBSECTION]\n\n')
        audio_script = audio_script.replace('\n---\n', '\n\n[PAUSE]\n\n')
        
        # Add pronunciation guides for technical terms (placeholder for actual implementation)
        # This would include a dictionary of technical term pronunciations
        
        return audio_script
    
    def validate_multimodal_compatibility(self, content: str) -> Dict[str, List[str]]:
        """Validate content works well for both visual and audio"""
        
        issues = {
            'audio': [],
            'visual': [],
            'both': []
        }
        
        # Check for audio issues
        if content.count('**') > 100:
            issues['audio'].append("Excessive bold formatting may not translate well to audio emphasis")
        
        if '|' in content:
            issues['audio'].append("Tables detected - these don't work well in audio format")
        
        # Check for long paragraphs (harder for audio)
        paragraphs = content.split('\n\n')
        long_paragraphs = [p for p in paragraphs if len(p.split()) > 100]
        if long_paragraphs:
            issues['audio'].append(f"Found {len(long_paragraphs)} paragraphs with >100 words - consider breaking up for audio")
        
        # Check for visual issues
        if content.count('\n\n\n') > 10:
            issues['visual'].append("Excessive blank lines may cause visual gaps")
        
        # Check average sentence length
        sentences = re.split(r'[.!?]+', content)
        avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences) if sentences else 0
        if avg_sentence_length > 30:
            issues['both'].append(f"Average sentence length is {avg_sentence_length:.1f} words - consider shorter sentences for both modalities")
        
        return issues
    
    def get_optimization_stats(self) -> Dict:
        """Get statistics about optimizations applied"""
        return {
            'audio_cues_added': self.audio_cues_added,
            'formatting_changes': self.formatting_changes
        }


def example_usage():
    """Example of how to use the MultimodalOptimizer"""
    
    sample_content = """
# Machine Learning Fundamentals

## Overview

Machine learning is a subset of artificial intelligence. **It enables computers to learn from data**. Additionally, it allows systems to improve performance without explicit programming.

## Key Concepts

- **Training Data**: Data used to teach the model
- **Features**: Input variables for prediction
- **Labels**: Output variables to predict

## Example

Consider house price prediction. Features include square footage, bedrooms, location. The label is the sale price.
"""
    
    optimizer = MultimodalOptimizer()
    
    # Optimize for both modalities
    optimized = optimizer.optimize_complete_guide(sample_content, prioritize='both')
    
    print("=== OPTIMIZED CONTENT ===")
    print(optimized)
    print("\n")
    
    # Validate compatibility
    issues = optimizer.validate_multimodal_compatibility(optimized)
    
    if any(issues.values()):
        print("=== COMPATIBILITY ISSUES ===")
        for modality, issue_list in issues.items():
            if issue_list:
                print(f"\n{modality.upper()} Issues:")
                for issue in issue_list:
                    print(f"  - {issue}")
    else:
        print("✓ No compatibility issues found")
    
    # Show statistics
    stats = optimizer.get_optimization_stats()
    print(f"\n=== OPTIMIZATION STATS ===")
    print(f"Audio cues added: {stats['audio_cues_added']}")
    print(f"Formatting changes: {stats['formatting_changes']}")
    
    # Generate separate audio script
    audio_script = optimizer.generate_audio_script(sample_content)
    print("\n=== AUDIO-ONLY SCRIPT ===")
    print(audio_script)


if __name__ == "__main__":
    example_usage()

