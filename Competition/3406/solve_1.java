import java.util.Scanner;

public class solve_1 {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    String a = input.nextLine();
    String b = input.nextLine();
    StringBuilder aRev = new StringBuilder();
    StringBuilder bRev = new StringBuilder();
    aRev = aRev.append(a).reverse();
    bRev = bRev.append(b).reverse();
    String aRev2 = aRev.toString();
    String bRev2 = bRev.toString();
    if (Integer.parseInt(aRev2) > Integer.parseInt(bRev2)) {
      System.out.println(b + " < " + a);
    } else if (Integer.parseInt(aRev2) < Integer.parseInt(bRev2)) {
      System.out.println(a + " < " + b);
    } else {
      System.out.println(b + " = " + a);
    }
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
