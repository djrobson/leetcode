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

fn main() {
    assert!(is_valid("()[]{}".to_string()));
    assert!(is_valid("()".to_string()));
    assert!(!is_valid(")".to_string()));
}