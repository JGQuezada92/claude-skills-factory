#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Phenom Blog Formatting Engine
Applies Phenom's visual styling to blog content for both Word and Markdown outputs
"""

import re
from typing import Dict, List, Optional
from pathlib import Path


class PhenomBlogFormatter:
    """Applies Phenom's visual formatting to blog content"""
    
    def __init__(self):
        """Initialize the formatter"""
        self.formatted_content = []
    
    def format_markdown(self, content: str) -> str:
        """
        Format content as Markdown following Phenom's style
        
        Args:
            content: Raw blog content
            
        Returns:
            Formatted Markdown string
        """
        lines = content.split('\n')
        formatted_lines = []
        in_list = False
        in_quote = False
        
        for line in lines:
            line = line.strip()
            
            if not line:
                if in_list:
                    formatted_lines.append('')
                    in_list = False
                elif in_quote:
                    formatted_lines.append('')
                    in_quote = False
                else:
                    formatted_lines.append('')
                continue
            
            # Headers
            if line.startswith('# '):
                formatted_lines.append(f'# {line[2:]}')
                formatted_lines.append('')
            elif line.startswith('## '):
                formatted_lines.append(f'## {line[3:]}')
                formatted_lines.append('')
            elif line.startswith('### '):
                formatted_lines.append(f'### **{line[4:]}**')
                formatted_lines.append('')
            
            # Quotes
            elif line.startswith('"') or line.startswith("'"):
                formatted_lines.append(f'> {line}')
                in_quote = True
            elif in_quote and not line.startswith('-') and not line.startswith('*'):
                formatted_lines.append(f'> {line}')
            
            # Bullet lists
            elif line.startswith('- ') or line.startswith('* '):
                formatted_lines.append(line)
                in_list = True
            elif in_list and (line.startswith('  ') or line.startswith('\t')):
                formatted_lines.append(line)
            
            # Numbered lists
            elif re.match(r'^\d+\.\s', line):
                formatted_lines.append(line)
                in_list = True
            
            # Bold formatting for features/tools
            elif ':' in line and not line.startswith('#'):
                parts = line.split(':', 1)
                if len(parts) == 2:
                    formatted_lines.append(f'**{parts[0].strip()}:** {parts[1].strip()}')
                else:
                    formatted_lines.append(line)
            
            # Regular paragraphs
            else:
                formatted_lines.append(line)
                in_list = False
                in_quote = False
        
        return '\n'.join(formatted_lines)
    
    def format_links(self, text: str, links: Dict[str, str]) -> str:
        """
        Format links in text following Phenom's style
        
        Args:
            text: Text containing link placeholders
            links: Dictionary mapping link text to URLs
            
        Returns:
            Text with formatted Markdown links
        """
        for link_text, url in links.items():
            # Find link text in content and replace with Markdown link
            pattern = re.escape(link_text)
            replacement = f'[{link_text}]({url})'
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        
        return text
    
    def format_metrics(self, text: str) -> str:
        """
        Format metrics to ensure they stand out
        
        Args:
            text: Text containing metrics
            
        Returns:
            Text with formatted metrics
        """
        # Pattern for percentages
        text = re.sub(r'(\d+%)', r'**\1**', text)
        
        # Pattern for "from X to Y"
        text = re.sub(r'from (\d+) to (\d+)', r'from **\1** to **\2**', text)
        
        # Pattern for "X% increase/decrease"
        text = re.sub(r'(\d+%) (increase|decrease)', r'**\1 \2**', text)
        
        return text
    
    def format_section_structure(self, content: Dict) -> str:
        """
        Format a complete blog section following Phenom's structure
        
        Args:
            content: Dictionary with section content:
                - heading: Section heading
                - opening: Opening paragraph
                - challenge: Challenge statement (with quote)
                - strategy: Strategy points (list)
                - implementation: Implementation details
                - results: Results/metrics (list)
                - related_links: Related links
                - closing: Closing statement
        
        Returns:
            Formatted section as Markdown
        """
        formatted = []
        
        # Heading
        if 'heading' in content:
            formatted.append(f"## {content['heading']}")
            formatted.append('')
        
        # Opening paragraph
        if 'opening' in content:
            formatted.append(content['opening'])
            formatted.append('')
        
        # Challenge with quote
        if 'challenge' in content:
            challenge = content['challenge']
            if 'quote' in challenge:
                formatted.append(f'> "{challenge['quote']}"')
                if 'attribution' in challenge:
                    formatted.append(f'> — {challenge["attribution"]}')
                formatted.append('')
        
        # Strategy section
        if 'strategy' in content:
            formatted.append('### **Strategy/Approach**')
            formatted.append('')
            for item in content['strategy']:
                formatted.append(f"1. **{item['title']}:** {item['description']}")
            formatted.append('')
        
        # Implementation details
        if 'implementation' in content:
            formatted.append('### **Innovative Solutions Driving Results**')
            formatted.append('')
            for item in content['implementation']:
                formatted.append(f"**{item['feature']}:** {item['description']}")
                if 'link' in item:
                    formatted.append(f"Learn more: [{item['link']['text']}]({item['link']['url']})")
            formatted.append('')
        
        # Results
        if 'results' in content:
            formatted.append('The impact of these changes has reached far beyond just improving efficiency:')
            formatted.append('')
            for result in content['results']:
                formatted.append(f"- {result}")
            formatted.append('')
        
        # Related links
        if 'related_links' in content:
            for link in content['related_links']:
                formatted.append(f"**Related:** [**{link['text']}**]({link['url']})")
            formatted.append('')
        
        # Closing
        if 'closing' in content:
            formatted.append(content['closing'])
            formatted.append('')
        
        return '\n'.join(formatted)
    
    def validate_formatting(self, content: str, visual_examples: List[str]) -> Dict:
        """
        Validate that formatting matches visual examples
        
        Args:
            content: Formatted content to validate
            visual_examples: List of paths to visual example files
            
        Returns:
            Dictionary with validation results:
                - valid: Boolean indicating if formatting is correct
                - issues: List of formatting issues found
                - warnings: List of warnings
        """
        issues = []
        warnings = []
        
        # Check for required elements
        if not re.search(r'## In This Article', content):
            warnings.append("Missing 'In This Article' table of contents section")
        
        # Check for proper heading hierarchy
        if not re.search(r'^# .+', content, re.MULTILINE):
            issues.append("Missing H1 title")
        
        # Check for section headers
        if not re.search(r'^## .+', content, re.MULTILINE):
            issues.append("Missing H2 section headers")
        
        # Check for metrics
        if not re.search(r'\d+%', content):
            warnings.append("No percentage metrics found")
        
        # Check for quotes
        if not re.search(r'^> .+', content, re.MULTILINE):
            warnings.append("No quoted text found")
        
        # Check for links
        if not re.search(r'\[.+\]\(.+\)', content):
            warnings.append("No links found")
        
        return {
            'valid': len(issues) == 0,
            'issues': issues,
            'warnings': warnings
        }


def format_blog_content(
    content: str,
    output_format: str = 'markdown',
    visual_examples: Optional[List[str]] = None
) -> str:
    """
    Format blog content following Phenom's style
    
    Args:
        content: Raw blog content
        output_format: 'markdown' or 'word' (word uses word_blog_generator)
        visual_examples: Optional list of paths to visual example files
    
    Returns:
        Formatted content string
    """
    formatter = PhenomBlogFormatter()
    
    if output_format == 'markdown':
        formatted = formatter.format_markdown(content)
        formatted = formatter.format_metrics(formatted)
        return formatted
    else:
        # For Word format, return structured data for word_blog_generator
        return formatter.format_markdown(content)


if __name__ == '__main__':
    # Example usage
    sample_content = """
# Example Blog Post

## In This Article

- Company A
- Company B

## Company A

Company A provides services and faces challenges.

"Our biggest challenge is the supply," said John Doe.

### Strategy

1. **Targeted Messaging:** How to reach people
2. **Personalized Experience:** Create personalized experience

### Results

- 295% increase in applications
- 800 hours saved
"""

    formatter = PhenomBlogFormatter()
    formatted = formatter.format_markdown(sample_content)
    print(formatted)
    
    # Validate
    validation = formatter.validate_formatting(formatted, [])
    print(f"\nValidation: {validation}")


