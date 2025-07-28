//! Solution for https://leetcode.com/problems/permutations
//! 46. Permutations

impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        todo!("Fill in body")
    }
}

// << ---------------- Code below here is only for local use ---------------- >>

pub struct Solution;

#[cfg(test)]
mod tests {
    use super::*;

    use rstest::rstest;

    #[rstest]
    #[case(vec![1,2,3], vec![vec![1,2,3],vec![1,3,2],vec![2,1,3],vec![2,3,1],vec![3,1,2],vec![3,2,1]])]
    #[case(vec![0,1], vec![vec![0,1],vec![1,0]])]
    #[case(vec![1], vec![vec![1]])]
    fn case(#[case] nums: Vec<i32>, #[case] expected: Vec<Vec<i32>>) {
        let actual = Solution::permute(nums);
        assert_eq!(actual, expected);
    }
}
