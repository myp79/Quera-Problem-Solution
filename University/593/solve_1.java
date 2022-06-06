import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class solve_1 {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {

        int n = scanner.nextInt();
        int b = sumDigit(n);
        int i = n;
        List<Integer> num = new ArrayList<>();
        while (num.size() != b) {
            i++;
            if (prime(i)) {
                num.add(i);
            }
        }
        System.out.print(num.get(num.size() - 1));
    }

    public static int sumDigit(int n) {
        int sum = 0;
        while (n != 0) {
            sum += n % 10;
            n = n / 10;
        }
        return sum;
    }

    public static boolean prime(int x) {
        int counter = 0;
        for (int i = 2; i < x; i++) {
            if (x % i == 0) {
                counter++;
            }
        }
        return counter == 0;
    }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */