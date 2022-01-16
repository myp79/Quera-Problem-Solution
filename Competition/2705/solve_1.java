import java.util.Scanner;

public class solve_1 {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int p = scanner.nextInt();
    int d = scanner.nextInt();
    int halfP = p / 2;
    int i = 0;
    do {
      i++;
    } while ((d * i) % p > halfP);
    System.out.println(d * (i));
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
