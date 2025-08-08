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

| Problem | Rust | Python | Difficulty | Time | Space | Optimal |
|---------|------|--------|------------|------|-------|---------|
| [6. Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion) | ❌ | ✅ | Medium | O(n) | O(n) | ✅ |
| [15. 3Sum](https://leetcode.com/problems/3sum) | ❌ | ✅ | Medium | O(n²) | O(1) | ✅ |
| [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number) | ❌ | ✅ | Medium | O(4ⁿ) | O(4ⁿ) | ✅ |
| [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses) | ✅ | ❌ | Easy | O(n) | O(n) | ✅ |
| [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists) | ❌ | ✅ | Easy | O(m+n) | O(1) | ✅ |
| [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses) | ❌ | ✅ | Medium | O(4ⁿ/√n) | O(4ⁿ/√n) | ✅ |
| [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs) | ❌ | ✅ | Medium | O(n) | O(1) | ✅ |
| [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array) | ✅ | ❌ | Easy | O(n) | O(1) | ✅ |
| [46. Permutations](https://leetcode.com/problems/permutations) | ✅ | ❌ | Medium | O(n!×n) | O(n!×n) | ✅ |
| [48. Rotate Image](https://leetcode.com/problems/rotate-image) | ❌ | ✅ | Medium | O(n²) | O(1) | ✅ |
| [50. Pow(x, n)](https://leetcode.com/problems/powx-n) | ✅ | ❌ | Medium | O(log n) | O(1) | ✅ |
| [71. Simplify Path](https://leetcode.com/problems/simplify-path) | ✅ | ❌ | Medium | O(n) | O(n) | ✅ |
| [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self) | ❌ | ✅ | Medium | O(n) | O(1) | ✅ |
| [334. Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence) | ❌ | ✅ | Medium | O(n) | O(1) | ✅ |
| [345. Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string) | ❌ | ✅ | Medium | O(n) | O(n) | ✅ |
| [1071. Greatest Common Divisor of Strings](https://leetcode.com/problems/greatest-common-divisor-of-strings) | ❌ | ✅ | Easy | O(m+n) | O(1) | ✅ |

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

### Setting up the development environment

1. Install uv (if not already installed):
   ```bash
   # Windows
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

   # macOS/Linux
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Create virtual environment and install dependencies:
   ```bash
   uv venv
   uv pip install pytest flake8 black isort pre-commit
   ```

3. Activate the virtual environment:
   ```bash
   # Windows
   .venv\Scripts\activate

   # macOS/Linux
   source .venv/bin/activate
   ```

4. Install pre-commit hooks:
   ```bash
   pre-commit install
   ```

5. (Optional) Run hooks on all files:
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
