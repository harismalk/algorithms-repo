class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        int index = 0;

        while(index < nums.length){
            int product = 1; 
        
            for(int x = 0; x < nums.length; x++){
                if(x == index){
                    continue;
                }
                product = product * nums[x];
            }
            res[index] = product;
            index++;
        }
    return res;
    }
}  
