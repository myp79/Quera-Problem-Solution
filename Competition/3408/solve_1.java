import java.util.Scanner;

public class revers {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();
    String[] string = new String[n];
    for (int i = 0; i < n; i++) {
      string[i] = input.next();
    }
    for (int i = n - 1; i >= 0; i--) {
      System.out.print(string[i] + " ");
    }
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
