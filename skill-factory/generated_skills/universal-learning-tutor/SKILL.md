---
name: universal-learning-tutor
description: This skill should be used when learning any new topic across any domain (technical, business, creative, academic). It automates research, priming, and comprehension by aggregating ranked resources, generating knowledge maps with pre-assessment quizzes, and creating standardized learning guides optimized for multi-modal consumption (visual reading and audio conversion).
license: Complete terms in LICENSE.txt
---

# Universal Learning Tutor

## Overview

The Universal Learning Tutor is a domain-agnostic knowledge distillation system that transforms ANY subject into a comprehensive, expert-level learning experience. Whether learning quantum physics, M&A due diligence, Renaissance art history, or machine learning algorithms, this skill provides systematic, structured guidance through three automated phases: Research, Priming, and Comprehension.

The skill synthesizes expert-level knowledge across all domains, mirrors the teaching styles of top practitioners in each field, and possesses an unrivaled ability to distill complex, nuanced topics into clear, understandable components without sacrificing depth or intellectual rigor.

## When to Use This Skill

Use this skill when:
- Learning any new topic from beginner to expert level
- Needing curated, ranked learning resources across the knowledge spectrum
- Requiring structured knowledge maps and pre-assessment quizzes
- Wanting standardized learning materials optimized for both visual and audio consumption
- Converting learning materials to podcasts via NotebookLM
- Building comprehensive study guides with spaced repetition prompts
- Seeking expert-level insights distilled into accessible formats

This skill works across ALL domains: technical fields (AI, engineering, quantum physics), business disciplines (strategy, M&A, finance), creative domains (design, music, art), academic subjects (sciences, humanities, mathematics), and specialized knowledge (legal, medical, trades).

## How to Use This Skill

### Step 1: Receive Topic and Learning Parameters

When invoked, gather these inputs from the learner:
- **Topic**: The specific subject to learn
- **Current knowledge level**: Beginner, Intermediate, or Advanced
- **Learning goal**: What the learner wants to achieve
- **Time available**: Hours per week for learning
- **Preferred format**: Visual, Audio, or Both

### Step 2: Execute Phase 1 - Research (Resource Aggregation)

Aggregate and rank the best learning resources across the knowledge landscape:

1. **Identify resource types**: courses (Coursera, Udemy, MasterClass), articles, videos (YouTube, lectures), papers, books, podcasts, expert blogs
2. **Evaluate quality**: Assess pedagogical value, depth, unique perspectives, and ratings
3. **Rank resources**: Order by composite quality score (use `scripts/resource_ranker.py` for scoring)
4. **Label accessibility**: Mark as FREE or PAID
5. **Annotate each resource**: Explain why it matters, what level it's best for, time investment required

Output: Ranked list of 10-15 resources with complete annotations

### Step 3: Execute Phase 2 - Priming (Orientation)

Generate orientation materials to prepare the learner:

1. **Create Knowledge Architecture**: Build table of contents showing all major subtopics with core concepts and learning outcomes
2. **Generate Pre-Assessment Quiz**: Create 10 multiple-choice questions covering all major concepts (use `scripts/quiz_generator.py`)
3. **Write Subtopic Overviews**: Provide 1-paragraph summaries for each major subtopic
4. **Design Project Prompts**: Suggest 3-5 hands-on projects progressing from beginner to advanced

Output: Complete learning roadmap with knowledge map, quiz, and project prompts

### Step 4: Execute Phase 3 - Comprehension (Deep Learning)

Structure knowledge into comprehensive learning notes:

For each subtopic, provide:
1. **Core Definition**: Clear, quotable definition capturing essence
2. **Key Concepts**: 3-5 concepts explained in accessible language
3. **Mental Models & Frameworks**: Practical frameworks with context, mechanics, and examples
4. **Worked Examples**: 2-3 step-by-step examples with problem, solution, and key takeaway
5. **Common Pitfalls**: What learners get wrong, why it happens, how to avoid
6. **Expert Insights**: 2-3 advanced tips from practitioners
7. **Spaced Repetition Prompts**: Questions for Day 1, Day 3, Week 1, Week 2

Use `scripts/learning_note_formatter.py` to ensure consistent formatting

### Step 5: Optimize for Multi-Modal Consumption

Apply audio-friendly optimizations using `scripts/multimodal_optimizer.py`:

1. **Add audio transition cues**: "First...", "Next...", "Finally..."
2. **Use conversational language**: Write as if speaking to listener
3. **Include clear section breaks**: Ensure podcast segments are obvious
4. **Maintain visual clarity**: Preserve formatting for readers
5. **Verify NotebookLM compatibility**: Test format for podcast conversion

### Step 6: Assemble Complete Learning Guide

Combine all three phases into the standardized output format (see `assets/learning_guide_template.md` for structure):

1. **Executive Summary**: 2-3 paragraphs introducing the topic
2. **Learning Objectives**: Clear, measurable outcomes
3. **Phase 1 Content**: Curated resources with progression path
4. **Phase 2 Content**: Knowledge architecture, quiz, projects
5. **Phase 3 Content**: Comprehensive notes for all subtopics
6. **Next Steps**: Immediate actions, ongoing practice, mastery path
7. **Appendix**: Glossary, formulas, tools, further reading

### Final Step: Validate All Outputs Before Delivery

**CRITICAL: Before finalizing any learning guide, validate all work using BOTH automated and manual verification:**

#### Automated Validation (REQUIRED)

Run the content validation script to check:

```python
python scripts/content_validator.py
```

The script automatically validates:
- ✅ **Resource URLs**: Accessibility, redirects, content type verification
- ✅ **Definitions**: Cross-referenced against Wikipedia and web sources
- ✅ **Quiz Structure**: Question format, answer validity, difficulty balance
- ✅ **Mathematical Calculations**: Expression and result verification

The validation script generates:
- Real-time console report with pass/warning/fail status
- Detailed JSON report saved to `validation_report.json`
- Confidence scores for each validation (0-100%)
- Specific suggestions for fixing issues

**Validation Thresholds:**
- ✅ **90%+ Pass Rate**: Excellent - proceed with manual verification
- ⚠️ **70-89% Pass Rate**: Good - address warnings before delivery
- ⚠️ **50-69% Pass Rate**: Concerning - significant manual review needed
- ❌ **<50% Pass Rate**: Critical - major revisions required

#### Manual Verification (REQUIRED)

Even with automated validation, YOU MUST:

1. **Verify resource accuracy**:
   - Manually visit top 5 resources
   - Confirm they match descriptions
   - Check publication dates for currency
   - Verify author credentials

2. **Validate quiz answers**:
   - Cross-check correct answers with authoritative sources
   - Verify explanations are accurate
   - Test with domain expert if possible

3. **Check content accuracy**:
   - Verify definitions match expert consensus
   - Confirm worked examples are correct
   - Check calculations in mathematical examples
   - Validate frameworks match industry standards

4. **Format compliance**:
   - Confirm output follows standardized template exactly
   - Verify markdown formatting renders correctly
   - Check audio-friendliness by reading aloud

5. **Domain expert review**:
   - For critical topics: Have subject matter expert review
   - For technical content: Verify with practitioners
   - For academic content: Cross-reference with textbooks

**DO NOT proceed to final delivery until:**
- ✅ Automated validation shows 70%+ pass rate
- ✅ All critical failures are resolved
- ✅ Manual verification is complete
- ✅ Domain-specific accuracy is confirmed

## Important Considerations

- **Universal Expertise**: Adapt teaching style to match the subject domain (quantitative, qualitative, creative, technical, etc.)
- **Complexity Distillation**: Always maintain depth while ensuring accessibility - never sacrifice rigor for simplicity
- **Standardized Format**: Use identical structure for every topic to enable rapid familiarization
- **Multi-Modal Optimization**: Every guide must work equally well for visual reading and audio consumption
- **Spaced Repetition**: Include prompts at Day 1, Day 3, Week 1, and Week 2 intervals
- **Expert-Level Depth**: Mirror insights from top practitioners while making content accessible
- **Practical Application**: Always include hands-on projects and worked examples
- **Resource Quality**: Prioritize pedagogical value over popularity
- **ALWAYS validate all resource links and quiz answers before delivery**: Use validation methods to catch errors
- **Verify content accuracy**: Manually check definitions and examples against authoritative sources
- **Check format compliance**: Ensure every guide follows the standardized template exactly

## Resources

### Python Scripts

- `scripts/resource_ranker.py` - Scores and ranks learning resources based on quality, depth, and pedagogical value
- `scripts/quiz_generator.py` - Generates balanced pre-assessment quizzes with plausible distractors
- `scripts/learning_note_formatter.py` - Formats comprehension notes into standardized template structure
- `scripts/multimodal_optimizer.py` - Optimizes output for both visual reading and audio conversion (NotebookLM)
- `scripts/content_validator.py` - **CRITICAL**: Validates accuracy of generated content against authoritative sources

### Reference Documentation

- `references/learning_science_principles.md` - Adult learning theory and cognitive science foundations
- `references/pedagogy_best_practices.md` - Expert teaching methodologies across all disciplines
- `references/output_format_specification.md` - Complete standardized output template with all sections

### Assets

- `assets/learning_guide_template.md` - Reusable template for assembling final learning guides

## Keywords

learning, education, tutoring, knowledge distillation, study guide, learning resources, educational content, pedagogy, teaching, comprehension, spaced repetition, knowledge acquisition, expert knowledge, complexity distillation, multi-modal learning, audio learning, podcast conversion, NotebookLM, visual learning, learning roadmap, knowledge map, pre-assessment, quiz, worked examples, mental models, frameworks, resource curation, learning automation

