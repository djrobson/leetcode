//! Solution for https://leetcode.com/problems/powx-n
//! 50. Pow(x, n)

impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {

        // special cases for x
        if n == 0 {
            return 1.0;
        }
        if x == 1.0 {
            return 1.0;
        }
        if x == -1.0 {
            if n & 1 == 1 {
                return x;
            } else {
                return -x;
            }
        }

        // special cases for huge exponents
        if n > 1_000_000 {
            if x < 1.0 {
                return 0.0;
            } else if n == 1 {
                return x
            } else {
                return f64::MAX;
            }

        }
        if n < -1_000_000 {
            if x >= 2.0 {
                return 0.0;
            } else if x < 1.0 {
                return f64::MAX;
            }
        }

        // general solution using loops
        let mut exponent = n;
        let mut result = 1.0;
        let mult = 
            if exponent < 0 {
                // get the reciprocal
                exponent = -exponent;
                1.0/x
            } else {
                x
            };
        for _ in 0..exponent {
            result = result * mult;
        }
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
    #[case(2.00000, 10, 1024.00000)]
    #[case(2.10000, 3, 9.26100)]
    #[case(2.00000, -2, 0.25000)]
    fn case(#[case] x: f64, #[case] n: i32, #[case] expected: f64) {
        let actual = Solution::my_pow(x, n);
        assert!((actual - expected).abs() < 1e-5, "Assertion failed: actual {actual:.5} but expected {expected:.5}. Diff is more than 1e-5.");
    }
}
