import java.util.Scanner;

public class solve_1{
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        int n=scanner.nextInt();
        int [] numbers=new int[100];
        int result=0;
        int min=101;
        for (int i = 0; i < n; i++) {
            int num=scanner.nextInt();
            numbers[num-1]++;
        }
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i]!=0 && numbers[i]<min){
                min=numbers[i];
                result=i;
            }
        }
        System.out.println(result+1);
    }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
