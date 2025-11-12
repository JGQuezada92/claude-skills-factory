# Test Scenarios for Phenom Blog Content Creator

## Basic Scenarios

### Scenario 1: Simple Case Study Blog Post
**Input:** 
- Single company case study with challenge, solution, and results
- User provides content directly in chat

**Expected Output:** 
- Word document (Phenom_Blog_Post.docx)
- Markdown file (Phenom_Blog_Post.md)
- Both files with proper Phenom formatting
- Introduction section with hook
- Table of contents
- Single case study section following Phenom structure
- Conclusion section

**Success Criteria:**
- Files generated successfully
- Formatting matches visual examples
- Structure follows Phenom patterns
- All required sections present
- Metrics formatted correctly

### Scenario 2: Multiple Case Studies Blog Post
**Input:**
- Multiple company case studies (3-5 companies)
- Each with challenge, solution, metrics

**Expected Output:**
- Word and Markdown files
- Introduction section
- Table of contents listing all companies
- Multiple case study sections
- Each section follows Phenom structure
- Conclusion with call-to-action

**Success Criteria:**
- All case studies formatted consistently
- Proper section breaks between companies
- Table of contents matches all sections
- Consistent formatting throughout

## Intermediate Scenarios

### Scenario 3: Content from Research Skill
**Input:**
- Content passed from research skill
- Structured research data with findings
- Multiple sources and metrics

**Expected Output:**
- Formatted blog post
- Content organized into Phenom structure
- Proper attribution of sources
- Metrics extracted and formatted
- Related links included

**Success Criteria:**
- Content properly curated and organized
- All metrics formatted correctly
- Sources properly attributed
- Links formatted correctly

### Scenario 4: Complex Content with Quotes and Links
**Input:**
- Content with multiple quotes from company representatives
- Multiple links to resources
- Detailed implementation descriptions
- Extensive metrics and results

**Expected Output:**
- Blog post with all quotes properly formatted
- Links formatted as hyperlinks (Word) and Markdown links (MD)
- Implementation details with bold feature names
- Results section with bulleted metrics

**Success Criteria:**
- Quotes properly attributed and formatted
- All links functional and properly styled
- Features/tools bolded correctly
- Metrics clearly presented

## Advanced Scenarios

### Scenario 5: Content Requiring Visual Formatting Alignment
**Input:**
- Content that needs exact visual formatting
- Specific typography, colors, spacing requirements

**Expected Output:**
- Word document matching visual examples exactly
- Markdown file with proper formatting
- Colors, fonts, spacing matching visual examples

**Success Criteria:**
- Visual comparison shows exact match
- Typography matches (fonts, sizes, weights)
- Colors match (text, links, accents)
- Spacing matches (paragraph, line spacing)
- Layout matches (headings, body, lists)

### Scenario 6: Content with Mixed Content Types
**Input:**
- Content with text, lists, quotes, metrics, links
- Multiple sections with different structures
- Some sections with numbered lists, some with bullet lists

**Expected Output:**
- Properly formatted blog post
- Lists formatted correctly (numbered vs bulleted)
- Quotes properly styled
- All content types properly formatted

**Success Criteria:**
- All content types formatted correctly
- Lists maintain proper formatting
- Quotes are distinct from body text
- Metrics stand out appropriately

## Edge Cases to Verify

### Edge Case 1: Minimal Content
**Input:** Very short content with limited information

**Expected Output:** Blog post that still follows Phenom structure with available content

**Verification:** Structure maintained even with minimal content

### Edge Case 2: Content Without Metrics
**Input:** Content without quantifiable metrics

**Expected Output:** Blog post formatted correctly, with warnings about missing metrics

**Verification:** Formatting still correct, warnings provided

### Edge Case 3: Content Without Quotes
**Input:** Content without representative quotes

**Expected Output:** Blog post formatted correctly, with warnings about missing quotes

**Verification:** Formatting still correct, warnings provided

### Edge Case 4: Very Long Content
**Input:** Extensive content with many sections

**Expected Output:** Properly formatted long blog post with all sections

**Verification:** All sections formatted correctly, no formatting breaks

## Common Issues and Solutions

### Issue: Formatting doesn't match visual examples
**Solution:** 
- Re-reference visual example files
- Check Python script parameters
- Verify color, font, and spacing settings
- Run validation step

### Issue: Missing required sections
**Solution:**
- Check structure against `references/phenom-blog-structure.md`
- Ensure all required sections are created
- Verify table of contents matches sections

### Issue: Metrics not formatted correctly
**Solution:**
- Use `format_phenom_blog.py` metrics formatting
- Ensure percentages and numbers are bolded
- Check before/after comparisons are formatted

### Issue: Quotes not attributed
**Solution:**
- Ensure attribution is included in quote format
- Check that attribution includes name and title
- Verify quote formatting matches Phenom style

### Issue: Links not working
**Solution:**
- Check link format in Markdown (proper syntax)
- Verify hyperlinks in Word document
- Ensure URLs are valid and accessible

### Issue: Output files not generated
**Solution:**
- Check Python dependencies (python-docx installed)
- Verify script paths are correct
- Check file permissions for output directory

## Validation Checklist

Before delivering outputs, verify:

- [ ] Word document generated successfully
- [ ] Markdown file generated successfully
- [ ] Formatting matches visual examples (visual comparison)
- [ ] Introduction section present and formatted correctly
- [ ] Table of contents present and matches all sections
- [ ] All case study sections follow Phenom structure
- [ ] Quotes are properly formatted and attributed
- [ ] Metrics are formatted correctly (bold, specific numbers)
- [ ] Links are properly formatted and functional
- [ ] Conclusion section present with call-to-action
- [ ] Writing style matches Phenom guidelines (tone, voice)
- [ ] All required elements present (no missing sections)
- [ ] Validation script passes (no critical issues)


