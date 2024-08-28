class Solution {
  // Time: O(n)
  // Space: O(1)
  romanToInt(s) {
    const d = { I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000 };
    const n = s.length;
    let total = 0;
    let a = 0;

    while (a < n) {
      if (a < n - 1 && d[s[a]] < d[s[a + 1]]) {
        total += d[s[a + 1]] - d[s[a]];
        a += 2;
      } else {
        total += d[s[a]];
        a += 1;
      }
    }

    return total;
  }
}
