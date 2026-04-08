class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        List<List<Integer>> res = new ArrayList <>();
        Arrays.sort(nums); // O(nlogn)

        for(int x = 0; x < nums.length; x++){
            if(x > 0 && nums[x] == nums[x-1]){
                continue;
            }

            int left = x+1;
            int right = nums.length - 1;

            while(left < right){

                int threeSum = nums[x] + nums[left] + nums[right];

                if(threeSum > 0){
                    right--;
                }
                else if(threeSum < 0){
                    left++;
                }
                else{
                    res.add(Arrays.asList(nums[x], nums[left], nums[right]));
                    left++;
                    right--;
                    while(left < right && nums[left] == nums[left-1]){
                        left++;
                    }
                }
            }

        }
        return res;

    }
}
