import java.util.Scanner;

public class solve_1 {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int n = input.nextInt();
    int[] weight = new int[n];
    int max = 0, index = 0;
    for (int i = 0; i < n; i++) {
      weight[i] = input.nextInt();
      if (weight[i] > max) {
        max = weight[i];
        index = i;
      }
    }
    System.out.println(index + 1);
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
