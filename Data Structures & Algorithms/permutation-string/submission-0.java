class Solution {
    public boolean checkInclusion(String s1, String s2) {
        
        HashSet<Character> prev = new HashSet<>();
        for(char c : s1.toCharArray()){
            prev.add(c);
        }
        int count = 0;
        int target = prev.size();

        for(int x = 0; x < s2.length(); x++){
            if(prev.contains(s2.charAt(x))){
                count++;
            }
        }
        return count == target;
    }
}
