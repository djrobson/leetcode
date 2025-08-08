//! Solution for https://leetcode.com/problems/remove-duplicates-from-sorted-array
//! 26. Remove Duplicates from Sorted Array

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        nums.dedup();

        nums.len() as i32
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
    // Edge Cases
    #[case([1].to_vec(), 1, [1].to_vec())] // Single element
    #[case([1,1,1,1,1].to_vec(), 1, [1].to_vec())] // All same elements
    // Boundary Values
    #[case([1,2,3,4,5,6,7,8,9,10].to_vec(), 10, [1,2,3,4,5,6,7,8,9,10].to_vec())] // No duplicates
    #[case([-100].to_vec(), 1, [-100].to_vec())] // Minimum constraint value
    #[case([100].to_vec(), 1, [100].to_vec())] // Maximum constraint value
    #[case([-100,-100,100,100].to_vec(), 2, [-100,100].to_vec())] // Min/max with duplicates
    // Various patterns
    #[case([1,1,2,2,3,3].to_vec(), 3, [1,2,3].to_vec())] // Pairs of duplicates
    #[case([1,2,2,2,3].to_vec(), 3, [1,2,3].to_vec())] // Multiple consecutive duplicates
    #[case([-3,-1,0,0,0,3,3].to_vec(), 4, [-3,-1,0,3].to_vec())] // Mixed positive/negative
    fn test_remove_dup(
        #[case] mut nums: Vec<i32>,
        #[case] expected: i32,
        #[case] output: Vec<i32>,
    ) {
        let actual = Solution::remove_duplicates(&mut nums);
        assert_eq!(actual, expected);
        assert_eq!(nums, output);
    }
}
