import java.util.Scanner;

public class solve_1 {

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int sum = 0;
    int x = scanner.nextInt();
    String key = scanner.next();
    String[] words = new String[x];
    for (int i = 0; i < x; i++) {
      words[i] = scanner.next();
    }
    for (int i = 0; i < x; i++) {
      StringBuilder rev = new StringBuilder();
      rev.append(words[i]);
      rev = rev.reverse();
      int first = words[i].indexOf(key.charAt(i)) - 1;
      int second = rev.toString().indexOf(key.charAt(i));
      sum += Math.min(first, second);
    }
    System.out.println(sum + x);
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
