import java.util.Scanner;

public class solve_1 {
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        int x = input.nextInt();
        x = (int) (Math.log(x) / Math.log(2));
        System.out.println((int) Math.pow(2, x + 1));
    }
}

/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
