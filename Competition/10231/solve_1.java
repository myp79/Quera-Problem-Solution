import java.util.Scanner;

public class solve_1 {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    String[] strings = new String[5];
    int counter = 0;
    for (int i = 0; i < 5; i++) {
      strings[i] = input.nextLine();
      if (strings[i].contains("MOLANA") || strings[i].contains("HAFEZ")) {
        counter++;
        System.out.print(i + 1 + " ");
      }
    }
    if (counter == 0) {
      System.out.print("NOT FOUND!");
    }
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
