class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> prevMap = new HashMap<>();

        for(int x = 0; x < nums.length; x++){
            int num = nums[x];
            int diff = target - num;

            if(prevMap.containsKey(diff)){
                return new int []{prevMap.get(diff), x};
            }
            prevMap.put(num, x);
        }
        return new int [] {};
    }
}
