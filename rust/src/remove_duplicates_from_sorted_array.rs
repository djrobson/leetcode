//! Solution for https://leetcode.com/problems/remove-duplicates-from-sorted-array
//! 26. Remove Duplicates from Sorted Array

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        nums.dedup();

        return nums.len() as i32;
    }

}

// << ---------------- Code below here is only for local use ---------------- >>

pub struct Solution;

#[cfg(test)]
mod tests {
    use super::*;

    use rstest::rstest;

    #[rstest]
    #[case([1,1,2].to_vec(), 2, [1,2].to_vec())]
    #[case([0,0,1,1,1,2,2,3,3,4].to_vec(), 5, [0,1,2,3,4].to_vec())]
    fn test_remove_dup(#[case] mut nums: Vec<i32>, #[case] expected: i32, #[case] output: Vec<i32>) {
        let actual = Solution::remove_duplicates(&mut nums);
        assert_eq!(actual, expected);
        assert_eq!(nums,output);
    }
}
