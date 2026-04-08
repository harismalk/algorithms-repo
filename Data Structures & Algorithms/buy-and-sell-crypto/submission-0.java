class Solution {
    public int maxProfit(int[] prices) {
    
      int flag = 0;

      for(int x = 0; x < prices.length; x++){
        for(int y = x+1; y<prices.length; y++){
            if(prices[y]-prices[x] > flag){
                flag = prices[y]- prices[x];
            }
        }
      }
      return flag;
    }
}
