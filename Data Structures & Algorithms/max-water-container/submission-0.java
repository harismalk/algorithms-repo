class Solution {
    public int maxArea(int[] heights) {
        
        int max = 0;
        for(int x = 0; x < heights.length; x++){
            for(int y = 0; y < heights.length; y++){

                int width = Math.abs(x-y);
                int length = Math.min(heights[x], heights[y]);
                int currentArea = width * length;

                if(currentArea > max){
                    max = currentArea;
                }
            }
        }
        return max;
    }
}
