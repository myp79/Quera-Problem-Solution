import java.util.Scanner;

public class solve_1 {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int k = input.nextInt();
    int sum = 0;
    for (int i = 0; i < k; i++) {
      sum += i + 1;
    }
    System.out.println(sum);
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
