import java.util.Scanner;

public class solve_1 {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    String x = input.nextLine();
    int green = 0, red = 0, yellow = 0;
    for (int i = 0; i < x.length(); i++) {
      switch (x.charAt(i)) {
        case 'G':
          green++;
          break;
        case 'R':
          red++;
          break;
        case 'Y':
          yellow++;
          break;
      }
    }
    if (red >= 3 || (red >= 2 && yellow >= 2) || green == 0) {
      System.out.println("nakhor lite");
    } else {
      System.out.println("rahat baash");
    }
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
