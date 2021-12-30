import java.util.ArrayList;
import java.util.Scanner;

public class solve_1 {
    public static void main(String [] args) {
        Scanner input = new Scanner(System.in);
        int x=input.nextInt();
        ArrayList<Integer> num= new ArrayList<>();
        while (x!=0){
            num.add(x);
            x=input.nextInt();
        }
        for (int i = num.size()-1; i>=0 ; i--) {
            System.out.println(num.get(i));
        }
    }
}
/**
* @author Mohammad YousefiPour - Github.com/myp79
*/