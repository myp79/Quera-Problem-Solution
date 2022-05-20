import java.util.Scanner;

public class solve_1 {
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {

        int x = input.nextInt();
        int y = input.nextInt();
        for (int i = x; i <= y; i++) {
            int counter = 0;
            for (int j = 2; j < i; j++) {
                if (i % j == 0) {
                    counter++;
                }
            }
            if (counter == 0 && i != 1) {
                System.out.println(i);
            }

        }
    }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */