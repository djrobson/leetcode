# LeetCode Solutions

A dual-language LeetCode solutions repository with comprehensive test coverage in both Rust and Python.

## Repository Structure

### Rust Solutions (`rust/`)
- **Framework**: cargo-leet template structure with comprehensive testing
- **Testing**: Uses `rstest` for parameterized testing with multiple test cases
- **Version**: Rust 1.79 (pinned to match LeetCode environment)
- **Pattern**: Each problem implemented as a module with local `Solution` struct

### Python Solutions (`python/`)  
- **Framework**: pytest with individual test files
- **Pattern**: Each file follows `test_<problem_number>.py` format
- **Testing**: Includes complete problem implementations with test cases

## Problem Solutions

| Problem | Rust | Python | Difficulty |
|---------|------|--------|------------|
| [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses) | ✅ | ❌ | Easy |
| [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array) | ✅ | ❌ | Easy |
| [46. Permutations](https://leetcode.com/problems/permutations) | ✅ | ❌ | Medium |
| [50. Pow(x, n)](https://leetcode.com/problems/powx-n) | ✅ | ❌ | Medium |
| [71. Simplify Path](https://leetcode.com/problems/simplify-path) | ✅ | ❌ | Medium |

## Running Tests

### All Tests
```bash
# Run script from root
./test.sh
```

### Rust Tests
```bash
cd rust
cargo test                    # All tests
cargo test <module_name>      # Specific module (e.g., cargo test permutations)
cargo check                   # Quick compile check
cargo clippy                  # Linter
```

### Python Tests  
```bash
cd python
pytest                        # All tests
pytest <test_file.py>         # Specific test file
pytest -v                     # Verbose output
```

## Code Patterns

### Rust
- Each module contains LeetCode submission code plus local testing infrastructure
- Code above the `// << ---- Code below here is only for local use ---- >>` comment is the actual LeetCode submission
- Uses `rstest` for comprehensive parameterized testing
- Follows cargo-leet template conventions

### Python
- Each test file contains both `Solution` class and test functions
- Includes custom data structures when needed (e.g., `ListNode` for linked lists)
- Test functions follow pattern `test_<description>()`

## Development

This repository uses:
- **Rust 1.79** (pinned via rust-toolchain.toml)
- **pytest** for Python testing
- **GitHub Actions** for CI/CD
- **pre-commit hooks** for automatic code formatting
- **Comprehensive test coverage** with edge cases and boundary testing

### Setting up pre-commit hooks

1. Install pre-commit:
   ```bash
   pip install pre-commit
   ```

2. Install the hooks:
   ```bash
   pre-commit install
   ```

3. (Optional) Run hooks on all files:
   ```bash
   pre-commit run --all-files
   ```

Now formatting checks will run automatically before each commit!

## Contributing

When adding new solutions:
1. Follow existing patterns for file structure and naming
2. Include comprehensive test cases covering edge cases
3. Add problem entry to this README table
4. Run tests to ensure everything passes