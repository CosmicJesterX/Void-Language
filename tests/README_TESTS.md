# Comprehensive Test Suite for Void-Language Repository

This directory contains extensive unit and integration tests for all components added in the recent commit.

## 📋 Overview

The test suite validates:
- **JavaScript Modules**: jesterLoop.js, jesterOracle.js, voidchain-prototype.js
- **Bash Scripts**: 2pac_moji_dropper.sh, fog.sh, fogger.sh
- **Configuration Files**: error_sorpe.JSON, orbital_clickstream.json, workflow.yaml
- **Documentation**: EDU-RIDDLES.md (existing test suite)

## 🚀 Quick Start

### Run All Tests
\`\`\`bash
cd tests
./run_all_tests.sh
\`\`\`

### Run Individual Test Suites

#### JavaScript Tests
\`\`\`bash
# Test jesterLoop.js
node tests/test_jesterLoop.js

# Test jesterOracle.js
node tests/test_jesterOracle.js

# Test voidchain-prototype.js
node tests/test_voidchain.js
\`\`\`

#### Bash Script Tests
\`\`\`bash
bash tests/test_bash_scripts.sh
\`\`\`

#### Configuration File Tests
\`\`\`bash
python3 tests/test_config_files.py

# With verbose output
python3 tests/test_config_files.py -v
\`\`\`

#### Documentation Tests
\`\`\`bash
python3 tests/test_edu_riddles.py
\`\`\`

## 📚 Test Suite Details

### 1. test_jesterLoop.js

**Tests for:** `jesterLoop.js` - Infinite loop with philosophical thoughts

**Coverage:**
- Source code structure and syntax validation
- jesterThoughts array content and structure
- startVoidDance function implementation
- Infinite loop behavior
- Random exit condition logic
- Runtime behavior and output
- Code quality and best practices
- Performance considerations
- Memory usage patterns

**Key Test Categories:**
- **Structure Tests (15)**: Validates code organization and components
- **Runtime Tests (10)**: Verifies execution behavior
- **Edge Cases (5)**: Tests robustness and error handling
- **Quality Tests (8)**: Checks coding standards
- **Performance Tests (2)**: Validates efficiency

**Total Tests:** 40+

### 2. test_jesterOracle.js

**Tests for:** `jesterOracle.js` - Interactive oracle with random responses

**Coverage:**
- Readline interface setup and configuration
- Response array structure and content
- User input handling (readline.question)
- Random response selection logic
- Output formatting and emoji usage
- Interface cleanup (readline.close)
- Runtime interaction with various inputs
- Edge cases (empty, long, special characters, Unicode)
- Code quality and Node.js best practices

**Key Test Categories:**
- **Structure Tests (12)**: Source code analysis
- **Runtime Tests (10)**: Interactive behavior
- **Edge Cases (6)**: Input validation and robustness
- **Quality Tests (8)**: Code standards
- **Performance Tests (2)**: Response time and cleanup

**Total Tests:** 38+

### 3. test_voidchain.js

**Tests for:** `voidchain-prototype.js` - Blockchain-like visitor tracking

**Coverage:**
- Module imports (os, readline, fs)
- Visitor ID generation
- OS platform detection
- Chain initialization and structure
- Block creation and sequencing
- File persistence (JSON serialization)
- Interactive prompts and user input
- Keyword-based response logic
- Timestamp handling (ISO 8601)
- Runtime behavior across platforms
- Edge cases and input validation
- File operations and cleanup

**Key Test Categories:**
- **Structure Tests (18)**: Code organization and components
- **Runtime Tests (15)**: Execution and file operations
- **Edge Cases (8)**: Input handling and robustness
- **Quality Tests (10)**: Code standards and documentation
- **Integration Tests (5)**: Cross-platform compatibility

**Total Tests:** 56+

### 4. test_bash_scripts.sh

**Tests for:** Bash scripts (2pac_moji_dropper.sh, fog.sh, fogger.sh, invoice_goblinse.sh)

**Coverage:**

#### 2pac_moji_dropper.sh (25+ tests)
- File existence and permissions
- Shebang and syntax validation
- Script structure (echo, read, case statements)
- Mood handling (cool, sus, past, deep, default)
- Emoji usage and output
- Variable usage (sted, person, stemning)
- Norwegian language content
- Input/output behavior for each mood
- Syntax error checking

#### fog.sh (6+ tests)
- File existence and structure
- Echo statement validation
- "mist" output verification
- Multiple occurrence testing
- Exit code validation
- Syntax checking

#### fogger.sh (15+ tests)
- Shebang validation
- mkdir -p usage for safe directory creation
- Directory structure creation (rituals, artifacts, logs)
- Emoji usage (fog, sparkle)
- File creation (README_FOG.txt)
- Content validation
- Idempotency (multiple runs)
- Exit code validation
- Syntax checking

#### General Best Practices (5+ tests)
- Dangerous command detection (rm -rf /)
- Variable quoting
- Cross-directory execution

**Total Tests:** 51+

### 5. test_config_files.py

**Tests for:** JSON/YAML configuration files

**Coverage:**

#### error_sorpe.JSON (20+ tests)
- File existence and validity
- JSON syntax validation
- Required field presence (status, error, entity)
- Error structure validation
- Error code (666)
- Error message content
- Mood field validation
- Entity field (cosmic_jester)
- Remedy array structure
- Remedy item content
- Fun fact field
- Playful tone validation
- Schema compliance

#### orbital_clickstream.json (18+ tests)
- File existence and validity
- Array structure validation
- Block structure (block, event, timestamp)
- Sequential block numbering
- Event field validation
- First block visitor arrival
- OS field in first block
- ISO 8601 timestamp format
- Chronological ordering
- Meaningful event descriptions
- User action recording
- Unique block numbers
- File size validation

#### workflow.yaml (4+ tests)
- File existence
- Read permissions
- Extension validation
- Content structure

#### General Tests (3+ tests)
- All JSON files syntax validation
- Naming convention tests
- Self-documenting structure

**Total Tests:** 45+

### 6. test_edu_riddles.py

**Tests for:** EDU-RIDDLES.md documentation (existing comprehensive suite)

**Coverage:** 696 lines of tests
- Document structure validation
- Riddle completeness checks
- Content quality verification
- Markdown formatting validation
- Edge cases and robustness
- Usability and accessibility

**Total Tests:** 60+

## 📊 Test Statistics Summary

| Test Suite | Tests | Categories | Lines of Code |
|------------|-------|------------|---------------|
| test_jesterLoop.js | 40+ | 5 | ~450 |
| test_jesterOracle.js | 38+ | 5 | ~520 |
| test_voidchain.js | 56+ | 5 | ~680 |
| test_bash_scripts.sh | 51+ | 4 | ~520 |
| test_config_files.py | 45+ | 4 | ~480 |
| test_edu_riddles.py | 60+ | 6 | 696 |
| **TOTAL** | **290+** | **29** | **~3,346** |

## 🎯 Test Coverage by File Type

### JavaScript Files (134+ tests)
- ✅ jesterLoop.js: 40+ tests
- ✅ jesterOracle.js: 38+ tests
- ✅ voidchain-prototype.js: 56+ tests

### Bash Scripts (51+ tests)
- ✅ 2pac_moji_dropper.sh: 25+ tests
- ✅ fog.sh: 6+ tests
- ✅ fogger.sh: 15+ tests
- ✅ invoice_goblinse.sh: 5+ tests

### Configuration Files (45+ tests)
- ✅ error_sorpe.JSON: 20+ tests
- ✅ orbital_clickstream.json: 18+ tests
- ✅ workflow.yaml: 4+ tests
- ✅ General validation: 3+ tests

### Documentation (60+ tests)
- ✅ EDU-RIDDLES.md: 60+ tests

## 🔧 Requirements

### JavaScript Tests
- Node.js (v12+)
- Core modules only (no external dependencies)

### Bash Script Tests
- Bash 4.0+
- Standard Unix utilities (grep, mkdir, cat, etc.)

### Python Tests
- Python 3.6+
- Standard library only (unittest, json, pathlib)

## 📖 Test Methodology

### Unit Testing Approach
1. **Source Code Analysis**: Parse and validate file structure
2. **Runtime Behavior**: Execute code with various inputs
3. **Edge Case Testing**: Test boundary conditions and error states
4. **Code Quality**: Validate best practices and conventions
5. **Integration**: Test interaction with system and other components

### Test Organization
- Each test suite is self-contained
- Tests use descriptive names following pattern: `test_<what>_<scenario>`
- Comprehensive assertion messages for debugging
- Cleanup after execution (temp files, directories)

### Coverage Goals
- ✅ **Happy Path**: Normal operation scenarios
- ✅ **Edge Cases**: Boundary conditions, empty inputs, special characters
- ✅ **Error Handling**: Invalid inputs, missing dependencies
- ✅ **Performance**: Execution time, memory usage
- ✅ **Security**: No dangerous operations, proper sanitization
- ✅ **Documentation**: Self-documenting code and clear structure

## 🐛 Debugging Failed Tests

### Enable Verbose Output

**JavaScript:**
\`\`\`bash
VERBOSE=1 node tests/test_jesterLoop.js
\`\`\`

**Python:**
\`\`\`bash
python3 tests/test_config_files.py -v
\`\`\`

**Bash:**
\`\`\`bash
# Bash tests already include detailed output
bash tests/test_bash_scripts.sh
\`\`\`

### Common Issues

1. **Timeout Errors**: Some tests spawn processes with timeouts
   - Increase timeout values if system is slow
   - Check that Node.js is installed and accessible

2. **File Permission Errors**: 
   - Ensure test scripts are executable: `chmod +x tests/*.sh tests/*.js`
   - Check file read permissions

3. **Module Not Found**:
   - Verify Node.js is installed: `node --version`
   - Verify Python 3 is installed: `python3 --version`

4. **Path Issues**:
   - Tests expect to run from repository root
   - Use `./tests/run_all_tests.sh` from root directory

## 🎨 Test Output

Tests provide color-coded output:
- 🟢 **Green ✓**: Test passed
- 🔴 **Red ✗**: Test failed
- 🟡 **Yellow**: Test suite header
- 🔵 **Blue**: Section separators

## 📝 Adding New Tests

### For JavaScript Modules

1. Create `tests/test_<module>.js`
2. Use Node.js assert module
3. Follow existing test structure:
   \`\`\`javascript
   function test(name, fn) { ... }
   test('description', () => {
       assert.ok(condition, 'message');
   });
   \`\`\`

### For Bash Scripts

1. Add to `tests/test_bash_scripts.sh`
2. Use assertion helpers:
   \`\`\`bash
   assert_equals expected actual "message"
   assert_contains haystack needle "message"
   assert_file_exists file "message"
   \`\`\`

### For Config Files

1. Add to `tests/test_config_files.py`
2. Create new test class:
   \`\`\`python
   class TestNewFile(unittest.TestCase):
       def test_something(self):
           self.assertTrue(condition, "message")
   \`\`\`

## 🔄 Continuous Integration

These tests are designed to run in CI environments:
- No external dependencies beyond core languages
- Deterministic (no random failures)
- Fast execution (< 30 seconds total)
- Clear error messages
- Exit codes for pass/fail

Add to your CI workflow:
\`\`\`yaml
- name: Run Tests
  run: |
    cd tests
    ./run_all_tests.sh
\`\`\`

## 📜 License

Tests follow the same license as the main repository.

## 🤝 Contributing

When adding new features:
1. Write tests first (TDD approach)
2. Ensure all existing tests pass
3. Add tests to appropriate suite
4. Update this README if adding new test categories
5. Run `./run_all_tests.sh` before submitting PR

---

**Happy Testing! 🎭🌀**

*"In the void, even tests must dance with uncertainty... but they should still pass."*
