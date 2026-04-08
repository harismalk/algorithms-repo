class Solution {
    public double myPow(double x, int n) {
            double answer = 1;
        if(n == 0){
            return answer;
        }
        else if(n > 0){
            for(int z = 0; z < n; z++){
                answer = answer * x;
            }

        } else{
            int index = n*(-1);
            double denom = 1;
            for(int z = 0; z < index; z++){
                denom = denom * x;
            }
            answer = 1/denom;
            return answer;
        }
                return answer;

    }
}
