import java.util.Scanner;

public class solve_1 {
    static Scanner input = new Scanner(System.in);


    public static void main(String[] args) {

        String x = input.nextLine();
        StringBuilder y = new StringBuilder();
        for (int i = x.length() - 1; i >= 0; i--) {
            y.append(String.valueOf(x.charAt(i)));
        }
        if (x.equals(y.toString())) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}

/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
