# Test Suite for EDU-RIDDLES.md

This directory contains comprehensive validation tests for the `EDU-RIDDLES.md` documentation file.

## Overview

The test suite validates:
- **Document Structure**: Ensures proper markdown formatting and organization
- **Riddle Completeness**: Verifies each riddle has all required sections
- **Content Quality**: Checks that content is meaningful and consistent
- **Markdown Formatting**: Validates proper markdown syntax and styling
- **Edge Cases**: Tests robustness and handles edge cases
- **Usability**: Ensures the document is accessible and user-friendly

## Running the Tests

### Basic Usage

Run all tests:
```bash
python3 tests/test_edu_riddles.py
```

### Verbose Output

Run with detailed output:
```bash
python3 tests/test_edu_riddles.py -v
```

### Run Specific Test Classes

Run only structure tests:
```bash
python3 -m unittest tests.test_edu_riddles.TestEduRiddlesStructure
```

Run only completeness tests:
```bash
python3 -m unittest tests.test_edu_riddles.TestRiddleCompleteness
```

### Run Individual Tests

Run a specific test:
```bash
python3 -m unittest tests.test_edu_riddles.TestEduRiddlesStructure.test_has_main_title
```

## Test Categories

### 1. TestEduRiddlesStructure
Validates the overall document structure including:
- Main title presence
- Introduction section
- Usage guide section
- License/attribution section
- Correct number of riddles (10)
- Sequential numbering
- Horizontal rule separators

### 2. TestRiddleCompleteness
Ensures each riddle contains all required components:
- Descriptive title
- Riddle text (in quotes)
- Clear answer
- Learning goal
- Usage context ("Where to use")
- Teacher notes

### 3. TestRiddleContentQuality
Validates the quality of riddle content:
- Title format consistency
- Relevant project references (Void-Language/WIMP)
- Actionable learning goals
- Practical teacher guidance
- Concrete usage locations

### 4. TestMarkdownFormatting
Checks markdown syntax and formatting:
- No trailing whitespace
- Consistent header spacing
- Consistent horizontal rules
- No multiple blank lines
- Proper HTML entity escaping
- Consistent list formatting

### 5. TestEdgeCasesAndRobustness
Tests edge cases and document robustness:
- File ends with newline
- No empty riddles
- Reasonable riddle length (20-500 chars)
- Proper section headers
- Appropriate document length (100-300 lines)
- Consistent terminology

### 6. TestUsabilityAndAccessibility
Ensures document usability:
- Clear riddle structure
- Helpful usage guide
- Self-contained riddles with clear connections

## Test Output

Successful test run example: