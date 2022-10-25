public class Main{
	public static void main (String[]args){
		String s="()())()";
		int prefixSum=0;
// 		The logic is that every time the number of opening brackets should be
//      greater than or equal to closing brackets and in the end opening brackets
//      should be equal to closing brackets
//     So we assign closing bracket as -1 and opening as 1;
		for(int i=0;i<s.length();i++){
			int value=(s.charAt(i)==')')?-1:1;
			prefixSum+=value;
			if(prefixSum<0){
				System.out.println("Invalid String ");
				return;
			}
		}
		if(prefixSum==0){
				System.out.println("Valid String ");
				
			}
			else{
				System.out.println("Invalid String ");
			}
		
		
	}
	
}
