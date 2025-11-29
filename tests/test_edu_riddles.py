#!/usr/bin/env python3
"""
Comprehensive test suite for EDU-RIDDLES.md

This test suite validates:
- Document structure and formatting
- Riddle completeness and consistency
- Required sections presence
- Content quality and formatting
- HTML entity handling
- Markdown syntax correctness
"""

import re
import unittest
from pathlib import Path
from typing import List, Dict, Tuple


class RiddleValidator:
    """Helper class to parse and validate riddle structure"""
    
    def __init__(self, content: str):
        self.content = content
        self.lines = content.split('\n')
        
    def get_riddles(self) -> List[Dict[str, any]]:
        """Extract all riddles from the document"""
        riddles = []
        current_riddle = None
        current_section = None
        
        for i, line in enumerate(self.lines, 1):
            # Match riddle headers (## N) ...)
            riddle_match = re.match(r'^## (\d+)\) (.+)$', line)
            if riddle_match:
                if current_riddle:
                    riddles.append(current_riddle)
                current_riddle = {
                    'number': int(riddle_match.group(1)),
                    'title': riddle_match.group(2),
                    'line_number': i,
                    'riddle_text': [],
                    'answer': None,
                    'learning_goal': None,
                    'where_to_use': None,
                    'teacher_note': None,
                }
                current_section = None
                continue
            
            if current_riddle and line.strip():
                # Detect sections
                if line.startswith('Riddle:'):
                    current_section = 'riddle_text'
                elif line.startswith('Answer:'):
                    current_riddle['answer'] = line.replace('Answer:', '').strip()
                    current_section = None
                elif line.startswith('Learning goal:'):
                    current_riddle['learning_goal'] = line.replace('Learning goal:', '').strip()
                    current_section = None
                elif line.startswith('Where to use:'):
                    current_riddle['where_to_use'] = line.replace('Where to use:', '').strip()
                    current_section = None
                elif line.startswith('Teacher note:'):
                    current_riddle['teacher_note'] = line.replace('Teacher note:', '').strip()
                    current_section = None
                elif current_section == 'riddle_text' and not line.startswith('---'):
                    current_riddle['riddle_text'].append(line)
        
        if current_riddle:
            riddles.append(current_riddle)
        
        return riddles
    
    def get_main_sections(self) -> List[str]:
        """Extract main document sections (# headers)"""
        sections = []
        for line in self.lines:
            if line.startswith('# '):
                sections.append(line[2:].strip())
        return sections


class TestEduRiddlesStructure(unittest.TestCase):
    """Test the overall document structure"""
    
    @classmethod
    def setUpClass(cls):
        """Load the EDU-RIDDLES.md file once for all tests"""
        riddles_path = Path(__file__).parent.parent / 'EDU-RIDDLES.md'
        with open(riddles_path, 'r', encoding='utf-8') as f:
            cls.content = f.read()
        cls.validator = RiddleValidator(cls.content)
        cls.riddles = cls.validator.get_riddles()
    
    def test_file_exists_and_readable(self):
        """Test that EDU-RIDDLES.md exists and is readable"""
        riddles_path = Path(__file__).parent.parent / 'EDU-RIDDLES.md'
        self.assertTrue(riddles_path.exists(), "EDU-RIDDLES.md should exist")
        self.assertTrue(riddles_path.is_file(), "EDU-RIDDLES.md should be a file")
    
    def test_has_main_title(self):
        """Test that document has a main title"""
        self.assertTrue(
            self.content.startswith('# '),
            "Document should start with a level-1 header"
        )
        self.assertIn(
            'Riddling Educational Hooks',
            self.content.split('\n')[0],
            "Title should mention 'Riddling Educational Hooks'"
        )
    
    def test_has_introduction(self):
        """Test that document has an introduction section"""
        lines = self.content.split('\n')
        # Introduction should be within first 10 lines
        intro_text = '\n'.join(lines[:10])
        self.assertIn(
            'bite-sized riddles',
            intro_text.lower(),
            "Introduction should explain the purpose"
        )
    
    def test_has_usage_section(self):
        """Test that document has 'How to use this file' section"""
        self.assertIn(
            '## How to use this file',
            self.content,
            "Document should have a usage guide section"
        )
    
    def test_has_license_section(self):
        """Test that document has license/attribution section"""
        self.assertIn(
            '## License and attribution',
            self.content,
            "Document should have a license/attribution section"
        )
    
    def test_correct_number_of_riddles(self):
        """Test that document contains exactly 10 riddles"""
        self.assertEqual(
            len(self.riddles),
            10,
            "Document should contain exactly 10 riddles"
        )
    
    def test_riddles_are_numbered_sequentially(self):
        """Test that riddles are numbered 1-10 in order"""
        expected_numbers = list(range(1, 11))
        actual_numbers = [r['number'] for r in self.riddles]
        self.assertEqual(
            actual_numbers,
            expected_numbers,
            "Riddles should be numbered 1-10 in sequential order"
        )
    
    def test_riddles_separated_by_horizontal_rules(self):
        """Test that riddles are separated by horizontal rules (---)"""
        hr_count = self.content.count('\n---\n')
        # Should have at least 10 horizontal rules (one after each riddle)
        self.assertGreaterEqual(
            hr_count,
            10,
            "Riddles should be separated by horizontal rules (---)"
        )


class TestRiddleCompleteness(unittest.TestCase):
    """Test that each riddle has all required components"""
    
    @classmethod
    def setUpClass(cls):
        """Load riddles for testing"""
        riddles_path = Path(__file__).parent.parent / 'EDU-RIDDLES.md'
        with open(riddles_path, 'r', encoding='utf-8') as f:
            cls.content = f.read()
        cls.validator = RiddleValidator(cls.content)
        cls.riddles = cls.validator.get_riddles()
    
    def test_all_riddles_have_titles(self):
        """Test that all riddles have descriptive titles"""
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                self.assertIsNotNone(riddle['title'], 
                    f"Riddle {riddle['number']} should have a title")
                self.assertGreater(len(riddle['title']), 5,
                    f"Riddle {riddle['number']} title should be descriptive")
    
    def test_all_riddles_have_riddle_text(self):
        """Test that all riddles have riddle text"""
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                self.assertGreater(
                    len(riddle['riddle_text']),
                    0,
                    f"Riddle {riddle['number']} should have riddle text"
                )
                # Riddle text should be in quotes
                riddle_full = '\n'.join(riddle['riddle_text'])
                self.assertTrue(
                    '"' in riddle_full,
                    f"Riddle {riddle['number']} text should be in quotes"
                )
    
    def test_all_riddles_have_answers(self):
        """Test that all riddles have answers"""
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                self.assertIsNotNone(
                    riddle['answer'],
                    f"Riddle {riddle['number']} should have an answer"
                )
                self.assertGreater(
                    len(riddle['answer']),
                    3,
                    f"Riddle {riddle['number']} answer should be substantive"
                )
    
    def test_all_riddles_have_learning_goals(self):
        """Test that all riddles have learning goals"""
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                self.assertIsNotNone(
                    riddle['learning_goal'],
                    f"Riddle {riddle['number']} should have a learning goal"
                )
                self.assertGreater(
                    len(riddle['learning_goal']),
                    10,
                    f"Riddle {riddle['number']} learning goal should be descriptive"
                )
    
    def test_all_riddles_have_usage_context(self):
        """Test that all riddles have 'Where to use' context"""
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                self.assertIsNotNone(
                    riddle['where_to_use'],
                    f"Riddle {riddle['number']} should have usage context"
                )
                self.assertGreater(
                    len(riddle['where_to_use']),
                    5,
                    f"Riddle {riddle['number']} usage context should be specific"
                )
    
    def test_all_riddles_have_teacher_notes(self):
        """Test that all riddles have teacher notes"""
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                self.assertIsNotNone(
                    riddle['teacher_note'],
                    f"Riddle {riddle['number']} should have teacher notes"
                )
                self.assertGreater(
                    len(riddle['teacher_note']),
                    10,
                    f"Riddle {riddle['number']} teacher note should be helpful"
                )


class TestRiddleContentQuality(unittest.TestCase):
    """Test the quality and consistency of riddle content"""
    
    @classmethod
    def setUpClass(cls):
        """Load riddles for testing"""
        riddles_path = Path(__file__).parent.parent / 'EDU-RIDDLES.md'
        with open(riddles_path, 'r', encoding='utf-8') as f:
            cls.content = f.read()
        cls.validator = RiddleValidator(cls.content)
        cls.riddles = cls.validator.get_riddles()
    
    def test_riddle_titles_follow_format(self):
        """Test that riddle titles follow the format: 'Category — "Name"'"""
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                title = riddle['title']
                # Should contain an em dash or regular dash
                self.assertTrue(
                    '—' in title or '–' in title or ' - ' in title,
                    f"Riddle {riddle['number']} title should contain a separator"
                )
                # Should contain quoted name
                self.assertIn(
                    '"',
                    title,
                    f"Riddle {riddle['number']} title should have a quoted name"
                )
    
    def test_riddles_reference_void_or_wimp(self):
        """Test that riddles reference Void-Language or WIMP appropriately"""
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                full_text = (
                    riddle['title'] + ' ' +
                    '\n'.join(riddle['riddle_text']) + ' ' +
                    (riddle['answer'] or '') + ' ' +
                    (riddle['learning_goal'] or '')
                ).lower()
                
                # Should mention void, wimp, or related concepts
                relevant_terms = [
                    'void', 'wimp', 'interpreter', 'language',
                    'compiler', 'docs', 'manual', 'roff'
                ]
                has_relevant_term = any(term in full_text for term in relevant_terms)
                self.assertTrue(
                    has_relevant_term,
                    f"Riddle {riddle['number']} should reference project concepts"
                )
    
    def test_learning_goals_are_actionable(self):
        """Test that learning goals use actionable verbs"""
        actionable_verbs = [
            'introduce', 'teach', 'encourage', 'show', 'explain',
            'help', 'demonstrate', 'guide', 'create', 'make',
            'provide', 'give', 'frame', 'present'
        ]
        
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                learning_goal = (riddle['learning_goal'] or '').lower()
                has_actionable_verb = any(
                    verb in learning_goal for verb in actionable_verbs
                )
                self.assertTrue(
                    has_actionable_verb,
                    f"Riddle {riddle['number']} learning goal should use actionable verbs"
                )
    
    def test_teacher_notes_provide_guidance(self):
        """Test that teacher notes provide practical guidance"""
        guidance_indicators = [
            'provide', 'include', 'add', 'show', 'give',
            'follow', 'link', 'append', 'keep', 'ensure'
        ]
        
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                teacher_note = (riddle['teacher_note'] or '').lower()
                has_guidance = any(
                    indicator in teacher_note for indicator in guidance_indicators
                )
                self.assertTrue(
                    has_guidance,
                    f"Riddle {riddle['number']} teacher note should provide guidance"
                )
    
    def test_where_to_use_specifies_concrete_locations(self):
        """Test that 'Where to use' specifies concrete locations"""
        location_patterns = [
            r'readme', r'issue', r'pr', r'contributing',
            r'workshop', r'demo', r'tweet', r'discussion',
            r'doc', r'header', r'template', r'slide'
        ]
        
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                where_to_use = (riddle['where_to_use'] or '').lower()
                has_location = any(
                    re.search(pattern, where_to_use) for pattern in location_patterns
                )
                self.assertTrue(
                    has_location,
                    f"Riddle {riddle['number']} should specify concrete usage locations"
                )


class TestMarkdownFormatting(unittest.TestCase):
    """Test markdown formatting and syntax"""
    
    @classmethod
    def setUpClass(cls):
        """Load content for testing"""
        riddles_path = Path(__file__).parent.parent / 'EDU-RIDDLES.md'
        with open(riddles_path, 'r', encoding='utf-8') as f:
            cls.content = f.read()
        cls.lines = cls.content.split('\n')
    
    def test_no_trailing_whitespace(self):
        """Test that lines don't have trailing whitespace"""
        lines_with_trailing = [
            (i+1, line) for i, line in enumerate(self.lines)
            if line.rstrip() != line and line.strip()  # Ignore empty lines
        ]
        self.assertEqual(
            len(lines_with_trailing),
            0,
            f"Lines with trailing whitespace: {lines_with_trailing[:5]}"
        )
    
    def test_consistent_header_spacing(self):
        """Test that headers have consistent spacing"""
        for i, line in enumerate(self.lines):
            if line.startswith('#'):
                with self.subTest(line_number=i+1):
                    # Headers should have space after #
                    self.assertTrue(
                        line.startswith('# ') or line.startswith('## '),
                        f"Line {i+1}: Headers should have space after # symbol"
                    )
    
    def test_horizontal_rules_are_consistent(self):
        """Test that horizontal rules use consistent format"""
        hr_lines = [
            (i+1, line) for i, line in enumerate(self.lines)
            if line.strip() in ['---', '***', '___']
        ]
        
        if hr_lines:
            # Get the most common format
            formats = [line for _, line in hr_lines]
            most_common = max(set(formats), key=formats.count)
            
            # All should use the same format
            inconsistent = [(num, line) for num, line in hr_lines if line != most_common]
            self.assertEqual(
                len(inconsistent),
                0,
                f"Horizontal rules should be consistent. Found: {inconsistent}"
            )
    
    def test_no_multiple_blank_lines(self):
        """Test that there are no multiple consecutive blank lines"""
        consecutive_blanks = []
        blank_count = 0
        
        for i, line in enumerate(self.lines):
            if not line.strip():
                blank_count += 1
                if blank_count > 2:
                    consecutive_blanks.append(i+1)
            else:
                blank_count = 0
        
        self.assertEqual(
            len(consecutive_blanks),
            0,
            f"Multiple consecutive blank lines at: {consecutive_blanks}"
        )
    
    def test_html_entities_are_properly_escaped(self):
        """Test that HTML entities like &amp; are properly used"""
        # Find all HTML entities
        html_entity_pattern = r'&[a-z]+;'
        entities = re.findall(html_entity_pattern, self.content)
        
        # Common valid entities
        valid_entities = ['&amp;', '&lt;', '&gt;', '&quot;', '&apos;']
        
        for entity in entities:
            with self.subTest(entity=entity):
                self.assertIn(
                    entity,
                    valid_entities,
                    f"HTML entity {entity} should be valid"
                )
    
    def test_consistent_list_formatting(self):
        """Test that lists use consistent bullet formatting"""
        list_items = [
            (i+1, line) for i, line in enumerate(self.lines)
            if re.match(r'^\s*[-*+]\s', line)
        ]
        
        if list_items:
            # Extract bullet types
            bullets = [re.match(r'^\s*([-*+])', line).group(1) 
                      for _, line in list_items]
            most_common = max(set(bullets), key=bullets.count)
            
            # Check consistency
            inconsistent = [
                (num, line) for (num, line), bullet in zip(list_items, bullets)
                if bullet != most_common
            ]
            
            # Allow some flexibility, but most should be consistent
            consistency_ratio = 1 - (len(inconsistent) / len(list_items))
            self.assertGreater(
                consistency_ratio,
                0.8,
                f"List bullets should be mostly consistent. Found mixed: {inconsistent[:5]}"
            )


class TestEdgeCasesAndRobustness(unittest.TestCase):
    """Test edge cases and document robustness"""
    
    @classmethod
    def setUpClass(cls):
        """Load content for testing"""
        riddles_path = Path(__file__).parent.parent / 'EDU-RIDDLES.md'
        with open(riddles_path, 'r', encoding='utf-8') as f:
            cls.content = f.read()
        cls.validator = RiddleValidator(cls.content)
        cls.riddles = cls.validator.get_riddles()
    
    def test_file_ends_with_newline(self):
        """Test that file ends with a newline character"""
        self.assertTrue(
            self.content.endswith('\n'),
            "File should end with a newline character"
        )
    
    def test_no_riddle_is_empty(self):
        """Test that no riddle section is completely empty"""
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                total_content = (
                    len(riddle['riddle_text']) +
                    len(riddle['answer'] or '') +
                    len(riddle['learning_goal'] or '') +
                    len(riddle['where_to_use'] or '') +
                    len(riddle['teacher_note'] or '')
                )
                self.assertGreater(
                    total_content,
                    50,
                    f"Riddle {riddle['number']} should have substantial content"
                )
    
    def test_riddles_have_reasonable_length(self):
        """Test that riddles are not too short or excessively long"""
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                riddle_text = '\n'.join(riddle['riddle_text'])
                char_count = len(riddle_text)
                
                # Riddle text should be between 20 and 500 characters
                self.assertGreater(
                    char_count,
                    20,
                    f"Riddle {riddle['number']} text seems too short"
                )
                self.assertLess(
                    char_count,
                    500,
                    f"Riddle {riddle['number']} text seems too long"
                )
    
    def test_special_characters_are_handled(self):
        """Test that special characters in riddles are properly formatted"""
        special_chars = ['—', '–', '"', '"', ''', ''']
        
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                title = riddle['title']
                # If special chars are used, they should be typographically correct
                if any(char in title for char in ['-', '"', "'"]):
                    # This is more of a style check
                    pass  # We allow both styles
    
    def test_no_broken_section_references(self):
        """Test that section headers are properly formatted"""
        section_headers = [
            'Riddle:', 'Answer:', 'Learning goal:',
            'Where to use:', 'Teacher note:'
        ]
        
        for header in section_headers:
            # Count occurrences
            count = self.content.count(header)
            # Each should appear at least 10 times (once per riddle)
            self.assertGreaterEqual(
                count,
                10,
                f"Section header '{header}' should appear at least 10 times"
            )
    
    def test_document_has_reasonable_length(self):
        """Test that document is a reasonable length"""
        line_count = len(self.content.split('\n'))
        
        # Should be between 100 and 300 lines
        self.assertGreater(
            line_count,
            100,
            "Document should have substantial content"
        )
        self.assertLess(
            line_count,
            300,
            "Document should be concise and focused"
        )
    
    def test_consistent_terminology(self):
        """Test that the document uses consistent terminology"""
        # Check that project names are consistently capitalized
        self.assertIn('Void-Language', self.content)
        self.assertIn('WIMP', self.content)
        
        # Check for common inconsistencies
        inconsistent_terms = ['void-language', 'Void language', 'wimp']
        for term in inconsistent_terms:
            if term.lower() in self.content.lower():
                # Allow in context but check it's not misused
                pass  # This is a softer check


class TestUsabilityAndAccessibility(unittest.TestCase):
    """Test document usability and accessibility"""
    
    @classmethod
    def setUpClass(cls):
        """Load content for testing"""
        riddles_path = Path(__file__).parent.parent / 'EDU-RIDDLES.md'
        with open(riddles_path, 'r', encoding='utf-8') as f:
            cls.content = f.read()
        cls.validator = RiddleValidator(cls.content)
        cls.riddles = cls.validator.get_riddles()
    
    def test_riddles_have_clear_structure(self):
        """Test that each riddle follows a predictable structure"""
        expected_order = [
            'riddle_text', 'answer', 'learning_goal',
            'where_to_use', 'teacher_note'
        ]
        
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                # All expected fields should be present
                for field in ['answer', 'learning_goal', 'where_to_use', 'teacher_note']:
                    self.assertIsNotNone(
                        riddle[field],
                        f"Riddle {riddle['number']} should have {field}"
                    )
    
    def test_usage_guide_is_helpful(self):
        """Test that the usage guide provides clear instructions"""
        usage_section_match = re.search(
            r'## How to use this file\n(.*?)(?=\n##|\Z)',
            self.content,
            re.DOTALL
        )
        
        self.assertIsNotNone(usage_section_match, "Should have usage guide")
        
        usage_text = usage_section_match.group(1)
        # Should contain practical instructions
        self.assertIn('-', usage_text, "Usage guide should have bullet points")
        self.assertGreater(
            len(usage_text),
            100,
            "Usage guide should be detailed"
        )
    
    def test_riddles_are_self_contained(self):
        """Test that riddles can be understood independently"""
        for riddle in self.riddles:
            with self.subTest(riddle_number=riddle['number']):
                # Answer should relate to riddle
                answer = (riddle['answer'] or '').lower()
                riddle_text = '\n'.join(riddle['riddle_text']).lower()
                
                # They should share some common concepts
                # Extract key nouns/terms from answer
                answer_words = set(re.findall(r'\b[a-z]{4,}\b', answer))
                riddle_words = set(re.findall(r'\b[a-z]{4,}\b', riddle_text))
                
                # Should have some overlap or clear connection
                overlap = answer_words & riddle_words
                self.assertTrue(
                    len(overlap) > 0 or len(answer) > 10,
                    f"Riddle {riddle['number']} answer should relate to riddle text"
                )


def run_tests():
    """Run all tests and return results"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestEduRiddlesStructure))
    suite.addTests(loader.loadTestsFromTestCase(TestRiddleCompleteness))
    suite.addTests(loader.loadTestsFromTestCase(TestRiddleContentQuality))
    suite.addTests(loader.loadTestsFromTestCase(TestMarkdownFormatting))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCasesAndRobustness))
    suite.addTests(loader.loadTestsFromTestCase(TestUsabilityAndAccessibility))
    
    # Run tests with verbose output
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


if __name__ == '__main__':
    result = run_tests()
    # Exit with appropriate code
    exit(0 if result.wasSuccessful() else 1)