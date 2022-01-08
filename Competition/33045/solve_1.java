import java.util.Scanner;

public class solve_1 {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();
    int counter = 0, sum = 0;
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= i; j++) {
        if (i % j == 0) {
          counter++;
          sum += j;
        }
      }
    }
    System.out.print(counter + " " + sum);
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
