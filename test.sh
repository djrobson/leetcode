#!/bin/bash
# LeetCode Solutions Test Runner for WSL/Linux

set -e  # Exit on any error

echo "🦀 Running Rust tests..."
cd rust
if cargo test; then
    echo "✅ Rust tests passed"
else
    echo "❌ Rust tests failed"
    exit 1
fi
cd ..

echo
echo "🐍 Running Python tests..."
cd python
if pytest -v; then
    echo "✅ Python tests passed"
else
    echo "❌ Python tests failed"
    exit 1
fi
cd ..

echo
echo "🎉 All tests passed!"
