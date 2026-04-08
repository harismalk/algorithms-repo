class Solution {
    public int[] twoSum(int[] numbers, int target) {
        for(int x = 0; x < numbers.length; x++){
            for(int y = x+1; y < numbers.length; y++){
                if((numbers[x] + numbers[y] == target) && numbers[x] != numbers[y]){
                    return new int[] {x+1, y+1};
                }
            }
        }
        return new int []{};
    }
}
