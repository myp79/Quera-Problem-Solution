import java.util.Scanner;

public class solve_1 {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();
    int a;
    if (n % 2 == 0) {
      a = n / 2 + 1;
      System.out.println(a * a);
    } else {
      a = (n - 1) / 2;
      System.out.println((a + 1) * (a + 2));
    }
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
