//! Solution for https://leetcode.com/problems/permutations
//! 46. Permutations

impl Solution {
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut permutations = Vec::new();
        fn descend(pin_offset: usize, input: &mut Vec<i32>, output: &mut Vec<Vec<i32>>) {
            if pin_offset == input.len() {
                // we've pinned and swapped all the way to the end, save a clone
                output.push(input.clone())
            }
            for i in pin_offset..input.len() {
                // for each spot we can swap with, swap it and descend, then unswap it
                input.swap(pin_offset, i);
                descend(pin_offset + 1, input, output);
                input.swap(pin_offset, i);
            }
        }

        let mut input = nums;
        descend(0, &mut input, &mut permutations);
        permutations
    }
}

// << ---------------- Code below here is only for local use ---------------- >>

pub struct Solution;

#[cfg(test)]
mod tests {
    use super::*;

    use rstest::rstest;

    #[rstest]
    #[case(vec![1,2,3], vec![vec![1,2,3],vec![1,3,2],vec![2,1,3],vec![2,3,1],vec![3,2,1],vec![3,1,2]])]
    #[case(vec![0,1], vec![vec![0,1],vec![1,0]])]
    #[case(vec![1], vec![vec![1]])]
    // Negative numbers
    #[case(vec![-1], vec![vec![-1]])]
    #[case(vec![-1, -2], vec![vec![-1,-2], vec![-2,-1]])]
    #[case(vec![-10, 10], vec![vec![-10,10], vec![10,-10]])]
    // Boundary constraints (n=1 to 6, values -10 to 10)
    #[case(vec![-10], vec![vec![-10]])]
    #[case(vec![10], vec![vec![10]])]
    #[case(vec![-1, 0, 1], vec![vec![-1,0,1],vec![-1,1,0],vec![0,-1,1],vec![0,1,-1],vec![1,0,-1],vec![1,-1,0]])]
    // Descending input order
    #[case(vec![5,4,3,2], vec![vec![5,4,3,2],vec![5,4,2,3],vec![5,3,4,2],vec![5,3,2,4],vec![5,2,3,4],vec![5,2,4,3],vec![4,5,3,2],vec![4,5,2,3],vec![4,3,5,2],vec![4,3,2,5],vec![4,2,5,3],vec![4,2,3,5],vec![3,4,5,2],vec![3,4,2,5],vec![3,5,4,2],vec![3,5,2,4],vec![3,2,4,5],vec![3,2,5,4],vec![2,4,3,5],vec![2,4,5,3],vec![2,3,4,5],vec![2,3,5,4],vec![2,5,3,4],vec![2,5,4,3]])]
    fn case(#[case] nums: Vec<i32>, #[case] expected: Vec<Vec<i32>>) {
        let mut actual = Solution::permute(nums);
        let mut expected = expected;
        actual.sort();
        expected.sort();
        assert_eq!(actual, expected);
    }
}
