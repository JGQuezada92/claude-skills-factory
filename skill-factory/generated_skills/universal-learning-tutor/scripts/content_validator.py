#!/usr/bin/env python3
"""
Content Validator for Universal Learning Tutor
Validates accuracy of generated learning content against authoritative sources
"""

import requests
import json
import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict
from datetime import datetime
import hashlib
from urllib.parse import urlparse, quote
import time
from collections import defaultdict

# Optional imports (gracefully degrade if not available)
try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False
    print("⚠️  Warning: BeautifulSoup not available. Install with: pip install beautifulsoup4")

try:
    import wikipedia
    HAS_WIKIPEDIA = True
except ImportError:
    HAS_WIKIPEDIA = False
    print("⚠️  Warning: Wikipedia library not available. Install with: pip install wikipedia")


@dataclass
class ValidationResult:
    """Results from a validation check"""
    check_type: str
    item: str
    status: str  # 'passed', 'failed', 'warning', 'skipped'
    confidence: float  # 0.0 to 1.0
    details: str
    suggestions: List[str]
    evidence: List[str]
    timestamp: str


class URLValidator:
    """Validates resource URLs and checks accessibility"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        self.timeout = 10
        self.checked_urls = {}  # Cache results
    
    def validate_url(self, url: str, expected_type: str = None, resource_name: str = None) -> ValidationResult:
        """Validate a single URL"""
        
        # Check cache
        cache_key = f"{url}_{expected_type}"
        if cache_key in self.checked_urls:
            return self.checked_urls[cache_key]
        
        try:
            # Check URL format
            parsed = urlparse(url)
            if not parsed.scheme or not parsed.netloc:
                result = ValidationResult(
                    check_type='url_format',
                    item=resource_name or url,
                    status='failed',
                    confidence=0.0,
                    details=f"Invalid URL format: {url}",
                    suggestions=["Check URL formatting", "Ensure http:// or https:// prefix"],
                    evidence=[],
                    timestamp=datetime.now().isoformat()
                )
                self.checked_urls[cache_key] = result
                return result
            
            # Check accessibility
            response = self.session.head(url, timeout=self.timeout, allow_redirects=True)
            
            if response.status_code == 200:
                # Get content type if available
                content_type = response.headers.get('content-type', '').lower()
                
                # Verify expected type matches
                type_warnings = []
                confidence = 0.95
                
                if expected_type:
                    expected_lower = expected_type.lower()
                    if expected_lower == 'video' and not any(x in url.lower() for x in ['youtube.com', 'vimeo.com', 'video']):
                        type_warnings.append(f"URL may not be a {expected_type} resource")
                        confidence = 0.7
                    elif expected_lower == 'course' and not any(x in url.lower() for x in ['coursera', 'udemy', 'edx', 'udacity', 'course']):
                        type_warnings.append(f"URL may not be a {expected_type} resource")
                        confidence = 0.7
                    elif expected_lower == 'book' and not any(x in url.lower() for x in ['amazon', 'book', 'springer', 'oreilly']):
                        type_warnings.append(f"URL may not be a {expected_type} resource")
                        confidence = 0.7
                
                result = ValidationResult(
                    check_type='url_accessibility',
                    item=resource_name or url,
                    status='passed' if not type_warnings else 'warning',
                    confidence=confidence,
                    details=f"URL accessible (Status: {response.status_code})",
                    suggestions=type_warnings,
                    evidence=[f"Content-Type: {content_type}", f"Final URL: {response.url}"],
                    timestamp=datetime.now().isoformat()
                )
            
            elif response.status_code in [301, 302, 307, 308]:
                result = ValidationResult(
                    check_type='url_accessibility',
                    item=resource_name or url,
                    status='warning',
                    confidence=0.8,
                    details=f"URL redirects (Status: {response.status_code})",
                    suggestions=["Consider using the final URL directly"],
                    evidence=[f"Redirects to: {response.url}"],
                    timestamp=datetime.now().isoformat()
                )
            
            else:
                result = ValidationResult(
                    check_type='url_accessibility',
                    item=resource_name or url,
                    status='failed',
                    confidence=0.0,
                    details=f"URL not accessible (Status: {response.status_code})",
                    suggestions=["Verify URL is correct", "Check if resource still exists", "Try accessing in browser"],
                    evidence=[f"HTTP Status: {response.status_code}"],
                    timestamp=datetime.now().isoformat()
                )
        
        except requests.Timeout:
            result = ValidationResult(
                check_type='url_accessibility',
                item=resource_name or url,
                status='warning',
                confidence=0.3,
                details=f"URL timed out after {self.timeout} seconds",
                suggestions=["Resource may be slow or temporarily unavailable", "Try again later"],
                evidence=["Timeout"],
                timestamp=datetime.now().isoformat()
            )
        
        except Exception as e:
            result = ValidationResult(
                check_type='url_accessibility',
                item=resource_name or url,
                status='failed',
                confidence=0.0,
                details=f"Error checking URL: {str(e)}",
                suggestions=["Verify URL format", "Check internet connection"],
                evidence=[str(e)],
                timestamp=datetime.now().isoformat()
            )
        
        self.checked_urls[cache_key] = result
        return result
    
    def batch_validate_urls(self, resources: List[Dict]) -> List[ValidationResult]:
        """Validate multiple URLs"""
        results = []
        for idx, resource in enumerate(resources):
            url = resource.get('url') or resource.get('link')
            resource_type = resource.get('type')
            resource_name = resource.get('name', f"Resource {idx+1}")
            
            if url:
                result = self.validate_url(url, resource_type, resource_name)
                results.append(result)
                time.sleep(0.5)  # Rate limiting to be polite
        
        return results


class DefinitionValidator:
    """Validates definitions against authoritative sources"""
    
    def __init__(self):
        self.wikipedia_available = HAS_WIKIPEDIA
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def validate_definition(self, term: str, definition: str, domain: str = None) -> ValidationResult:
        """Validate a definition against Wikipedia and web sources"""
        
        if not self.wikipedia_available:
            return ValidationResult(
                check_type='definition_accuracy',
                item=term,
                status='skipped',
                confidence=0.0,
                details="Wikipedia library not available for validation",
                suggestions=["Install wikipedia library: pip install wikipedia"],
                evidence=[],
                timestamp=datetime.now().isoformat()
            )
        
        try:
            # Search Wikipedia
            search_results = wikipedia.search(term, results=3)
            
            if not search_results:
                return ValidationResult(
                    check_type='definition_accuracy',
                    item=term,
                    status='warning',
                    confidence=0.3,
                    details=f"No Wikipedia article found for '{term}'",
                    suggestions=["Term may be too specific or misspelled", "Verify term name"],
                    evidence=["No Wikipedia results"],
                    timestamp=datetime.now().isoformat()
                )
            
            # Get the most relevant article
            try:
                page = wikipedia.page(search_results[0], auto_suggest=False)
                wiki_summary = page.summary[:500]  # First 500 chars
                
                # Simple similarity check (keyword overlap)
                definition_words = set(re.findall(r'\w+', definition.lower()))
                summary_words = set(re.findall(r'\w+', wiki_summary.lower()))
                
                # Remove common words
                common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'is', 'are', 'was', 'were'}
                definition_words -= common_words
                summary_words -= common_words
                
                # Calculate overlap
                overlap = len(definition_words & summary_words)
                total = len(definition_words)
                similarity = overlap / total if total > 0 else 0
                
                if similarity > 0.4:
                    status = 'passed'
                    confidence = min(0.7 + (similarity - 0.4) * 0.5, 0.95)
                    details = f"Definition aligns with Wikipedia content (similarity: {similarity:.2%})"
                    suggestions = []
                elif similarity > 0.2:
                    status = 'warning'
                    confidence = 0.5
                    details = f"Definition partially aligns with Wikipedia (similarity: {similarity:.2%})"
                    suggestions = ["Consider cross-checking with additional sources", "Definition may need refinement"]
                else:
                    status = 'warning'
                    confidence = 0.3
                    details = f"Definition has low alignment with Wikipedia (similarity: {similarity:.2%})"
                    suggestions = ["Verify definition accuracy", "Compare with multiple authoritative sources"]
                
                return ValidationResult(
                    check_type='definition_accuracy',
                    item=term,
                    status=status,
                    confidence=confidence,
                    details=details,
                    suggestions=suggestions,
                    evidence=[
                        f"Wikipedia article: {page.title}",
                        f"URL: {page.url}",
                        f"Summary excerpt: {wiki_summary[:200]}..."
                    ],
                    timestamp=datetime.now().isoformat()
                )
            
            except wikipedia.exceptions.DisambiguationError as e:
                return ValidationResult(
                    check_type='definition_accuracy',
                    item=term,
                    status='warning',
                    confidence=0.5,
                    details=f"Term '{term}' has multiple meanings (disambiguation)",
                    suggestions=["Term may need more context", "Consider specifying domain"],
                    evidence=[f"Possible meanings: {', '.join(e.options[:5])}"],
                    timestamp=datetime.now().isoformat()
                )
        
        except Exception as e:
            return ValidationResult(
                check_type='definition_accuracy',
                item=term,
                status='warning',
                confidence=0.3,
                details=f"Error validating definition: {str(e)}",
                suggestions=["Manual verification recommended"],
                evidence=[str(e)],
                timestamp=datetime.now().isoformat()
            )
    
    def batch_validate_definitions(self, definitions: List[Dict]) -> List[ValidationResult]:
        """Validate multiple definitions"""
        results = []
        for defn in definitions:
            term = defn.get('term')
            definition = defn.get('definition')
            domain = defn.get('domain')
            
            if term and definition:
                result = self.validate_definition(term, definition, domain)
                results.append(result)
                time.sleep(1)  # Rate limiting for Wikipedia API
        
        return results


class QuizValidator:
    """Validates quiz questions and answers"""
    
    def __init__(self):
        self.definition_validator = DefinitionValidator()
    
    def validate_quiz_question(self, question: Dict) -> ValidationResult:
        """Validate a single quiz question"""
        
        question_text = question.get('question', '')
        options = question.get('options', [])
        correct_answer = question.get('correct_answer', '')
        explanation = question.get('explanation', '')
        
        issues = []
        warnings = []
        
        # Check structure
        if not question_text:
            issues.append("Question text is empty")
        if len(options) < 4:
            issues.append(f"Only {len(options)} options provided (should be 4)")
        if not correct_answer:
            issues.append("No correct answer specified")
        if not explanation:
            warnings.append("No explanation provided")
        
        # Check answer is valid option
        if correct_answer:
            option_letters = [opt.get('letter', '') for opt in options]
            if correct_answer.lower() not in [l.lower() for l in option_letters]:
                issues.append(f"Correct answer '{correct_answer}' not found in options")
        
        # Check for duplicate options
        option_texts = [opt.get('text', '') for opt in options]
        if len(option_texts) != len(set(option_texts)):
            warnings.append("Duplicate answer options detected")
        
        # Determine status
        if issues:
            status = 'failed'
            confidence = 0.0
            details = "Quiz question has structural issues: " + "; ".join(issues)
        elif warnings:
            status = 'warning'
            confidence = 0.7
            details = "Quiz question has minor issues: " + "; ".join(warnings)
        else:
            status = 'passed'
            confidence = 0.8  # Can't verify correctness automatically
            details = "Quiz question structure is valid"
        
        return ValidationResult(
            check_type='quiz_structure',
            item=question_text[:50] + "..." if len(question_text) > 50 else question_text,
            status=status,
            confidence=confidence,
            details=details,
            suggestions=warnings + issues,
            evidence=[f"{len(options)} options", f"Correct: {correct_answer}", f"Has explanation: {bool(explanation)}"],
            timestamp=datetime.now().isoformat()
        )
    
    def batch_validate_quiz(self, questions: List[Dict]) -> List[ValidationResult]:
        """Validate all quiz questions"""
        results = []
        
        # Check total count
        if len(questions) != 10:
            results.append(ValidationResult(
                check_type='quiz_completeness',
                item='Total Question Count',
                status='warning' if len(questions) >= 8 else 'failed',
                confidence=0.5 if len(questions) >= 8 else 0.0,
                details=f"Quiz has {len(questions)} questions (should be 10)",
                suggestions=["Add more questions to reach 10" if len(questions) < 10 else "Remove extra questions"],
                evidence=[f"Count: {len(questions)}"],
                timestamp=datetime.now().isoformat()
            ))
        
        # Validate each question
        for idx, question in enumerate(questions):
            result = self.validate_quiz_question(question)
            results.append(result)
        
        # Check difficulty distribution (if available)
        difficulties = [q.get('difficulty', 'unknown') for q in questions]
        easy_count = sum(1 for d in difficulties if d.lower() == 'easy')
        medium_count = sum(1 for d in difficulties if d.lower() == 'medium')
        hard_count = sum(1 for d in difficulties if d.lower() == 'hard')
        
        if easy_count + medium_count + hard_count > 0:
            # Expected: 40% easy, 40% medium, 20% hard
            expected_easy = 4
            expected_medium = 4
            expected_hard = 2
            
            if abs(easy_count - expected_easy) > 1 or abs(medium_count - expected_medium) > 1:
                results.append(ValidationResult(
                    check_type='quiz_difficulty_balance',
                    item='Difficulty Distribution',
                    status='warning',
                    confidence=0.6,
                    details=f"Difficulty distribution: {easy_count} easy, {medium_count} medium, {hard_count} hard",
                    suggestions=["Recommended: 4 easy, 4 medium, 2 hard for optimal learning"],
                    evidence=[f"Easy: {easy_count}/4", f"Medium: {medium_count}/4", f"Hard: {hard_count}/2"],
                    timestamp=datetime.now().isoformat()
                ))
        
        return results


class MathValidator:
    """Validates mathematical calculations in worked examples"""
    
    def validate_calculation(self, expression: str, expected_result: str) -> ValidationResult:
        """Validate a mathematical calculation"""
        
        try:
            # Simple eval for basic math (DANGER: Only use on trusted content!)
            # In production, use a safer math expression evaluator
            
            # Extract numbers and operators
            if '=' in expression:
                parts = expression.split('=')
                calculation = parts[0].strip()
                stated_result = parts[1].strip() if len(parts) > 1 else expected_result
            else:
                calculation = expression
                stated_result = expected_result
            
            # Very basic validation (expand this significantly for production)
            numbers = re.findall(r'-?\d+\.?\d*', calculation)
            
            if not numbers:
                return ValidationResult(
                    check_type='math_validation',
                    item=expression[:50],
                    status='skipped',
                    confidence=0.0,
                    details="No numbers found to validate",
                    suggestions=["Manual verification recommended for non-numeric content"],
                    evidence=[],
                    timestamp=datetime.now().isoformat()
                )
            
            # For now, just check that calculation and result exist
            return ValidationResult(
                check_type='math_validation',
                item=expression[:50],
                status='warning',
                confidence=0.5,
                details="Mathematical expression detected - manual verification required",
                suggestions=["Verify calculation manually", "Use calculator or CAS to confirm"],
                evidence=[f"Expression: {calculation}", f"Result: {stated_result}"],
                timestamp=datetime.now().isoformat()
            )
        
        except Exception as e:
            return ValidationResult(
                check_type='math_validation',
                item=expression[:50],
                status='warning',
                confidence=0.3,
                details=f"Cannot automatically validate: {str(e)}",
                suggestions=["Manual verification required"],
                evidence=[str(e)],
                timestamp=datetime.now().isoformat()
            )


class ContentValidator:
    """Main validator orchestrating all validation checks"""
    
    def __init__(self):
        self.url_validator = URLValidator()
        self.definition_validator = DefinitionValidator()
        self.quiz_validator = QuizValidator()
        self.math_validator = MathValidator()
    
    def validate_learning_guide(self, guide_content: Dict) -> Dict:
        """Validate a complete learning guide"""
        
        all_results = []
        
        print("\n" + "="*70)
        print("CONTENT VALIDATION REPORT")
        print("="*70)
        print(f"\nTopic: {guide_content.get('topic', 'Unknown')}")
        print(f"Validation Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        # 1. Validate Resources
        print("📚 Validating Resources...")
        resources = guide_content.get('resources', [])
        if resources:
            resource_results = self.url_validator.batch_validate_urls(resources)
            all_results.extend(resource_results)
            self._print_results_summary("Resource URLs", resource_results)
        else:
            print("   ⚠️  No resources found to validate\n")
        
        # 2. Validate Definitions
        print("📖 Validating Definitions...")
        definitions = guide_content.get('definitions', [])
        if definitions:
            definition_results = self.definition_validator.batch_validate_definitions(definitions)
            all_results.extend(definition_results)
            self._print_results_summary("Definitions", definition_results)
        else:
            print("   ⚠️  No definitions found to validate\n")
        
        # 3. Validate Quiz
        print("❓ Validating Quiz Questions...")
        quiz = guide_content.get('quiz', [])
        if quiz:
            quiz_results = self.quiz_validator.batch_validate_quiz(quiz)
            all_results.extend(quiz_results)
            self._print_results_summary("Quiz Questions", quiz_results)
        else:
            print("   ⚠️  No quiz questions found to validate\n")
        
        # 4. Validate Examples
        print("🧮 Validating Worked Examples...")
        examples = guide_content.get('examples', [])
        if examples:
            example_results = []
            for example in examples:
                if 'calculation' in example:
                    result = self.math_validator.validate_calculation(
                        example['calculation'],
                        example.get('result', '')
                    )
                    example_results.append(result)
            if example_results:
                all_results.extend(example_results)
                self._print_results_summary("Mathematical Examples", example_results)
            else:
                print("   ℹ️  No mathematical calculations to validate\n")
        else:
            print("   ⚠️  No examples found to validate\n")
        
        # Generate summary
        summary = self._generate_summary(all_results)
        
        # Print final report
        print("\n" + "="*70)
        print("VALIDATION SUMMARY")
        print("="*70)
        print(f"\nTotal Checks: {summary['total_checks']}")
        print(f"✅ Passed: {summary['passed']} ({summary['passed_pct']:.1f}%)")
        print(f"⚠️  Warnings: {summary['warnings']} ({summary['warnings_pct']:.1f}%)")
        print(f"❌ Failed: {summary['failed']} ({summary['failed_pct']:.1f}%)")
        print(f"⏭️  Skipped: {summary['skipped']} ({summary['skipped_pct']:.1f}%)")
        print(f"\nOverall Confidence: {summary['avg_confidence']:.1%}")
        
        if summary['failed'] > 0:
            print("\n⚠️  CRITICAL: Some validations failed. Manual review required!")
        elif summary['warnings'] > summary['passed']:
            print("\n⚠️  WARNING: Many items need manual verification.")
        else:
            print("\n✅ Content validation looks good! Still recommend expert review.")
        
        print("\n" + "="*70)
        print(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*70 + "\n")
        
        return {
            'summary': summary,
            'detailed_results': [asdict(r) for r in all_results],
            'timestamp': datetime.now().isoformat()
        }
    
    def _print_results_summary(self, category: str, results: List[ValidationResult]):
        """Print summary of validation results for a category"""
        passed = sum(1 for r in results if r.status == 'passed')
        warnings = sum(1 for r in results if r.status == 'warning')
        failed = sum(1 for r in results if r.status == 'failed')
        
        print(f"   {category}: {passed} passed, {warnings} warnings, {failed} failed")
        
        # Show critical failures
        for result in results:
            if result.status == 'failed':
                print(f"      ❌ {result.item}: {result.details}")
        
        print()
    
    def _generate_summary(self, results: List[ValidationResult]) -> Dict:
        """Generate summary statistics"""
        total = len(results)
        if total == 0:
            return {
                'total_checks': 0,
                'passed': 0,
                'warnings': 0,
                'failed': 0,
                'skipped': 0,
                'passed_pct': 0,
                'warnings_pct': 0,
                'failed_pct': 0,
                'skipped_pct': 0,
                'avg_confidence': 0
            }
        
        passed = sum(1 for r in results if r.status == 'passed')
        warnings = sum(1 for r in results if r.status == 'warning')
        failed = sum(1 for r in results if r.status == 'failed')
        skipped = sum(1 for r in results if r.status == 'skipped')
        
        avg_confidence = sum(r.confidence for r in results) / total
        
        return {
            'total_checks': total,
            'passed': passed,
            'warnings': warnings,
            'failed': failed,
            'skipped': skipped,
            'passed_pct': (passed / total) * 100,
            'warnings_pct': (warnings / total) * 100,
            'failed_pct': (failed / total) * 100,
            'skipped_pct': (skipped / total) * 100,
            'avg_confidence': avg_confidence
        }
    
    def save_report(self, validation_report: Dict, output_path: str):
        """Save validation report to JSON file"""
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(validation_report, f, indent=2, ensure_ascii=False)
        print(f"✅ Validation report saved to: {output_path}")


def example_usage():
    """Example of how to use the ContentValidator"""
    
    # Example learning guide content structure
    example_guide = {
        'topic': 'Introduction to Machine Learning',
        'resources': [
            {
                'name': 'Machine Learning Course by Andrew Ng',
                'type': 'Course',
                'url': 'https://www.coursera.org/learn/machine-learning',
            },
            {
                'name': 'Deep Learning Book',
                'type': 'Book',
                'url': 'https://www.deeplearningbook.org/',
            },
            {
                'name': 'Fast.ai Course',
                'type': 'Course',
                'url': 'https://www.fast.ai/',
            }
        ],
        'definitions': [
            {
                'term': 'Machine Learning',
                'definition': 'A subset of artificial intelligence that enables computers to learn from data without being explicitly programmed.',
                'domain': 'Computer Science'
            },
            {
                'term': 'Supervised Learning',
                'definition': 'A type of machine learning where the algorithm learns from labeled training data.',
                'domain': 'Machine Learning'
            }
        ],
        'quiz': [
            {
                'question': 'What is supervised learning?',
                'options': [
                    {'letter': 'a', 'text': 'Learning from labeled data'},
                    {'letter': 'b', 'text': 'Learning without labels'},
                    {'letter': 'c', 'text': 'Reinforcement learning'},
                    {'letter': 'd', 'text': 'Transfer learning'}
                ],
                'correct_answer': 'a',
                'explanation': 'Supervised learning uses labeled training data.',
                'difficulty': 'easy'
            }
        ],
        'examples': [
            {
                'calculation': '(100 + 200) / 2 = 150',
                'result': '150'
            }
        ]
    }
    
    # Run validation
    validator = ContentValidator()
    report = validator.validate_learning_guide(example_guide)
    
    # Save report
    validator.save_report(report, 'validation_report.json')


if __name__ == "__main__":
    example_usage()

