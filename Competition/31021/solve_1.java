import java.util.Scanner;

public class solve_1 {
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        int n = input.nextInt();
        String[] name = new String[n];
        for (int i = 0; i < n; i++) {
            name[i] = input.next();
        }
        if (n != 1) {
            for (int i = 1; i < n; i++) {
                for (int j = 1; j <= i; j++) {
                    System.out.printf("%s: salam %s!\n", name[i], name[i - j]);
                }
            }
            for (int i = 0; i < n; i++) {
                System.out.printf("%s: khodafez bacheha!\n", name[i]);
                for (int j = i + 1; j < n; j++) {
                    System.out.printf("%s: khodafez %s!\n", name[j], name[i]);
                }
            }
        } else {
            System.out.printf("%s: khodafez bacheha!\n", name[0]);
        }
    }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
