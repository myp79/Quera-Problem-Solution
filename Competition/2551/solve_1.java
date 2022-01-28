import java.math.BigInteger;
import java.util.Scanner;

public class solve_1 {
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        BigInteger a = input.nextBigInteger();
        input.nextLine();
        String operator = input.nextLine();
        BigInteger b = input.nextBigInteger();
        if (operator.equals("+")) {
            System.out.println(a.add(b));
        } else {
            System.out.println(a.multiply(b));
        }
    }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
