class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for(int row = 0; row < 3; row++){
            for(int col = 0; col < 4; col++){
                if(matrix[row][col] == target){
                    return true;
                }
            }
        }
        return false;
    }
}
