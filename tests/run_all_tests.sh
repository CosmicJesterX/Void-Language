#!/bin/bash
# Master test runner for all test suites

set -e

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

TOTAL_SUITES=0
PASSED_SUITES=0
FAILED_SUITES=0

echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║         VOID-LANGUAGE COMPREHENSIVE TEST SUITE             ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Change to repository root
cd "$(dirname "$0")/.."

# Function to run a test suite
run_suite() {
    local name="$1"
    local command="$2"
    
    TOTAL_SUITES=$((TOTAL_SUITES + 1))
    
    echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
    echo -e "${YELLOW}Running: $name${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"
    echo ""
    
    if eval "$command"; then
        echo ""
        echo -e "${GREEN}✓ $name: PASSED${NC}"
        PASSED_SUITES=$((PASSED_SUITES + 1))
        return 0
    else
        echo ""
        echo -e "${RED}✗ $name: FAILED${NC}"
        FAILED_SUITES=$((FAILED_SUITES + 1))
        return 1
    fi
}

# Run all test suites
echo "Starting test execution..."
echo ""

# JavaScript tests
run_suite "jesterLoop.js Tests" "node tests/test_jesterLoop.js" || true
run_suite "jesterOracle.js Tests" "node tests/test_jesterOracle.js" || true
run_suite "voidchain-prototype.js Tests" "node tests/test_voidchain.js" || true

# Bash script tests
run_suite "Bash Scripts Tests" "bash tests/test_bash_scripts.sh" || true

# Python/Config tests
run_suite "Configuration Files Tests" "python3 tests/test_config_files.py" || true
run_suite "EDU-RIDDLES.md Tests" "python3 tests/test_edu_riddles.py" || true

# Final summary
echo ""
echo "╔════════════════════════════════════════════════════════════╗"
echo "║                    TEST SUITE SUMMARY                      ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "Total Test Suites: $TOTAL_SUITES"
echo -e "${GREEN}Passed: $PASSED_SUITES${NC}"
echo -e "${RED}Failed: $FAILED_SUITES${NC}"
echo ""

if [ $FAILED_SUITES -eq 0 ]; then
    echo -e "${GREEN}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║                  ALL TESTS PASSED! 🎉                      ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════════════════════╝${NC}"
    exit 0
else
    echo -e "${RED}╔════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${RED}║              SOME TESTS FAILED - SEE ABOVE                 ║${NC}"
    echo -e "${RED}╚════════════════════════════════════════════════════════════╝${NC}"
    exit 1
fi
