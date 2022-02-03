import java.util.Scanner;

public class solve_1 {
    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        int n = scanner.nextInt();
        int[] arr = new int[n];
        int sum = 0, sum2 = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = scanner.nextInt();
            sum += arr[i];
        }
        sum = sum / n;
        for (int i = 0; i < n; i++) {
            int a = arr[i] - sum;
            if (a > 0) {
                sum2 += a;
            }
        }
        System.out.println(sum2);
    }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */