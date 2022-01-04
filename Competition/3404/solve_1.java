import java.util.Scanner;

public class solve_1 {

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    int weight = input.nextInt();
    double height = input.nextFloat();
    double bmi = (double) weight / Math.pow(height, 2);
    System.out.printf("%.2f\n", bmi);
    if (bmi < 18.5) {
      System.out.println("Underweight");
    } else if (bmi >= 18.5 && bmi < 25) {
      System.out.println("Normal");
    } else if (bmi >= 25 && bmi <= 30) {
      System.out.println("Overweight");
    } else {
      System.out.println("Obese");
    }
  }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
