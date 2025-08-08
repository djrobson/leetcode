# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Common Commands

### Rust (rust/ directory)
- `cargo test` - Run all tests for Rust solutions
- `cargo test <module_name>` - Run tests for a specific module (e.g., `cargo test permutations`)
- `cargo check` - Quick compile check without building binaries
- `cargo build` - Build the project
- `cargo clippy` - Run linter for code quality checks

### Python (python/ directory)
- `pytest` - Run all Python tests
- `pytest <test_file.py>` - Run a specific test file (e.g., `pytest test_21.py`)
- `pytest -v` - Run tests with verbose output

## Repository Structure

This is a dual-language LeetCode solutions repository with:

- **rust/**: Rust solutions using cargo-leet template structure
  - Each problem is implemented as a module in `src/` with comprehensive test cases using rstest
  - Solutions follow LeetCode's expected signature format but include a local `Solution` struct for testing
  - Uses Rust 1.79 (pinned to match LeetCode environment)
  
- **python/**: Python solutions with test files
  - Each file follows pattern `test_<problem_number>.py`
  - Uses pytest framework for testing
  - Includes complete problem implementations with test cases

## Code Patterns

### Rust Solutions
- Each module contains the solution implementation plus a local `Solution` struct for testing
- Uses `rstest` for parameterized testing with multiple test cases
- Code above `// << ---------------- Code below here is only for local use ---------------- >>` comment is the actual LeetCode submission
- All modules are declared in `lib.rs`

### Python Solutions  
- Each test file contains both the `Solution` class and test functions
- Uses pytest for testing framework
- Includes custom data structures when needed (e.g., `ListNode` for linked list problems)
- Test functions follow pattern `test_<description>()`

## Dependencies

### Rust
- `rstest` - For parameterized testing
- `cargo-leet` - LeetCode template tooling
- `rand`, `regex` - Common algorithm dependencies

### Python
- `pytest` - Testing framework
- Standard library typing for type hints