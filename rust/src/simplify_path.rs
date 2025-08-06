//! Solution for https://leetcode.com/problems/simplify-path
//! 71. Simplify Path

impl Solution {
    pub fn simplify_path(path: String) -> String {
        let filtered: Vec<&str> = path
            .split('/')
            .filter(|dir| !dir.is_empty() && !dir.eq(&"."))
            .collect();

        let mut dirs_removed: Vec<&str> = Vec::new();
        for dir in filtered {
            if dir.eq("..") {
                if !dirs_removed.is_empty() {
                    dirs_removed.pop();
                }
            } else {
                dirs_removed.push(dir)
            }
        }

        let mut result = "/".to_string();
        result.push_str(&dirs_removed.join("/"));
        result
    }
}

// << ---------------- Code below here is only for local use ---------------- >>

pub struct Solution;

#[cfg(test)]
mod tests {
    use super::*;

    use rstest::rstest;

    #[rstest]
    #[case("/home/", "/home")]
    #[case("/home/user/Documents/../../Pictures", "/home/Pictures")]
    #[case("/home//////user/", "/home/user")]
    #[case("/home//foo/", "/home/foo")]
    #[case("/home/user/Documents/../Pictures", "/home/user/Pictures")]
    #[case("/../", "/")]
    #[case("/..", "/")]
    #[case("/.", "/")]
    #[case("/.../a/../b/c/../d/./", "/.../b/d")]
    fn case(#[case] path: String, #[case] expected: String) {
        let actual = Solution::simplify_path(path);
        assert_eq!(actual, expected);
    }
}
