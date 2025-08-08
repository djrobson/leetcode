//! Solution for https://leetcode.com/problems/valid-parentheses
//! 20. Valid Parentheses

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut parens: Vec<char> = Vec::new();
        for c in s.chars() {
            if c == '(' || c == '{' || c == '[' {
                parens.push(c);
            } else if c == ')' {
                if parens.is_empty() {
                    return false;
                }
                if parens.pop().unwrap() != '(' {
                    return false;
                }
            } else if c == ']' {
                if parens.is_empty() {
                    return false;
                }
                if parens.pop().unwrap() != '[' {
                    return false;
                }
            } else if c == '}' {
                if parens.is_empty() {
                    return false;
                }
                if parens.pop().unwrap() != '{' {
                    return false;
                }
            }
        }
        parens.is_empty()
    }
}

// << ---------------- Code below here is only for local use ---------------- >>

pub struct Solution;

#[cfg(test)]
mod tests {
    use super::*;

    use rstest::rstest;

    #[rstest]
    #[case("()", true)]
    #[case("()[]{}", true)]
    #[case("(]", false)]
    #[case("([])", true)]
    #[case("([)]", false)]
    // Edge Cases
    #[case("", true)] // Empty string
    #[case("(", false)] // Single opening
    #[case(")", false)] // Single closing
    #[case("{", false)] // Single opening brace
    #[case("]", false)] // Single closing bracket
    // Unbalanced cases
    #[case("((((", false)] // All opening
    #[case("))))", false)] // All closing
    #[case("()(", false)] // Valid then invalid
    #[case("())", false)] // Valid then extra closing
    // Complex valid cases
    #[case("((()))", true)] // Nested parentheses
    #[case("{[()]}", true)] // All types nested
    #[case("()[]{}()[]{}", true)] // Multiple separate groups
    // Complex invalid cases
    #[case("({)}", false)] // Interleaved different types
    #[case("[{]}", false)] // Wrong closing order
    #[case("(((", false)] // Only opening parens
    #[case("{[}", false)] // Missing closing bracket
    fn case(#[case] s: String, #[case] expected: bool) {
        let actual = Solution::is_valid(s);
        assert_eq!(actual, expected);
    }
}
