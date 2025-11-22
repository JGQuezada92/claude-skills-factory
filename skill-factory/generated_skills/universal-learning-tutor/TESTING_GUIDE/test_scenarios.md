# Universal Learning Tutor - Test Scenarios

## Overview

This document outlines comprehensive test scenarios for validating the Universal Learning Tutor skill across different domains, difficulty levels, and use cases.

---

## SCENARIO 1: Technical Subject - Machine Learning (Beginner)

### Setup

**User Profile**: Software engineer with no ML background
**Topic**: "Introduction to Machine Learning"
**Knowledge Level**: Beginner
**Learning Goal**: Build first ML model
**Time Available**: 5 hours/week
**Format Preference**: Both visual and audio

### Expected Outputs

**Phase 1 - Research**:
- 10-15 ranked resources including Andrew Ng's course, Fast.ai, etc.
- Mix of FREE and PAID clearly labeled
- Resources categorized (Foundation, Building Depth, Advanced)

**Phase 2 - Priming**:
- Knowledge map with 5-7 subtopics (Supervised Learning, Unsupervised Learning, Model Evaluation, etc.)
- 10 quiz questions (4 easy, 4 medium, 2 hard)
- 3-5 projects (Build spam classifier → Image classifier → Recommender system)

**Phase 3 - Comprehension**:
- Complete notes for each subtopic
- Worked examples showing algorithm implementations
- Common pitfalls (overfitting, feature scaling, etc.)
- Spaced repetition prompts at Day 1, 3, Week 1, 2

### Success Criteria

- [ ] All resources are real and accessible
- [ ] Quiz answers are correct
- [ ] Worked examples show proper ML methodology
- [ ] Format is audio-friendly (conversational, clear transitions)
- [ ] Output follows standardized template exactly

### Validation Steps

1. Check that resource URLs are valid
2. Manually verify quiz answers against authoritative sources
3. Test worked examples for mathematical correctness
4. Read aloud to verify audio-friendliness
5. Convert to NotebookLM to test podcast conversion

---

## SCENARIO 2: Business Subject - M&A Due Diligence (Intermediate)

### Setup

**User Profile**: Investment banker with 3 years experience
**Topic**: "Financial Due Diligence for M&A Transactions"
**Knowledge Level**: Intermediate
**Learning Goal**: Lead due diligence projects
**Time Available**: 10 hours/week
**Format Preference**: Visual primarily

### Expected Outputs

**Phase 1 - Research**:
- Resources from top firms (McKinsey, BCG, PE firms)
- Mix of courses, case studies, frameworks
- Both free and paid resources

**Phase 2 - Priming**:
- Knowledge map covering Financial Analysis, Commercial DD, Legal DD, Operational DD, etc.
- Quiz covering key concepts, red flags, valuation methods
- Projects: Analyze public company financials → Mock DD on private company → Full deal memo

**Phase 3 - Comprehension**:
- Frameworks (Quality of Earnings, Working Capital Analysis, etc.)
- Worked examples showing actual DD findings
- Common pitfalls (missing red flags, overoptimistic projections)
- Expert insights from M&A practitioners

### Success Criteria

- [ ] Resources reflect industry best practices
- [ ] Frameworks match those used at top firms
- [ ] Examples use realistic financial scenarios
- [ ] Red flags identified are comprehensive
- [ ] Visual formatting is clear and scannable

### Validation Steps

1. Compare frameworks against McKinsey/BCG methodologies
2. Verify financial calculations in worked examples
3. Check that red flags match industry standards
4. Assess visual hierarchy and scannability
5. Validate against real M&A professional feedback

---

## SCENARIO 3: Creative Subject - Classical Oil Painting (Beginner)

### Setup

**User Profile**: Complete beginner, no art background
**Topic**: "Classical Oil Painting Techniques"
**Knowledge Level**: Beginner
**Learning Goal**: Create realistic portraits
**Time Available**: 3 hours/week
**Format Preference**: Both visual and audio

### Expected Outputs

**Phase 1 - Research**:
- Courses from established artists/schools
- Books by Old Masters and contemporary realists
- YouTube channels with technique demonstrations
- Mix of free and paid

**Phase 2 - Priming**:
- Knowledge map: Materials, Color Theory, Composition, Technique, Subject Matter
- Quiz on fundamentals (color mixing, brushwork, etc.)
- Projects: Still life → Landscape → Portrait

**Phase 3 - Comprehension**:
- Techniques explained step-by-step
- Color mixing principles with examples
- Analysis of master paintings (Rembrandt, Vermeer, etc.)
- Common beginner mistakes
- Process tips from professional artists

### Success Criteria

- [ ] Techniques are accurately described
- [ ] Resources include visual demonstrations
- [ ] Projects progress logically in difficulty
- [ ] Examples reference actual master works
- [ ] Audio format works for learning art (verbal descriptions clear)

### Validation Steps

1. Verify techniques against art instruction literature
2. Check that color theory is accurate
3. Confirm master painting analysis is art-historically correct
4. Test if verbal descriptions are clear without visuals
5. Validate progression makes sense for beginners

---

## SCENARIO 4: Academic Subject - Molecular Biology (Intermediate)

### Setup

**User Profile**: Biology undergrad, 2 years coursework completed
**Topic**: "Molecular Biology of Cancer"
**Knowledge Level**: Intermediate
**Learning Goal**: Understand research papers in oncology
**Time Available**: 8 hours/week
**Format Preference**: Audio-friendly for podcast

### Expected Outputs

**Phase 1 - Research**:
- Academic resources (textbooks, review papers, lecture series)
- Online courses from universities (MIT OCW, etc.)
- Research databases and journals

**Phase 2 - Priming**:
- Knowledge map: Cell Cycle, Oncogenes, Tumor Suppressors, Metastasis, Treatment
- Quiz covering molecular mechanisms
- Projects: Analyze mutation data → Read primary research paper → Critique clinical trial

**Phase 3 - Comprehension**:
- Multi-scale explanations (molecular → cellular → tissue → organism)
- Mechanistic diagrams described verbally
- Key experiments that established the field
- Cancer hallmarks framework (Hanahan & Weinberg)

### Success Criteria

- [ ] Scientific accuracy (definitions, mechanisms)
- [ ] Appropriate level (intermediate bio background)
- [ ] Audio descriptions of diagrams are clear
- [ ] References to key papers/experiments
- [ ] Terminology matches field conventions

### Validation Steps

1. Verify against authoritative textbooks (Alberts, Lodish)
2. Check mechanisms against primary literature
3. Confirm hallmarks framework is accurately presented
4. Test if diagrams can be understood from audio alone
5. Validate terminology with biology faculty

---

## SCENARIO 5: Specialized Domain - Contract Law (Beginner)

### Setup

**User Profile**: Business professional, no legal training
**Topic**: "Contract Law Fundamentals for Business"
**Knowledge Level**: Beginner
**Learning Goal**: Review and negotiate SaaS contracts
**Time Available**: 6 hours/week
**Format Preference**: Visual (reference document)

### Expected Outputs

**Phase 1 - Research**:
- Law school materials adapted for business audience
- Practical guides from legal publishers
- Template contracts with annotations
- Business-oriented legal resources

**Phase 2 - Priming**:
- Knowledge map: Formation, Terms, Breach, Remedies, Special Clauses (IP, Indemnification, etc.)
- Quiz on basic principles and common clauses
- Projects: Analyze sample contract → Identify issues → Draft simple terms

**Phase 3 - Comprehension**:
- Legal principles explained in plain language
- Examples from actual business contracts
- Common negotiation points
- Red flags to watch for
- When to involve attorney

### Success Criteria

- [ ] Legal principles are accurate
- [ ] Language is accessible to non-lawyers
- [ ] Examples are business-relevant (not academic)
- [ ] Practical guidance for contract review
- [ ] Clear about limitations (not legal advice)

### Validation Steps

1. Verify legal principles with attorney
2. Check examples against real contracts
3. Assess accessibility for non-legal audience
4. Confirm red flags are comprehensive
5. Validate against business contract reviewer feedback

---

## SCENARIO 6: Edge Case - Highly Technical/Advanced

### Setup

**User Profile**: PhD student in physics
**Topic**: "Tensor Calculus and Differential Geometry for General Relativity"
**Knowledge Level**: Advanced
**Learning Goal**: Apply to GR research
**Time Available**: 15 hours/week
**Format Preference**: Visual with mathematical rigor

### Expected Outputs

**Phase 1 - Research**:
- Graduate-level textbooks (Wald, Carroll, Misner/Thorne/Wheeler)
- Lecture notes from top universities
- Research papers and review articles

**Phase 2 - Priming**:
- Knowledge map: Manifolds, Tensors, Connections, Curvature, Einstein Equations
- Quiz on advanced concepts (covariant derivatives, Riemann tensor, etc.)
- Projects: Calculate Christoffel symbols → Derive Schwarzschild → Analyze gravitational waves

**Phase 3 - Comprehension**:
- Rigorous mathematical definitions
- Derivations shown in full detail
- Physical interpretation of mathematical objects
- Connection to general relativity applications

### Success Criteria

- [ ] Mathematical rigor appropriate for PhD level
- [ ] Derivations are complete and correct
- [ ] Resources are graduate-level
- [ ] Examples connect math to physical phenomena
- [ ] Notation is standard (Einstein summation, etc.)

### Validation Steps

1. Verify derivations against textbooks
2. Check mathematical notation is standard
3. Confirm examples are physically accurate
4. Validate against physics PhD student feedback
5. Test mathematical examples for correctness

---

## SCENARIO 7: Edge Case - Very Narrow Topic

### Setup

**User Profile**: Web developer
**Topic**: "HTTP/2 Protocol Improvements over HTTP/1.1"
**Knowledge Level**: Intermediate
**Learning Goal**: Optimize website performance
**Time Available**: 4 hours/week
**Format Preference**: Visual

### Expected Outputs

**Phase 1 - Research**:
- RFC specifications
- Technical articles comparing protocols
- Performance benchmarks
- Implementation guides

**Phase 2 - Priming**:
- Knowledge map: Multiplexing, Header Compression, Server Push, Binary Framing
- Quiz on protocol differences
- Projects: Analyze network traffic → Implement HTTP/2 server → Optimize website

**Phase 3 - Comprehension**:
- Technical specifications explained clearly
- Performance comparisons with data
- Implementation considerations
- When to use each feature

### Success Criteria

- [ ] Technical accuracy (protocol details)
- [ ] Appropriate scope (focused on HTTP/2 specifically)
- [ ] Practical implementation guidance
- [ ] Performance data is accurate
- [ ] Resources are authoritative (RFCs, MDN, etc.)

### Validation Steps

1. Verify against RFC 7540
2. Check performance claims against benchmarks
3. Confirm implementation details are correct
4. Test examples for technical accuracy
5. Validate with web performance expert

---

## SCENARIO 8: Multi-Turn Refinement

### Setup

**Initial Request**: "Teach me strategic business planning"
**User Profile**: Mid-level manager
**Knowledge Level**: Beginner in strategy
**Follow-up 1**: "Can you focus more on competitive analysis frameworks?"
**Follow-up 2**: "Add more examples from tech companies"

### Expected Behavior

1. **Initial Response**: Comprehensive guide covering strategy broadly
2. **After Follow-up 1**: Add more depth to competitive analysis section, include Porter's Five Forces, competitor mapping, etc.
3. **After Follow-up 2**: Incorporate examples from Google, Apple, Amazon, Microsoft, Meta in worked examples

### Success Criteria

- [ ] Skill responds appropriately to refinement requests
- [ ] Added depth maintains overall structure
- [ ] New examples are accurate and relevant
- [ ] Format consistency maintained across iterations

---

## Cross-Cutting Validation Checks

For ALL scenarios, validate:

### Format Compliance
- [ ] Follows standardized template exactly
- [ ] All required sections present
- [ ] Proper markdown formatting
- [ ] Consistent structure across topics

### Content Quality
- [ ] Resources are real and high-quality
- [ ] Quiz answers are correct with explanations
- [ ] Worked examples are accurate
- [ ] Definitions match expert consensus
- [ ] No placeholder text remains

### Multi-Modal Optimization
- [ ] Conversational tone (audio-friendly)
- [ ] Clear visual hierarchy (scannable)
- [ ] Transition phrases present
- [ ] Sentence length appropriate (15-20 words avg)
- [ ] NotebookLM compatible

### Domain Adaptation
- [ ] Teaching style suits subject
- [ ] Appropriate depth for level
- [ ] Examples match domain conventions
- [ ] Terminology is field-standard

### Completeness
- [ ] 10-15 resources ranked
- [ ] 10 quiz questions (4/4/2 difficulty split)
- [ ] 3-5 project prompts
- [ ] Complete notes for all subtopics
- [ ] Spaced repetition prompts (4 per subtopic)

---

## Testing Workflow

1. **Select Scenario**: Choose test scenario
2. **Execute**: Invoke skill with specified parameters
3. **Review Output**: Check all sections present
4. **Validate Content**: Verify accuracy and quality
5. **Check Format**: Ensure template compliance
6. **Test Multi-Modal**: Verify audio and visual optimization
7. **Document Issues**: Note any problems found
8. **Iterate**: Request refinements if needed

---

## Success Metrics

### Quantitative
- 100% of required sections present
- 95%+ accuracy in quiz answers
- 90%+ of resources currently available
- Average 15-20 words per sentence
- 10-15 resources provided
- 10 quiz questions provided
- 3-5 project prompts provided

### Qualitative
- Expert validation of content accuracy
- User feedback on usability
- Audio conversion success (NotebookLM)
- Visual scannability rating
- Domain adaptation appropriateness

---

## Issue Reporting Template

When issues are found:

**Issue ID**: [Unique identifier]
**Scenario**: [Which test scenario]
**Category**: [Format/Content/Multi-Modal/Domain]
**Severity**: [Critical/High/Medium/Low]
**Description**: [What's wrong]
**Expected**: [What should happen]
**Actual**: [What actually happened]
**Steps to Reproduce**: [How to trigger issue]
**Suggested Fix**: [Proposed solution]

---

## Notes

- Test scenarios should be run on diverse topics regularly
- New edge cases should be added as discovered
- Validation should include domain experts when possible
- Audio testing should include actual NotebookLM conversion
- Visual testing should include different devices/browsers

