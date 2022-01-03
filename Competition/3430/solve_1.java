import java.util.Scanner;

public class solve_1 {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    String voice = input.nextLine();
    for (int i = 0; i < voice.length(); i++) {
      char alpha = voice.charAt(i);
      String result = "";
      for (int j = 0; j <= i; j++) {
        result = result.concat(String.valueOf(alpha));
      }
      result = result.concat(voice.substring(i + 1));
      System.out.println(result);
    }
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
