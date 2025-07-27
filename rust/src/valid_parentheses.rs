//! Solution for https://leetcode.com/problems/valid-parentheses
//! 20. Valid Parentheses

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut parens: Vec<char> = Vec::new();
        for c in s.chars() {
            if c == '(' || c == '{' || c == '[' {
                parens.push(c);
            } else if c == ')' {
                if parens.len() == 0 {
                    return false;
                }
                if parens.pop().unwrap() != '(' {
                    return false;
                }
            } else if c == ']' {
                if parens.len() == 0 {
                    return false;
                }
                if parens.pop().unwrap() != '[' {
                    return false;
                }
            } else if c == '}' {
                if parens.len() == 0 {
                    return false;
                }
                if parens.pop().unwrap() != '{' {
                    return false;
                }
            }

        }
        return parens.len() == 0; 
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
    fn case(#[case] s: String, #[case] expected: bool) {
        let actual = Solution::is_valid(s);
        assert_eq!(actual, expected);
    }
}
