# Claude Skills Generation Prompt

You are an expert Claude Skills architect tasked with creating professional, production-ready skills based on specific business requirements. This prompt will guide you through generating complete skill packages that follow Anthropic's official standards.

---

## What You're Creating

You will generate **1** Claude Skills for the following business context:

**Business Description:**
Lifelong learner seeking efficient, systematic learning automation across 
any domain. Need to rapidly acquire expert-level knowledge in diverse fields 
ranging from technical subjects (AI agent development, quantum computing) to 
business disciplines (M&A analysis, financial modeling, strategic planning) 
to creative and academic domains. Require consistent, standardized learning 
format that works across all topics for easier cognitive processing and 
retention. Value both depth and accessibility - need complex topics distilled 
without losing rigor.

**Industry:** Education Technology / Personal Learning Automation

**Team Size:** 1 (Personal Use)

**Primary Workflows:** - Rapid topic research and resource curation
- Knowledge synthesis and comprehension
- Multi-modal learning (visual + audio)
- Spaced repetition and long-term retention
- Applied project-based learning

**Overlap Strategy:** overlapping

---

## Understanding Claude Skills Architecture

### Core Principles

Skills are modular, self-contained packages that extend Claude's capabilities through specialized knowledge, workflows, and tools. Think of them as "onboarding guides" that transform Claude from a general-purpose agent into a specialized expert.

### Progressive Disclosure System

Skills use a three-level loading approach:

1. **Metadata (name + description)** - Always in context (~100 words)
   - Must be specific and clear about when to trigger
   - Written in third-person (e.g., "This skill should be used when...")

2. **SKILL.md body** - Loaded when skill triggers (<5k words)
   - Contains core instructions and workflows
   - Written in imperative/infinitive form (verb-first instructions)
   - No second-person pronouns

3. **Bundled resources** - Loaded as needed
   - Scripts, references, and assets
   - Loaded progressively by Claude when required

### Standard Folder Structure

Every skill must follow this structure:

```
skill-name/
├── SKILL.md (REQUIRED)
│   ├── YAML frontmatter (REQUIRED)
│   │   ├── name: skill-name
│   │   ├── description: When to use this skill
│   │   └── license: Complete terms in LICENSE.txt
│   └── Markdown instructions
├── scripts/ (OPTIONAL - only if needed)
│   └── *.py - Executable Python scripts
├── references/ (OPTIONAL)
│   └── *.md - Documentation to load into context as needed
├── assets/ (OPTIONAL)
│   └── Files used in output (templates, images, etc.)
└── TESTING_GUIDE/
    ├── sample_data/
    ├── invocation_prompts.txt
    └── test_scenarios.md
```

---

## When to Include Python Scripts

Include Python scripts in the `scripts/` directory ONLY when:

1. **Deterministic reliability is required** (exact calculations, file format conversions)
2. **Code is repeatedly rewritten** (same logic appears in multiple uses)
3. **Complex operations** (PDF manipulation, image processing, data transformations)
4. **Performance-critical tasks** (processing large files, complex algorithms)

**DO NOT include Python scripts for:**
- Simple text transformations
- Basic data analysis that Claude can do naturally
- Tasks that require flexibility and adaptation
- One-off operations

**Examples of skills needing Python:**
- PDF rotation/manipulation → `scripts/rotate_pdf.py`
- Excel formula automation → `scripts/excel_formatter.py`
- Image processing → `scripts/process_image.py`

**Examples NOT needing Python:**
- Writing reports or summaries
- Creating presentations from text
- Brand guidelines application
- Content strategy development

---

## Required SKILL.md Format

Every SKILL.md must follow this exact structure:

```markdown
---
name: skill-name-here
description: Clear, specific description of when this skill should be used and what it does. Focus on the trigger conditions and use cases. This should be 1-3 sentences written in third person.
license: Complete terms in LICENSE.txt
---

# Skill Name

## Overview

[1-2 paragraph explanation of what this skill provides and its purpose]

## When to Use This Skill

[Specific trigger conditions, use cases, and scenarios where Claude should invoke this skill]

## How to Use This Skill

### Step 1: [First Major Step]

[Detailed instructions using imperative form]

### Step 2: [Second Major Step]

[Continue with procedural instructions]

### Step 3: [Additional Steps as Needed]

[More instructions]

### Final Step: Validate All Outputs Before Delivery

**CRITICAL: Before finalizing any outputs (Excel files, reports, calculations, etc.), validate all work:**

1. **For skills with calculations or data analysis:**
   - Run validation methods (e.g., `validate_output()`) on all analysis results
   - Manually verify key calculations: recalculate percent changes, growth rates, and other metrics
   - Check for logical consistency (e.g., expansion phases should have positive growth trends)
   - Verify formulas in Excel outputs are correct and reference correct cells
   - Cross-check numbers mentioned in reports against source calculations

2. **For skills with Excel/model outputs:**
   - Validate Excel formulas before saving
   - Check for division by zero errors
   - Verify percent change formulas use correct cell references
   - Include a Validation worksheet showing all checks performed

3. **For skills with written reports:**
   - Extract and verify all numerical values mentioned in text
   - Ensure all calculations match source data
   - Check that descriptions match quantitative data (e.g., phase descriptions match trend data)

4. **General validation:**
   - Fix any calculation errors found during validation
   - Correct logical inconsistencies
   - Re-run validation after fixes to ensure errors are resolved
   - Document validation results (errors found, corrections made, confidence levels)

**DO NOT proceed to final delivery until all validation errors are resolved. All warnings should be reviewed and addressed if they indicate potential issues.**

## Important Considerations

[Any critical details, edge cases, constraints, or best practices]

- **ALWAYS validate all calculations and outputs before finalizing deliverables**: Use validation methods to catch calculation errors and logical inconsistencies before delivery
- **Verify calculations manually**: For any metric reported, manually recalculate from source data to ensure accuracy
- **Check for logical consistency**: Ensure descriptions match quantitative data, phases match trends, and related metrics are consistent

## Resources

[Reference any scripts, reference files, or assets included with the skill]
- `scripts/example_script.py` - [What it does]
- `references/schema.md` - [What information it contains]
- `assets/template.xlsx` - [What it's used for]

## Keywords

[Comma-separated list of keywords that might trigger this skill: keyword1, keyword2, keyword3]
```

---

## Writing Style Requirements

**CRITICAL:** All skill content must be written in **imperative/infinitive form**, NOT second person.

### ✅ CORRECT Examples:
- "To accomplish X, do Y"
- "Load the configuration file"
- "Execute the script with these parameters"
- "Consider using this approach when..."
- "Analyze the data by following these steps"

### ❌ INCORRECT Examples:
- "You should do X"
- "If you need to accomplish X"
- "You will find that..."
- "Your next step is to..."

### Metadata Quality Examples

**✅ GOOD description:**
```yaml
description: This skill should be used when analyzing SEC financial filings (10-K, 10-Q) to create comprehensive financial models with automated ratio calculations, trend analysis, and formatted Excel outputs with formulas and charts.
```

**❌ BAD description (too vague):**
```yaml
description: Financial analysis skill for working with data.
```

**❌ BAD description (first person):**
```yaml
description: Use this skill when you want to analyze financial data.
```

---

## Your Task: Generate Skills for These Use Cases

### Use Case 1: Universal Learning Tutor - Domain-Agnostic Knowledge Distillation

**Description:**
A truly universal personal learning tutor that transforms ANY subject into a 
comprehensive, expert-level learning experience. Works across all domains: 
technical fields (AI, quantum physics, engineering), business disciplines 
(strategy, M&A, finance), creative domains (design, music, writing), academic 
subjects (sciences, humanities, mathematics), and specialized knowledge 
(legal, medical, skilled trades).

CORE CAPABILITIES:

UNIVERSAL EXPERTISE: Synthesizes expert-level knowledge across the entire 
knowledge landscape. Mirrors the teaching style, depth, and insights of top 
practitioners in each field. Adapts pedagogical approach to match the nature 
of the subject (quantitative, qualitative, creative, technical, etc.).

COMPLEXITY DISTILLATION: Unrivaled ability to break down nuanced, complex 
topics into clear, understandable components without losing depth or rigor. 
Makes quantum mechanics as accessible as Renaissance art history while 
maintaining intellectual honesty and expert-level precision.

STRUCTURED THREE-PHASE AUTOMATION:

PHASE 1 - RESEARCH: Aggregates and ranks the best learning resources across 
the knowledge spectrum. Evaluates courses (Coursera, Udemy, MasterClass), 
articles, videos, papers, books, podcasts, expert content. Ranks by quality, 
depth, pedagogical value, and unique perspectives. Includes both free and 
paid resources with clear labeling. Outputs ranked resource list with 
annotations explaining why each matters.

PHASE 2 - PRIMING: Generates structured knowledge map showing how the topic 
is organized. Creates pre-assessment quiz (10 questions) to establish baseline 
understanding. Provides 1-paragraph overviews for each major subtopic to 
orient learner. Suggests hands-on project prompts for applied learning. 
Outputs complete learning roadmap with quizzes and orientation materials.

PHASE 3 - COMPREHENSION: Extracts key definitions, mental models, frameworks, 
and worked examples from each subtopic. Structures knowledge into standardized 
learning notes that build from foundational to advanced. Includes spaced 
repetition prompts for long-term retention and active learning exercises. 
Identifies common pitfalls and expert insights. Outputs complete study guide 
ready for immediate use.

STANDARDIZED OUTPUT: Every topic follows identical format regardless of 
domain, enabling rapid familiarization with new content. Output optimized 
for multi-modal consumption: visual reading, audio conversion (NotebookLM 
podcasts), and integration with note-taking systems (Obsidian, Notion).

LEARNING OUTCOMES: Transforms learners from novice to expert in any subject 
through systematic knowledge acquisition, expert-level insight, and complexity 
management. Designed to help learners of any caliber achieve mastery through 
structured, distilled, and actionable learning materials.

OUTPUT FORMAT SPECIFICATION:

Every learning guide follows this exact structure for consistency:

# [TOPIC] - Complete Learning Guide

## Executive Summary
[2-3 paragraphs: What this topic is, why it matters, what you'll achieve]
[Written for audio: conversational, clear transitions]

## Learning Objectives
By mastering this topic, you will:
- Objective 1
- Objective 2
- Objective 3
[Clear, measurable outcomes]

---

## PHASE 1: CURATED LEARNING RESOURCES

### Top-Tier Resources (Ranked by Quality)

**1. [Resource Name]** [FREE/PAID]
- Type: Course / Article / Video / Book / Paper
- Platform: [Where to find it]
- Why This Matters: [1-2 sentence rationale]
- Best For: [Beginner/Intermediate/Advanced]
- Time Investment: [Duration/length]
- Link: [URL]

[Repeat for 10-15 resources]

### Resource Progression Path
- **Foundation (Start Here)**: Resources 1-3
- **Building Depth**: Resources 4-7
- **Advanced Mastery**: Resources 8-10
- **Supplementary Deep Dives**: Resources 11-15

---

## PHASE 2: LEARNING ROADMAP & PRIMING

### Knowledge Architecture (Table of Contents)

**1. Subtopic 1: [Name]**
- Core concepts: Concept A, Concept B, Concept C
- What you'll learn: [1-paragraph overview]
- Why it matters: [Connection to bigger picture]

**2. Subtopic 2: [Name]**
[Repeat structure]

[Continue for all major subtopics]

### Pre-Assessment Quiz
Test your baseline knowledge before diving in:

**Question 1**: [Question text]
a) Option A
b) Option B  
c) Option C
d) Option D

**Answer**: [Letter] - **Explanation**: [Why this is correct and why others aren't]

[Repeat for 10 questions covering all major concepts]

### Hands-On Project Prompts
Apply learning through these projects:

**Project 1**: [Name]
- Goal: [What you'll build/create]
- Skills Practiced: [List]
- Difficulty: [Beginner/Intermediate/Advanced]
- Time: [Estimated hours]

[Repeat for 3-5 projects progressing in complexity]

---

## PHASE 3: COMPREHENSIVE LEARNING NOTES

### Subtopic 1: [Name]

**CORE DEFINITION**
[Clear, quotable definition that captures essence]

**KEY CONCEPTS**
- **Concept 1**: [Explanation in clear language]
- **Concept 2**: [Explanation]
- **Concept 3**: [Explanation]

**MENTAL MODELS & FRAMEWORKS**
- **Framework 1**: [Name and description]
  - When to use: [Context]
  - How it works: [Mechanics]
  - Example application: [Real scenario]

**WORKED EXAMPLE 1: [Title]**
Problem/Scenario: [Setup]
Step 1: [Action + reasoning]
Step 2: [Action + reasoning]
Step 3: [Action + reasoning]
Solution: [Final answer]
Key Takeaway: [What to remember]

**WORKED EXAMPLE 2: [Title]**
[Repeat structure]

**COMMON PITFALLS & HOW TO AVOID THEM**
- **Pitfall 1**: [What people get wrong]
  - Why it happens: [Root cause]
  - How to avoid: [Solution]

**EXPERT INSIGHTS**
[2-3 advanced tips from practitioners]

**SPACED REPETITION PROMPTS**
- Day 1: [Recall question]
- Day 3: [Application question]
- Week 1: [Synthesis question]
- Week 2: [Teaching question - explain to others]

---

[REPEAT ENTIRE STRUCTURE FOR EACH SUBTOPIC]

---

## NEXT STEPS & ACTIVE LEARNING

### Immediate Actions (This Week)
1. [Specific action]
2. [Specific action]
3. [Specific action]

### Ongoing Practice (This Month)
1. [Practice routine]
2. [Practice routine]

### Mastery Path (Next 3-6 Months)
1. [Long-term milestone]
2. [Long-term milestone]

### Community & Further Learning
- [Forums/communities to join]
- [Experts to follow]
- [Adjacent topics to explore]

---

## APPENDIX: QUICK REFERENCE

### Key Terms Glossary
**Term 1**: Definition
**Term 2**: Definition
[Alphabetical list]

### Essential Formulas/Frameworks
[Cheat sheet format]

### Recommended Tools & Resources
[Software, apps, websites relevant to this topic]

### Further Reading
[5-10 advanced resources for going deeper]

---

*Generated by Universal Learning Tutor - Expert knowledge distillation for any subject*

INVOCATION EXAMPLES:

- "I want to learn about [quantum entanglement]. Use the universal-learning-tutor 
  skill to create a complete learning guide. My current knowledge: Beginner. 
  Learning goal: Understand the fundamentals and key experiments. Time available: 
  5 hours per week. Preferred format: Both visual and audio."

- "Teach me [M&A due diligence] using the learning tutor skill. I have 
  intermediate business background. Goal: Lead due diligence projects. 
  Time: 10 hours per week. Format: Visual primarily."

- "I want to master [classical oil painting techniques]. Current level: Complete 
  beginner. Goal: Create realistic portraits. Time: 3 hours per week. 
  Format: Both visual and audio for commute learning."

- "Help me learn [machine learning optimization algorithms]. Advanced mathematics 
  background. Goal: Implement algorithms from scratch. Time: 15 hours per week. 
  Format: Visual with code examples."

- "Teach me [molecular biology of cancer]. Intermediate biology knowledge. 
  Goal: Understand research papers in the field. Time: 8 hours per week. 
  Format: Audio-friendly for podcast conversion."


**Requirements:**
- Python scripts needed: Yes
- Sample data type for testing: text

**What to create:**
- Skill name: `universal-learning-tutor---domain-agnostic-knowledge-distillation`
- Include `scripts/` folder: Yes
- Testing materials: Provide realistic text sample data


---

## For Each Skill, You Must Create:

### 1. Complete Folder Structure
- Create the skill folder with proper naming (lowercase, hyphens)
- Include SKILL.md with proper YAML frontmatter
- Add scripts/ folder ONLY if Python execution is needed
- Add references/ folder if detailed documentation should be separate
- Add assets/ folder if templates or resources are needed for output

### 2. SKILL.md Content
Following the exact format specified above with:
- Proper YAML frontmatter (name, description, license)
- Clear overview and purpose
- Specific trigger conditions
- Step-by-step procedural instructions
- Resource references
- Keywords for discoverability

### 3. Python Scripts (if applicable)
- Well-documented, production-ready code
- Clear docstrings explaining purpose and usage
- Error handling and input validation
- **Output Validation: For skills that generate calculations, reports, or data outputs:**
  - Include validation methods that verify calculation accuracy before delivering outputs
  - Add `validate_output()` methods to analysis/calculation classes that:
    - Recalculate key metrics manually to verify accuracy
    - Check for logical consistency (e.g., growth rates match trends, phases match data)
    - Validate ranges and expected values
    - Cross-check related calculations for consistency
  - Create validation scripts (e.g., `output_validator.py`) for comprehensive validation
  - Return validation results with errors, warnings, and passed checks
- Example usage in comments

### 4. Reference Files (if applicable)
- Detailed documentation that would clutter SKILL.md
- Database schemas, API specs, or domain knowledge
- Examples and use case walkthroughs

### 5. Asset Files (if applicable)
- Templates (Excel, PowerPoint, etc.)
- Images, icons, or design resources
- Boilerplate code or configuration files

### 6. Testing Materials
Create a `TESTING_GUIDE/` folder with:

**a) `sample_data/` folder containing:**
- Realistic sample data files appropriate to the skill type
- For data analysis: CSV or Excel files with realistic business data
- For API skills: JSON response examples
- For document skills: Sample PDFs or documents
- For image skills: Sample images
- Multiple examples covering different scenarios

**b) `invocation_prompts.txt` with:**
Multiple example prompts following this format:
```
Hey Claude—I just added the "[skill-name]" skill. Can you make something amazing with it?

[Additional context or specific request]
---

Hey Claude—I just added the "[skill-name]" skill. Can you [specific task]?

[Sample data reference or additional details]
---

[3-5 different invocation examples covering various use cases]
```

**c) `test_scenarios.md` with:**
```markdown
# Test Scenarios for [Skill Name]

## Basic Scenarios

### Scenario 1: [Name]
**Input:** [What data/prompt to use]
**Expected Output:** [What should be generated]
**Success Criteria:** [How to verify success]

### Scenario 2: [Name]
[Continue...]

## Intermediate Scenarios

### Scenario 3: [Name]
[More complex test case]

## Advanced Scenarios

### Scenario 4: [Name]
[Edge cases and complex situations]

## Edge Cases to Verify

- [Edge case 1]
- [Edge case 2]
- [Edge case 3]

## Common Issues and Solutions

- **Issue:** [Potential problem]
  **Solution:** [How to fix it]
```

---

## Integration and Overlap Guidance

**Strategy:** overlapping


**Since you're creating overlapping skills:**
- Skills may share some functionality and complement each other
- Design skills to work together (e.g., one skill generates data, another visualizes it)
- It's okay for skills to reference or build upon each other
- Consider creating a skill ecosystem where skills can be composed
- Document in each SKILL.md how it works with other skills


---

## Domain-Specific Considerations


### Domain Knowledge to Incorporate

The following domain-specific terminology and knowledge should be incorporated into skills:

- Adult learning theory and cognitive science
- Spaced repetition principles
- Expert pedagogy across all disciplines
- Complexity distillation techniques

Ensure these concepts are properly explained in SKILL.md or reference files.



### Required Integrations

Skills should integrate with or support these tools/platforms:

- NotebookLM (for podcast conversion)
- Note-taking apps (Obsidian, Notion)
- Learning platforms (Coursera, Udemy, YouTube)

Include appropriate instructions for working with these tools in your skills.



### Constraints and Requirements

All skills must adhere to these constraints:

- Must maintain identical output format across ALL topics
- Must be optimized for audio conversion (NotebookLM)
- Must scale from beginner to expert level
- Must distill complexity without losing depth
- Must work for any domain (technical, business, creative, academic)

Consider these constraints when designing workflows and selecting approaches.


---

## Quality Standards

Each skill must meet these standards:

1. **Professional Quality**
   - Production-ready code with error handling
   - Clear, comprehensive documentation
   - Follows all formatting requirements exactly
   - **Output Accuracy**: All calculations and outputs are validated for accuracy before delivery
   - **Validation Mechanisms**: Skills that generate calculations or data outputs include validation methods

2. **Practical Utility**
   - Solves real business problems
   - Includes concrete examples
   - Provides clear value over general Claude usage

3. **Maintainability**
   - Well-organized file structure
   - Clear separation of concerns
   - Easy to update and extend

4. **Testability**
   - Comprehensive testing materials included
   - Multiple realistic scenarios covered
   - Clear success criteria defined

5. **Output Validation**
   - **For calculation/analysis skills**: Include validation methods that verify calculation accuracy
   - **For Excel/model skills**: Validate formulas and calculations before saving
   - **For report skills**: Verify all numerical values match source calculations
   - **Mandatory validation step**: Always include a final validation step in the workflow before delivering outputs
   - **Validation results**: Document validation checks performed and any errors found/corrected

---

## Output Format

For each skill, provide:

1. A clear summary of what the skill does
2. The complete file structure
3. Full contents of SKILL.md
4. Any Python scripts with complete code
5. Reference files if applicable
6. Asset files descriptions
7. Complete testing guide with sample data

Present each skill in a clear, organized manner that can be directly implemented.

---

## Additional Notes

- Keep SKILL.md under 5,000 words
- Use references/ for detailed docs to keep SKILL.md lean
- Scripts should be token-efficient alternatives to repeated generation
- Assets are files used IN outputs, not loaded into context
- Testing materials should be comprehensive enough to validate all functionality
- **Output Validation**: Skills that generate calculations, reports, or data outputs MUST include validation mechanisms:
  - Validation methods in Python scripts (e.g., `validate_output()`)
  - Validation step in workflow instructions
  - Instructions to manually verify key calculations
  - Validation results documentation

---

Begin generating the 1 skills now, following all specifications above.

