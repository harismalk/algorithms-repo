class Solution {
    public int maxArea(int[] heights) {
        int result = 0;
        int left = 0; 
        int right = heights.length - 1;

        while(left < right){
            int width = right - left;
            int length = Math.min(heights[left], heights[right]);
            int area = width * length;
            result = Math.max(result, area);

            if(heights[left] > heights[right]){
                right--;
            } else{
                left++;
            }
        }
        return result;
    }
}
