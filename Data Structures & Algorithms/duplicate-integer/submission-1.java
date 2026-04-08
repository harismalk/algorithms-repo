class Solution {
    public boolean hasDuplicate(int[] nums) {
 for(int x = 0; x< nums.length; x++){
    for(int y = x+1; y < nums.length; y++){
        if(nums[x] == nums[y]){
            return true;
        }
    }
 }
     return false;

    }
}


