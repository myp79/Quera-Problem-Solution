import java.util.Scanner;

public class solve_1 {
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {

        String num = input.nextLine();
        for (int i = 0; i < num.length(); i++) {
            char n = num.charAt(i);
            System.out.print(Integer.parseInt(String.valueOf(n)) + ": ");
            for (int j = 0; j < Integer.parseInt(String.valueOf(n)); j++) {
                System.out.print((Integer.parseInt(String.valueOf(n))));
            }
            System.out.print("\n");
        }
    }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
