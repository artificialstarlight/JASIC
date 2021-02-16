/* 
---COMMENT----
    Classes are public unless specified otherwise
    and begins and ends must be on the same line as the 
    statement.
*/

public class Test {
	public static void main(String[] args) { 
	/* You can use the above shortcut instead of public static void main. */
		System.out.println("Hello World! Imma count to 10!")
	for(int I=0; I<10; I+=1){
		System.out.println("Count is" + String.valueOf(I))
		/* The above is shortcut for String.valueOf(x) */
		divisibleBy2(I)
		}
	public void divisibleBy2(int X) {
	/* This is a method */
		if(X % 2) == 0 {
			System.out.println("It's divisible by 2!")
		}
		

}
}