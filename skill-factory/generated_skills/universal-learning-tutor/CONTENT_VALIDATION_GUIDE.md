# Content Validation Guide

## Overview

The Universal Learning Tutor includes an extensive **Content Validation System** that automatically verifies the accuracy, accessibility, and quality of generated learning materials. This guide explains how to use the validation system effectively.

## Why Validation Matters

AI-generated content can contain:
- ❌ Broken or outdated URLs
- ❌ Incorrect definitions
- ❌ Wrong quiz answers
- ❌ Mathematical errors
- ❌ Outdated information

**The validation system helps catch these issues before you invest time learning from incorrect content.**

---

## Installation

### Required Dependencies

```bash
# Core dependencies (required)
pip install requests

# Optional but highly recommended
pip install beautifulsoup4  # For web scraping
pip install wikipedia       # For definition validation
```

### Verify Installation

```bash
cd scripts
python content_validator.py
```

If libraries are missing, you'll see warnings but the script will still run with reduced functionality.

---

## How to Use the Validator

### Method 1: Validate Generated Learning Guide (Recommended)

After generating a learning guide, structure it as JSON and validate:

```python
from content_validator import ContentValidator
import json

# Load your generated learning guide
guide_data = {
    'topic': 'Machine Learning Fundamentals',
    
    'resources': [
        {
            'name': 'Andrew Ng Machine Learning Course',
            'type': 'Course',
            'url': 'https://www.coursera.org/learn/machine-learning'
        },
        {
            'name': 'Deep Learning Book',
            'type': 'Book',
            'url': 'https://www.deeplearningbook.org/'
        }
        # ... more resources
    ],
    
    'definitions': [
        {
            'term': 'Machine Learning',
            'definition': 'A subset of AI that enables computers to learn from data.',
            'domain': 'Computer Science'
        }
        # ... more definitions
    ],
    
    'quiz': [
        {
            'question': 'What is supervised learning?',
            'options': [
                {'letter': 'a', 'text': 'Learning from labeled data'},
                {'letter': 'b', 'text': 'Learning without labels'},
                {'letter': 'c', 'text': 'Reinforcement learning'},
                {'letter': 'd', 'text': 'Deep learning'}
            ],
            'correct_answer': 'a',
            'explanation': 'Supervised learning uses labeled training data.',
            'difficulty': 'easy'
        }
        # ... 10 questions total
    ],
    
    'examples': [
        {
            'calculation': '(100 + 200) / 2 = 150',
            'result': '150'
        }
        # ... mathematical examples
    ]
}

# Run validation
validator = ContentValidator()
report = validator.validate_learning_guide(guide_data)

# Save report
validator.save_report(report, 'validation_report.json')
```

### Method 2: Validate Individual Components

You can also validate specific parts:

#### Validate URLs Only

```python
from content_validator import URLValidator

url_validator = URLValidator()

resources = [
    {'name': 'Resource 1', 'type': 'Course', 'url': 'https://example.com'},
    {'name': 'Resource 2', 'type': 'Book', 'url': 'https://example2.com'}
]

results = url_validator.batch_validate_urls(resources)

for result in results:
    print(f"{result.item}: {result.status} (confidence: {result.confidence:.0%})")
    print(f"  {result.details}")
    if result.suggestions:
        print(f"  Suggestions: {', '.join(result.suggestions)}")
```

#### Validate Definitions Only

```python
from content_validator import DefinitionValidator

def_validator = DefinitionValidator()

definitions = [
    {'term': 'Neural Network', 'definition': 'A computing system inspired by biological neural networks.'},
    {'term': 'Gradient Descent', 'definition': 'An optimization algorithm for minimizing loss functions.'}
]

results = def_validator.batch_validate_definitions(definitions)

for result in results:
    print(f"{result.item}: {result.status} (confidence: {result.confidence:.0%})")
    if result.evidence:
        print(f"  Evidence: {result.evidence[0]}")
```

#### Validate Quiz Only

```python
from content_validator import QuizValidator

quiz_validator = QuizValidator()

quiz_questions = [
    {
        'question': 'What is machine learning?',
        'options': [
            {'letter': 'a', 'text': 'Option A'},
            {'letter': 'b', 'text': 'Option B'},
            {'letter': 'c', 'text': 'Option C'},
            {'letter': 'd', 'text': 'Option D'}
        ],
        'correct_answer': 'a',
        'explanation': 'Explanation here',
        'difficulty': 'easy'
    }
    # ... more questions
]

results = quiz_validator.batch_validate_quiz(quiz_questions)

for result in results:
    if result.status == 'failed':
        print(f"❌ {result.item}: {result.details}")
```

---

## Understanding Validation Results

### Status Levels

- ✅ **PASSED**: Item validated successfully (confidence 70-100%)
- ⚠️ **WARNING**: Item has minor issues or couldn't be fully verified (confidence 30-70%)
- ❌ **FAILED**: Item has critical issues (confidence 0-30%)
- ⏭️ **SKIPPED**: Validation not possible (missing libraries, etc.)

### Confidence Scores

- **90-100%**: Very high confidence - likely accurate
- **70-89%**: Good confidence - minor verification recommended
- **50-69%**: Moderate confidence - manual check recommended
- **30-49%**: Low confidence - definitely verify manually
- **0-29%**: Very low confidence - likely has issues

### Example Report Output

```
======================================================================
CONTENT VALIDATION REPORT
======================================================================

Topic: Introduction to Machine Learning

📚 Validating Resources...
   Resource URLs: 12 passed, 2 warnings, 1 failed

   ❌ Fast.ai Course: URL not accessible (Status: 404)

📖 Validating Definitions...
   Definitions: 8 passed, 2 warnings, 0 failed

❓ Validating Quiz Questions...
   Quiz Questions: 9 passed, 1 warnings, 0 failed

🧮 Validating Worked Examples...
   Mathematical Examples: 5 passed, 2 warnings, 0 failed

======================================================================
VALIDATION SUMMARY
======================================================================

Total Checks: 38
✅ Passed: 34 (89.5%)
⚠️  Warnings: 7 (18.4%)
❌ Failed: 1 (2.6%)
⏭️  Skipped: 0 (0.0%)

Overall Confidence: 82.3%

✅ Content validation looks good! Still recommend expert review.
```

---

## Validation Checks Performed

### 1. Resource URL Validation

**What's Checked:**
- ✅ URL format is valid
- ✅ URL is accessible (HTTP 200)
- ✅ No redirects or redirect destination is valid
- ✅ Content type matches expected type (Course, Book, Video, etc.)
- ✅ Response time is reasonable

**Limitations:**
- Cannot verify content quality or accuracy
- Cannot access paywalled content
- May fail for sites requiring JavaScript

### 2. Definition Validation

**What's Checked:**
- ✅ Term exists in Wikipedia
- ✅ Definition aligns with Wikipedia content
- ✅ Keyword overlap with authoritative sources
- ✅ No disambiguation issues

**Limitations:**
- Only checks Wikipedia (good baseline, but not exhaustive)
- Cannot verify very specialized terms
- May miss domain-specific nuances

### 3. Quiz Validation

**What's Checked:**
- ✅ Structural correctness (10 questions, 4 options each)
- ✅ Correct answer is one of the options
- ✅ No duplicate options
- ✅ Explanations are provided
- ✅ Difficulty distribution (40% easy, 40% medium, 20% hard)

**Limitations:**
- Cannot verify if answers are actually correct
- Cannot assess question quality
- Manual expert review still required for accuracy

### 4. Mathematical Validation

**What's Checked:**
- ✅ Mathematical expressions are present
- ✅ Results are stated

**Limitations:**
- Currently requires manual verification
- Does not execute calculations automatically (safety concern)
- Recommend using calculator/CAS for verification

---

## Best Practices

### 1. Always Run Validation First

```python
# Generate learning guide
guide = generate_learning_guide(topic)

# IMMEDIATELY validate
validator = ContentValidator()
report = validator.validate_learning_guide(guide)

# Review report before using
if report['summary']['failed'] > 0:
    print("⚠️ Critical issues found! Fix before using.")
```

### 2. Review Failed Items Carefully

```python
# Check detailed results
for result in report['detailed_results']:
    if result['status'] == 'failed':
        print(f"❌ {result['item']}")
        print(f"   Issue: {result['details']}")
        print(f"   Fix: {', '.join(result['suggestions'])}")
```

### 3. Set Confidence Thresholds

```python
# Only accept high-confidence results
high_confidence_items = [
    r for r in report['detailed_results']
    if r['confidence'] >= 0.8
]

if len(high_confidence_items) / len(report['detailed_results']) < 0.7:
    print("⚠️ Too many low-confidence items. Manual review essential.")
```

### 4. Save Validation Reports

```python
# Save with timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f"validation_report_{timestamp}.json"
validator.save_report(report, filename)
```

### 5. Combine with Manual Verification

**Automated validation catches:**
- Broken links
- Structural issues
- Basic accuracy checks

**Manual verification should check:**
- Content quality and depth
- Expert-level accuracy
- Domain-specific correctness
- Teaching effectiveness

---

## Troubleshooting

### URLs Keep Failing

**Possible causes:**
- Site is actually down
- Site requires JavaScript (validator uses HTTP only)
- Site blocks automated requests
- Temporary network issue

**Solutions:**
1. Manually check URL in browser
2. Wait and retry (may be temporary)
3. Check if URL redirects to login page
4. Use alternative resources

### Wikipedia Validation Not Working

**Causes:**
- Wikipedia library not installed
- Term too specific/specialized
- Internet connection issues

**Solutions:**
```bash
pip install wikipedia
```

Or manually verify definitions against textbooks.

### Validation Takes Too Long

**Optimization:**
```python
# Validate only critical components
url_results = url_validator.batch_validate_urls(resources[:5])  # Top 5 only
```

### Getting Too Many Warnings

**Normal for:**
- Specialized/technical topics
- New/emerging fields
- Domain-specific terminology

**Action:** Manual expert review is extra important.

---

## Integration with Workflow

### Recommended Workflow

```
1. Generate Learning Guide
         ↓
2. Run Automated Validation ← YOU ARE HERE
         ↓
3. Review Validation Report
         ↓
4. Fix Critical Issues
         ↓
5. Manual Expert Review (YOU + Domain Expert)
         ↓
6. Cross-check with Another LLM
         ↓
7. Final Approval
         ↓
8. Use for Learning
```

### Validation Checklist

Before using any learning guide:

- [ ] Ran content_validator.py
- [ ] Overall confidence >70%
- [ ] All failed items addressed
- [ ] Top 5 resources manually checked
- [ ] Quiz answers verified with authoritative sources
- [ ] Definitions cross-checked with textbooks
- [ ] Mathematical examples calculated independently
- [ ] Domain expert reviewed (if critical topic)
- [ ] Cross-checked with another LLM
- [ ] Saved validation report for reference

---

## Advanced Usage

### Custom Validation Rules

Extend the validator for domain-specific checks:

```python
from content_validator import ContentValidator

class TechnicalContentValidator(ContentValidator):
    """Extended validator for technical content"""
    
    def validate_code_examples(self, code: str, language: str) -> ValidationResult:
        """Validate code syntax"""
        # Add custom code validation
        pass
    
    def validate_mathematical_proofs(self, proof: str) -> ValidationResult:
        """Validate mathematical proofs"""
        # Add proof checking logic
        pass
```

### Batch Validation

Validate multiple guides:

```python
guides = [guide1, guide2, guide3]
validator = ContentValidator()

for idx, guide in enumerate(guides):
    print(f"\nValidating Guide {idx+1}: {guide['topic']}")
    report = validator.validate_learning_guide(guide)
    validator.save_report(report, f"report_{idx+1}.json")
```

---

## Limitations and Disclaimers

### What Validation CAN Do:
- ✅ Catch broken URLs
- ✅ Verify basic structure
- ✅ Cross-check against Wikipedia
- ✅ Identify obvious errors

### What Validation CANNOT Do:
- ❌ Verify expert-level accuracy
- ❌ Assess teaching quality
- ❌ Validate domain-specific nuances
- ❌ Replace human expert review
- ❌ Guarantee 100% correctness

### Your Responsibility:
**You must still manually verify critical information, especially for:**
- Medical/health information
- Legal advice
- Financial decisions
- Safety-critical applications
- Academic citations

---

## Support

If you find validation issues:

1. Check validation report details
2. Cross-reference with authoritative sources
3. Consult domain experts
4. Report systematic issues

**Remember:** Validation is a tool to help you, not a guarantee. Always use critical thinking!

