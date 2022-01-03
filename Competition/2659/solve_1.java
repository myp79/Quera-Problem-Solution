import java.util.Scanner;

public class solve_1 {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    String n = input.nextLine();
    String one = input.nextLine();
    String two = input.nextLine();
    int counter = 0;
    for (int i = 0; i < Integer.parseInt(String.valueOf(n)); i++) {
      if (one.charAt(i) != two.charAt(i)) {
        counter++;
      }
    }
    System.out.print(counter);
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
