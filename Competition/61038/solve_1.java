import java.util.Scanner;

public class solve_1 {
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {

        int n = input.nextInt();
        int[] teacher = new int[n];
        for (int i = 0; i < n; i++) {
            teacher[i] = input.nextInt();
        }
        long freq = lcm(teacher);
        System.out.println(freq % 30 + 1);
    }

    public static long lcm(int[] numbers) {
        long firstLcm = 1;
        int divisor = 2;
        while (true) {
            int counter = 0;
            boolean divisible = false;

            for (int i = 0; i < numbers.length; i++) {
                if (numbers[i] == 0) {
                    return 0;
                } else if (numbers[i] < 0) {
                    numbers[i] = numbers[i] * (-1);
                }
                if (numbers[i] == 1) {
                    counter++;
                }
                if (numbers[i] % divisor == 0) {
                    divisible = true;
                    numbers[i] = numbers[i] / divisor;
                }
            }
            if (divisible) {
                firstLcm = firstLcm * divisor;
            } else {
                divisor++;
            }
            if (counter == numbers.length) {
                return firstLcm;
            }
        }
    }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
