 import edu.princeton.cs.algs4.*;
public class Main {

	public static void main(String[] args) {
		
		Comparable[] a = {2,3,4,11,3423,23,54};
		
		Selection.sort(a);
		
		
		for (int i = 0; i<a.length; i++){
			System.out.println(" " + a[i]);
		}

	}

}
