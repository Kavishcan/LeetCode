function twoSum1(nums, target) {
  for (let n = 0; n < nums.length; n++) {
    for (let m = 0; m < nums.length - n; m++) {
      if (n !== m) {
        if (nums[n] + nums[m] === target) {
          return [n, m];
        }
      }
    }
  }
}
