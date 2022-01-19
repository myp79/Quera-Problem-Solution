import java.util.Scanner;

public class solve_1 {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int n = scanner.nextInt();
    int[] forms = new int[n];
    int counter = 0;
    for (int i = 0; i < n; i++) {
      forms[i] = scanner.nextInt();
    }
    for (int i = 0; i < n - 1; i++) {
      if (forms[i] != forms[i + 1]) {
        counter++;
      }
    }
    System.out.println(counter);
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
