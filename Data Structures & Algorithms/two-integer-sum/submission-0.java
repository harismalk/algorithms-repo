class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> previousCheck = new HashMap<>();

        for(int x = 0; x < nums.length; x++){
            int num = nums[x]; 
            int diff = target - num; 

            if(previousCheck.containsKey(diff)){
                return new int[] {previousCheck.get(diff), x};
            }

            previousCheck.put(num, x);
        }
        return new int[] {};
    }
}
