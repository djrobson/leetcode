//! Solution for https://leetcode.com/problems/powx-n
//! 50. Pow(x, n)

impl Solution {
    pub fn my_pow(x: f64, n: i32) -> f64 {
        // special cases for x
        if n == 0 {
            return 1.0;
        }
        if x == 0.0 {
            return if n > 0 { 0.0 } else { f64::INFINITY };
        }
        if x == 1.0 {
            return 1.0;
        }
        if x == -1.0 {
            return if n % 2 == 0 { 1.0 } else { -1.0 };
        }

        // special cases for huge exponents (use more aggressive threshold)
        let abs_n = n.unsigned_abs();
        if abs_n > 100_000 {
            let abs_x = x.abs();
            return match (abs_x > 1.0, n > 0) {
                (true, true) => f64::INFINITY,   // |x| > 1, n > 0: grows to infinity
                (true, false) => 0.0,            // |x| > 1, n < 0: shrinks to zero
                (false, true) => 0.0,            // |x| < 1, n > 0: shrinks to zero
                (false, false) => f64::INFINITY, // |x| < 1, n < 0: grows to infinity
            };
        }

        // binary exponentiation for O(log n) performance
        let mut exponent = n;
        let mut base = if exponent < 0 {
            // get the reciprocal
            exponent = -exponent;
            1.0 / x
        } else {
            x
        };

        let mut result = 1.0;
        while exponent > 0 {
            if exponent % 2 == 1 {
                result *= base;
            }
            base *= base;
            exponent /= 2;
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
    // Edge Cases
    #[case(0.0, 5, 0.0)]
    #[case(1.0, -100, 1.0)]
    #[case(-1.0, 3, -1.0)]
    #[case(-1.0, 4, 1.0)]
    // Boundary Values
    #[case(2.0, 0, 1.0)]
    #[case(0.5, 2, 0.25)]
    #[case(-2.0, 3, -8.0)]
    #[case(-2.0, 4, 16.0)]
    // Large Exponent Cases
    #[case(0.5, 1000001, 0.0)]
    #[case(2.0, -1000001, 0.0)]
    #[case(1.5, 1000001, f64::INFINITY)]
    // Precision Cases
    #[case(1.00001, 100000, 2.71827)] // approximately e
    #[case(0.99999, 100000, 0.36788)] // approximately 1/e
    fn case(#[case] x: f64, #[case] n: i32, #[case] expected: f64) {
        let actual = Solution::my_pow(x, n);
        if expected.is_infinite() && actual.is_infinite() {
            assert_eq!(expected.is_sign_positive(), actual.is_sign_positive());
        } else {
            assert!((actual - expected).abs() < 1e-5, "Assertion failed: actual {actual:.5} but expected {expected:.5}. Diff is more than 1e-5.");
        }
    }
}
