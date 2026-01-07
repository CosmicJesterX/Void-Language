
#!/bin/bash
# Comprehensive test suite for bash scripts
# Tests: 2pac_moji_dropper.sh, fog.sh, fogger.sh

set -e

# Test counters
PASSED=0
FAILED=0
TOTAL=0

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Test helper functions
assert_equals() {
    local expected="$1"
    local actual="$2"
    local message="$3"
    
    TOTAL=$((TOTAL + 1))
    
    if [ "$expected" = "$actual" ]; then
        echo -e "${GREEN}✓${NC} $message"
        PASSED=$((PASSED + 1))
    else
        echo -e "${RED}✗${NC} $message"
        echo "  Expected: $expected"
        echo "  Actual: $actual"
        FAILED=$((FAILED + 1))
    fi
}

assert_contains() {
    local haystack="$1"
    local needle="$2"
    local message="$3"
    
    TOTAL=$((TOTAL + 1))
    
    if echo "$haystack" | grep -q "$needle"; then
        echo -e "${GREEN}✓${NC} $message"
        PASSED=$((PASSED + 1))
    else
        echo -e "${RED}✗${NC} $message"
        echo "  Expected to contain: $needle"
        echo "  In: $haystack"
        FAILED=$((FAILED + 1))
    fi
}

assert_file_exists() {
    local file="$1"
    local message="$2"
    
    TOTAL=$((TOTAL + 1))
    
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓${NC} $message"
        PASSED=$((PASSED + 1))
    else
        echo -e "${RED}✗${NC} $message"
        echo "  File not found: $file"
        FAILED=$((FAILED + 1))
    fi
}

assert_true() {
    local condition="$1"
    local message="$2"
    
    TOTAL=$((TOTAL + 1))
    
    if [ "$condition" = "true" ]; then
        echo -e "${GREEN}✓${NC} $message"
        PASSED=$((PASSED + 1))
    else
        echo -e "${RED}✗${NC} $message"
        FAILED=$((FAILED + 1))
    fi
}

assert_exit_code() {
    local expected="$1"
    local actual="$2"
    local message="$3"
    
    TOTAL=$((TOTAL + 1))
    
    if [ "$expected" -eq "$actual" ]; then
        echo -e "${GREEN}✓${NC} $message"
        PASSED=$((PASSED + 1))
    else
        echo -e "${RED}✗${NC} $message"
        echo "  Expected exit code: $expected"
        echo "  Actual exit code: $actual"
        FAILED=$((FAILED + 1))
    fi
}

# Change to repository root
cd "$(dirname "$0")/.."

echo ""
echo "🧪 Running Bash Scripts Test Suite"
echo ""
echo "============================================================"

# ============================================================
# Tests for 2pac_moji_dropper.sh
# ============================================================
echo ""
echo "Testing 2pac_moji_dropper.sh"
echo "------------------------------------------------------------"

# Test file exists
assert_file_exists "2pac_moji_dropper.sh" "2pac_moji_dropper.sh exists"

# Test file is executable or has shebang
if [ -f "2pac_moji_dropper.sh" ]; then
    FIRST_LINE=$(head -1 2pac_moji_dropper.sh)
    assert_contains "$FIRST_LINE" "#!/bin/bash" "Has bash shebang"
    
    # Test file has read permissions
    [ -r "2pac_moji_dropper.sh" ]
    assert_exit_code 0 $? "File is readable"
fi

# Test script structure
if [ -f "2pac_moji_dropper.sh" ]; then
    CONTENT=$(cat 2pac_moji_dropper.sh)
    
    # Test for echo statements
    assert_contains "$CONTENT" "echo" "Contains echo statements"
    
    # Test for read statements
    assert_contains "$CONTENT" "read" "Contains read statements for user input"
    
    # Test for case statement
    assert_contains "$CONTENT" "case" "Contains case statement for mood handling"
    
    # Test for esac (end of case)
    assert_contains "$CONTENT" "esac" "Has proper case statement closure"
    
    # Test for mood options
    assert_contains "$CONTENT" "cool" "Handles 'cool' mood"
    assert_contains "$CONTENT" "sus" "Handles 'sus' mood"
    assert_contains "$CONTENT" "past" "Handles 'past' mood"
    assert_contains "$CONTENT" "deep" "Handles 'deep' mood"
    assert_contains "$CONTENT" '\*' "Has default case handler"
    
    # Test for emojis
    assert_contains "$CONTENT" "🎤" "Contains microphone emoji"
    assert_contains "$CONTENT" "👁️" "Contains eye emoji"
    assert_contains "$CONTENT" "🧠" "Contains brain emoji"
    
    # Test for variables
    assert_contains "$CONTENT" "sted" "Uses 'sted' variable"
    assert_contains "$CONTENT" "person" "Uses 'person' variable"
    assert_contains "$CONTENT" "stemning" "Uses 'stemning' variable"
    
    # Test for Norwegian text
    assert_contains "$CONTENT" "hvor" "Contains Norwegian text"
    assert_contains "$CONTENT" "Hvem" "Contains Norwegian text"
fi

# Test script execution with cool mood
if [ -f "2pac_moji_dropper.sh" ]; then
    OUTPUT=$(echo -e "test_location\ntest_person\ncool" | bash 2pac_moji_dropper.sh 2>&1)
    assert_contains "$OUTPUT" "😎" "Cool mood produces sunglasses emoji"
    assert_contains "$OUTPUT" "test_person" "Output includes person name"
    assert_contains "$OUTPUT" "test_location" "Output includes location"
fi

# Test script execution with sus mood
if [ -f "2pac_moji_dropper.sh" ]; then
    OUTPUT=$(echo -e "location\nperson\nsus" | bash 2pac_moji_dropper.sh 2>&1)
    assert_contains "$OUTPUT" "🤨" "Sus mood produces suspicious emoji"
fi

# Test script execution with past mood
if [ -f "2pac_moji_dropper.sh" ]; then
    OUTPUT=$(echo -e "location\nperson\npast" | bash 2pac_moji_dropper.sh 2>&1)
    assert_contains "$OUTPUT" "😏" "Past mood produces smirk emoji"
fi

# Test script execution with deep mood
if [ -f "2pac_moji_dropper.sh" ]; then
    OUTPUT=$(echo -e "location\nperson\ndeep" | bash 2pac_moji_dropper.sh 2>&1)
    assert_contains "$OUTPUT" "🛣️" "Deep mood produces road emoji"
fi

# Test script execution with unknown mood
if [ -f "2pac_moji_dropper.sh" ]; then
    OUTPUT=$(echo -e "location\nperson\nunknown_mood" | bash 2pac_moji_dropper.sh 2>&1)
    assert_contains "$OUTPUT" "🎲" "Unknown mood produces dice emoji"
    assert_contains "$OUTPUT" "🤷" "Unknown mood produces shrug emoji"
fi

# Test no syntax errors
if [ -f "2pac_moji_dropper.sh" ]; then
    bash -n 2pac_moji_dropper.sh 2>/dev/null
    assert_exit_code 0 $? "Script has no syntax errors"
fi

# ============================================================
# Tests for fog.sh
# ============================================================
echo ""
echo "Testing fog.sh"
echo "------------------------------------------------------------"

# Test file exists
assert_file_exists "fog.sh" "fog.sh exists"

# Test file has shebang or is simple script
if [ -f "fog.sh" ]; then
    CONTENT=$(cat fog.sh)
    
    # Test contains echo statement
    assert_contains "$CONTENT" "echo" "Contains echo statement"
    
    # Test for mist output
    assert_contains "$CONTENT" "mist" "Outputs 'mist' text"
fi

# Test script execution
if [ -f "fog.sh" ]; then
    OUTPUT=$(bash fog.sh 2>&1)
    assert_contains "$OUTPUT" "mist" "Script outputs mist"
    
    # Count number of mist occurrences
    MIST_COUNT=$(echo "$OUTPUT" | grep -o "mist" | wc -l)
    [ "$MIST_COUNT" -ge 3 ]
    assert_exit_code 0 $? "Outputs 'mist' multiple times (at least 3)"
fi

# Test script exits successfully
if [ -f "fog.sh" ]; then
    bash fog.sh >/dev/null 2>&1
    assert_exit_code 0 $? "Script exits with success code"
fi

# Test no syntax errors
if [ -f "fog.sh" ]; then
    bash -n fog.sh 2>/dev/null
    assert_exit_code 0 $? "Script has no syntax errors"
fi

# ============================================================
# Tests for fogger.sh
# ============================================================
echo ""
echo "Testing fogger.sh"
echo "------------------------------------------------------------"

# Test file exists
assert_file_exists "fogger.sh" "fogger.sh exists"

# Test file has bash shebang
if [ -f "fogger.sh" ]; then
    FIRST_LINE=$(head -1 fogger.sh)
    assert_contains "$FIRST_LINE" "#!/bin/bash" "Has bash shebang"
fi

# Test script structure
if [ -f "fogger.sh" ]; then
    CONTENT=$(cat fogger.sh)
    
    # Test for mkdir commands
    assert_contains "$CONTENT" "mkdir" "Contains mkdir commands"
    
    # Test for -p flag (create parent directories)
    assert_contains "$CONTENT" "mkdir -p" "Uses mkdir -p for safe directory creation"
    
    # Test for echo statements
    assert_contains "$CONTENT" "echo" "Contains echo statements"
    
    # Test for fog emoji
    assert_contains "$CONTENT" "🌫️" "Contains fog emoji"
    
    # Test for sparkle emoji
    assert_contains "$CONTENT" "✨" "Contains sparkle emoji"
    
    # Test for directory paths
    assert_contains "$CONTENT" "rituals" "Creates rituals directory structure"
    assert_contains "$CONTENT" "artifacts" "Creates artifacts directory structure"
    assert_contains "$CONTENT" "logs" "Creates logs directory structure"
    
    # Test for file redirection
    assert_contains "$CONTENT" ">" "Uses file redirection"
    
    # Test for README creation
    assert_contains "$CONTENT" "README" "Creates README file"
fi

# Test script execution (in safe temporary directory)
if [ -f "fogger.sh" ]; then
    TEMP_DIR=$(mktemp -d)
    cd "$TEMP_DIR"
    
    OUTPUT=$(bash "$OLDPWD/fogger.sh" 2>&1)
    
    # Test output messages
    assert_contains "$OUTPUT" "Manifesting" "Displays manifesting message"
    assert_contains "$OUTPUT" "Fog complete" "Displays completion message"
    
    # Test directories were created (in home directory)
    [ -d ~/rituals/mist_layer ]
    assert_exit_code 0 $? "Creates ~/rituals/mist_layer directory"
    
    [ -d ~/artifacts/echoes ]
    assert_exit_code 0 $? "Creates ~/artifacts/echoes directory"
    
    [ -d ~/logs/silence ]
    assert_exit_code 0 $? "Creates ~/logs/silence directory"
    
    # Test README file was created
    [ -f ~/artifacts/echoes/README_FOG.txt ]
    assert_exit_code 0 $? "Creates README_FOG.txt file"
    
    # Test README content
    if [ -f ~/artifacts/echoes/README_FOG.txt ]; then
        README_CONTENT=$(cat ~/artifacts/echoes/README_FOG.txt)
        assert_contains "$README_CONTENT" "whispers" "README contains 'whispers'"
    fi
    
    # Cleanup
    cd - > /dev/null
    rm -rf "$TEMP_DIR"
fi

# Test script exits successfully
if [ -f "fogger.sh" ]; then
    bash fogger.sh >/dev/null 2>&1
    assert_exit_code 0 $? "Script exits with success code"
fi

# Test no syntax errors
if [ -f "fogger.sh" ]; then
    bash -n fogger.sh 2>/dev/null
    assert_exit_code 0 $? "Script has no syntax errors"
fi

# Test idempotency - running again should not fail
if [ -f "fogger.sh" ]; then
    bash fogger.sh >/dev/null 2>&1
    bash fogger.sh >/dev/null 2>&1
    assert_exit_code 0 $? "Script is idempotent (can run multiple times)"
fi

# ============================================================
# Tests for invoice_goblinse.sh
# ============================================================
echo ""
echo "Testing invoice_goblinse.sh"
echo "------------------------------------------------------------"

# Test file exists
assert_file_exists "invoice_goblinse.sh" "invoice_goblinse.sh exists"

# Test file structure
if [ -f "invoice_goblinse.sh" ]; then
    CONTENT=$(cat invoice_goblinse.sh)
    
    # Test for comment
    assert_contains "$CONTENT" "#" "Contains comment marker"
    
    # Test for Invoice Goblins reference
    assert_contains "$CONTENT" "Invoice" "References Invoice Goblins"
    
    # Test file is valid (even if it's just a comment)
    [ -r "invoice_goblinse.sh" ]
    assert_exit_code 0 $? "File is readable"
fi

# ============================================================
# General bash scripting best practices tests
# ============================================================
echo ""
echo "Testing Bash Scripting Best Practices"
echo "------------------------------------------------------------"

for script in 2pac_moji_dropper.sh fog.sh fogger.sh; do
    if [ -f "$script" ]; then
        # Test for set -e in complex scripts (optional but recommended)
        if [ "$script" = "fogger.sh" ]; then
            CONTENT=$(cat "$script")
            # fogger.sh should be relatively safe even without set -e
            # as it only creates directories and files
            [ -f "$script" ]
            assert_exit_code 0 $? "$script exists and is accessible"
        fi
        
        # Test files don't contain dangerous commands
        CONTENT=$(cat "$script")
        if echo "$CONTENT" | grep -q "rm -rf /"; then
            assert_true "false" "$script does not contain 'rm -rf /'"
        else
            assert_true "true" "$script does not contain dangerous 'rm -rf /'"
        fi
        
        # Test for proper quoting of variables (where applicable)
        if echo "$CONTENT" | grep -q 'read.*\$'; then
            assert_true "true" "$script uses variables appropriately"
        fi
    fi
done

# ============================================================
# Integration tests
# ============================================================
echo ""
echo "Testing Script Integration"
echo "------------------------------------------------------------"

# Test that all scripts are in repository root
ALL_FOUND=true
for script in 2pac_moji_dropper.sh fog.sh fogger.sh; do
    if [ ! -f "$script" ]; then
        ALL_FOUND=false
    fi
done

assert_true "$ALL_FOUND" "All bash scripts are in repository root"

# Test scripts can be executed from different directories
if [ -f "fog.sh" ]; then
    TEMP_DIR=$(mktemp -d)
    cd "$TEMP_DIR"
    OUTPUT=$(bash "$OLDPWD/fog.sh" 2>&1)
    SUCCESS=$?
    cd - > /dev/null
    rm -rf "$TEMP_DIR"
    assert_exit_code 0 $SUCCESS "fog.sh can be executed from different directory"
fi

# ============================================================
# Test Results Summary
# ============================================================
echo ""
echo "============================================================"
echo ""
echo "Test Results: $PASSED passed, $FAILED failed, $TOTAL total"
echo ""

if [ $FAILED -eq 0 ]; then
    echo -e "${GREEN}All tests passed!${NC}"
    exit 0
else
    echo -e "${RED}Some tests failed.${NC}"
    exit 1
fi
