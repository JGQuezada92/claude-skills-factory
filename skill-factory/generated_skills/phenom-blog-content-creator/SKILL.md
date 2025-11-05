---
name: phenom-blog-content-creator
description: This skill should be used when creating blog posts in Phenom's content style. The skill curates and formats content (either provided by the user or from research skills) into professionally formatted Phenom-style blog posts with exact visual formatting, following Phenom's structure, flow, and stylistic choices. The skill generates both Word (.docx) and Markdown (.md) files matching Phenom's visual style exactly as shown in the provided visual examples.
license: Complete terms in LICENSE.txt
---

# Phenom Blog Content Creator

## Overview

This skill enables the creation of professional blog posts in Phenom's content style. The skill takes content input (either provided directly by the user in Claude chat or passed from research skills) and formats it into Phenom-style blog posts following exact structural patterns, visual formatting, and stylistic guidelines. The skill generates both Microsoft Word (.docx) documents and Markdown (.md) files, ensuring consistent formatting across both output formats that matches Phenom's visual style exactly as demonstrated in the provided visual examples.

## When to Use This Skill

This skill should be invoked when:

- Creating blog posts in Phenom's content style
- Formatting research content into Phenom-style blog posts
- Curating content from multiple sources into a cohesive Phenom blog post
- Generating case study-style blog posts following Phenom's structure
- Creating content that requires Phenom's specific visual formatting and styling
- Producing both Word and Markdown versions of blog content

The skill accepts content input from two sources:
1. **User-provided content**: Content provided directly in Claude chat when invoking the skill
2. **Research skill content**: Content passed from research skills that conduct topic research

## How to Use This Skill

### Step 1: Receive and Analyze Content Input

Accept content input from either:
- User-provided content in the Claude conversation
- Content passed from research skills (structured research data, findings, or raw content)

Analyze the content to identify:
- Key themes and topics
- Main sections or case studies
- Available metrics and quantifiable results
- Quotes or statements from sources
- Related links and resources
- Company or organization information

### Step 2: Reference Phenom Blog Structure

Load and reference `references/phenom-blog-structure.md` to understand:
- Overall blog structure (introduction → TOC → sections → conclusion)
- Case study structure patterns (company context → challenge → strategy → implementation → results → closing)
- Section header hierarchy and formatting
- Writing style guidelines (tone, voice, language patterns)
- Metrics formatting requirements
- Link placement and formatting
- Visual break patterns

### Step 3: Reference Visual Formatting Examples

Load and examine visual formatting examples:
- `assets/phenom-visual-formatting-example-1.png`
- `assets/phenom-visual-formatting-example-2.png`

Identify exact formatting requirements:
- Typography (fonts, sizes, weights)
- Colors (text colors, link colors, accent colors)
- Spacing (paragraph spacing, line spacing, margins)
- Layout (headings, body text, lists, quotes)
- Visual elements (dividers, images, embeds)

### Step 4: Structure Content Following Phenom Patterns

Organize the content following Phenom's blog structure:

**Introduction Section:**
- Create compelling hook question or statement
- Set context with industry trends or challenges
- Reference relevant events or programs (if applicable)
- Include narrative bridge connecting hook to content
- Add call-to-action link if appropriate

**Table of Contents:**
- Create "## In This Article" section
- List all main sections as bullet points with anchor links

**Main Content Sections:**
For each case study or main section:
- Use company/organization name as H2 heading (linked to full case study if available)
- Include opening paragraph with company context and challenge statement
- Add quoted challenge statements with attribution
- Structure strategy/approach as numbered list if applicable
- Detail implementation with bold feature/tool names
- Present results as bulleted list with quantifiable metrics
- Include related links section
- Add closing statement or quote connecting to mission/outcomes

**Conclusion Section:**
- Add call-to-action linking to related content
- Include closing statement tying together themes

### Step 5: Apply Phenom Stylistic Guidelines

Follow Phenom's writing style:
- **Tone**: Professional but approachable, data-driven, outcome-focused
- **Voice**: Third-person, active voice, use direct quotes liberally
- **Language Patterns**: Use patterns like "faces a significant hurdle", "To tackle this challenge head-on", "The impact of these changes"
- **Emphasis**: Bold feature/tool names, italicize emphasis within quotes, use quotes for authenticity
- **Metrics**: Always include specific numbers, percentages, timeframes, before/after comparisons

### Step 6: Generate Word Document

Use `scripts/word_blog_generator.py` to create formatted Word document:

```python
from word_blog_generator import generate_phenom_blog_word

# Structure content into sections
sections = [
    {
        'heading': 'Company Name',
        'content': 'Section content...',
        'quotes': [{'text': 'Quote text', 'attribution': 'Name, Title'}],
        'lists': [
            {'type': 'bullet', 'items': ['Result 1', 'Result 2']},
            {'type': 'numbered', 'items': ['Strategy 1', 'Strategy 2']}
        ],
        'links': [{'text': 'Link Text', 'url': 'https://...', 'bold': True}]
    }
]

output_path = generate_phenom_blog_word(
    title='Blog Post Title',
    introduction='Introduction paragraph...',
    table_of_contents=['Section 1', 'Section 2'],
    sections=sections,
    conclusion='Conclusion paragraph...',
    output_path='Phenom_Blog_Post.docx'
)
```

The script applies:
- Phenom brand colors (primary blue, accent blue, text gray)
- Proper typography (Calibri font, appropriate sizes)
- Correct spacing and layout
- Formatted headings, body text, quotes, lists
- Hyperlinks with proper styling

**Output file naming**: Save the Word document as `Phenom_Blog_Post.docx` (this is the default filename in the script).

### Step 7: Generate Markdown File

Use `scripts/format_phenom_blog.py` to format content as Markdown:

```python
from format_phenom_blog import format_blog_content

formatted_markdown = format_blog_content(
    content=structured_content,
    output_format='markdown',
    visual_examples=['assets/phenom-visual-formatting-example-1.png', 
                     'assets/phenom-visual-formatting-example-2.png']
)
```

The formatter ensures:
- Proper heading hierarchy (H1, H2, H3)
- Bold formatting for features/tools
- Italic formatting for quotes
- Proper list formatting (bulleted and numbered)
- Link formatting with Markdown syntax
- Metrics formatting (bold percentages, numbers)
- Visual breaks (dividers, spacing)

Save the Markdown file as `Phenom_Blog_Post.md`.

### Step 8: Validate Formatting

Before finalizing outputs, validate that formatting matches visual examples:

1. **Visual Comparison**: Compare generated Word document and Markdown against visual examples to ensure:
   - Typography matches (fonts, sizes, weights)
   - Colors match (text colors, link colors)
   - Spacing matches (paragraph spacing, line spacing)
   - Layout matches (headings, body text, lists)

2. **Structure Validation**: Verify that:
   - Introduction section follows pattern
   - Table of contents is present and formatted correctly
   - Main sections follow case study structure
   - All required elements are present (quotes, metrics, links)

3. **Content Validation**: Ensure:
   - All metrics are quantifiable and specific
   - Quotes are properly attributed
   - Links are properly formatted
   - Writing style matches Phenom guidelines

4. **Format Validation**: Use `format_phenom_blog.py` validation:

```python
from format_phenom_blog import PhenomBlogFormatter

formatter = PhenomBlogFormatter()
validation = formatter.validate_formatting(
    content=formatted_content,
    visual_examples=['assets/phenom-visual-formatting-example-1.png',
                     'assets/phenom-visual-formatting-example-2.png']
)

if not validation['valid']:
    # Fix any issues found
    for issue in validation['issues']:
        # Address issue
        pass
```

### Step 9: Finalize and Deliver Outputs

After validation passes:
- Save final Word document: `Phenom_Blog_Post.docx`
- Save final Markdown file: `Phenom_Blog_Post.md`
- Ensure both files are ready for delivery
- Confirm formatting matches visual examples exactly

## Important Considerations

- **Visual Formatting**: The visual formatting examples (PNG files) are the authoritative source for exact formatting requirements. Always refer to them when applying formatting.
- **Structure Consistency**: Follow Phenom's blog structure patterns exactly as documented in `references/phenom-blog-structure.md`. Consistency is critical for maintaining Phenom's brand standards.
- **Content Quality**: Ensure all content is professional, data-driven, and outcome-focused. Include quantifiable metrics wherever possible.
- **Quote Attribution**: Always attribute quotes properly with name and title/role.
- **Link Formatting**: Links should be properly formatted with Markdown syntax in Markdown files and as hyperlinks in Word documents.
- **Output Format**: Generate BOTH Word (.docx) and Markdown (.md) files. Both must match visual styling exactly.
- **Python Scripts**: Use the provided Python scripts for deterministic formatting. Do not attempt to format manually as it may not match visual examples exactly.
- **Content Input Flexibility**: The skill should handle content from various sources (user input, research skills) and adapt it to Phenom's structure while maintaining accuracy.
- **ALWAYS validate all formatting before finalizing deliverables**: Compare outputs against visual examples to ensure exact match.

## Resources

- `scripts/word_blog_generator.py` - Generates formatted Word documents matching Phenom's visual style
- `scripts/format_phenom_blog.py` - Formats content as Markdown following Phenom's style
- `scripts/requirements.txt` - Python dependencies (python-docx)
- `references/phenom-blog-structure.md` - Complete documentation of Phenom's blog structure, patterns, and style guidelines
- `assets/phenom-visual-formatting-example-1.png` - Visual formatting example 1 (authoritative formatting reference)
- `assets/phenom-visual-formatting-example-2.png` - Visual formatting example 2 (authoritative formatting reference)

## Keywords

phenom, blog, content creation, content formatting, blog post, case study, talent management, talent acquisition, HR content, content curation, word document, markdown, visual formatting, brand style


