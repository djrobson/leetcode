@echo off
REM LeetCode Solutions Test Runner

echo 🦀 Running Rust tests...
cd rust
cargo test
if %errorlevel% neq 0 (
    echo ❌ Rust tests failed
    exit /b 1
)
echo ✅ Rust tests passed
cd ..

echo.
echo 🐍 Running Python tests...
cd python
pytest -v
if %errorlevel% neq 0 (
    echo ❌ Python tests failed
    exit /b 1
)
echo ✅ Python tests passed
cd ..

echo.
echo 🎉 All tests passed!
