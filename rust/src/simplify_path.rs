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
    // Additional edge cases
    #[case("/", "/")] // Root directory only
    #[case("//", "/")] // Multiple slashes at root
    #[case("/a/..", "/")] // Single dir then up
    #[case("/a/b/..", "/a")] // Go up one level
    // Complex nested cases
    #[case("/a/b/../../../c", "/c")] // Multiple ups beyond root
    #[case("/a/./b/../c/", "/a/c")] // Mixed . and ..
    // Special directory names
    #[case("/...", "/...")] // Three dots (valid dir name)
    #[case("/.../...", "/.../...")] // Multiple three-dot dirs
    #[case("/a-b_c.txt", "/a-b_c.txt")] // Special characters
    // Additional boundary cases
    #[case("/a/../b/../c/../..", "/")] // Multiple back-and-forth
    #[case("/./././.", "/")] // Multiple current directory references
    fn case(#[case] path: String, #[case] expected: String) {
        let actual = Solution::simplify_path(path);
        assert_eq!(actual, expected);
    }
}
