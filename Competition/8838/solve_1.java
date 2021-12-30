import java.util.Scanner;

public class solve_1 {
    public static void main(String [] args){
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        String s = input.next();
        String all = "";
        for (int i = 0; i < n; i++) {
           all=all.concat("copy of ");
        }
        all=all.concat(s);
        System.out.print(all);
    }
}
/**
* @author Mohammad YousefiPour - Github.com/myp79
*/
