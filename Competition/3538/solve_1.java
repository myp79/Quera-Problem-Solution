import java.util.Scanner;

public class solve_1 {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int[] days = new int[7];
    for (int i = 0; i < 3; i++) {
      int n = input.nextInt();
      input.nextLine();
      for (int j = 0; j < n; j++) {
        String day = input.next();
        switch (day) {
          case "shanbe":
            days[0]++;
            break;
          case "1shanbe":
            days[1]++;
            break;
          case "2shanbe":
            days[2]++;
            break;
          case "3shanbe":
            days[3]++;
            break;
          case "4shanbe":
            days[4]++;
            break;
          case "5shanbe":
            days[5]++;
            break;
          case "jome":
            days[6]++;
            break;
        }
      }
    }
    int counter = 0;
    for (int i = 0; i < days.length; i++) {
      if (days[i] == 0) {
        counter++;
      }
    }
    System.out.println(counter);
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
