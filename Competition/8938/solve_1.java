import java.util.Scanner;

public class solve_1 {
  static Scanner scanner = new Scanner(System.in);

  public static void main(String[] args) {
    int m = scanner.nextInt();
    int n = scanner.nextInt();
    int sum = 0;
    int[][] matrix = new int[m][m];
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < m; j++) {
        matrix[i][j] = scanner.nextInt();
      }
    }
    for (int i = 0; i < n; i++) {
      int x = scanner.nextInt();
      int y = scanner.nextInt();
      sum += matrix[x - 1][y - 1];
    }
    System.out.print(sum);
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
