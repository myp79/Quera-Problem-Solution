import java.util.Scanner;

public class solve_1 {
    static Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) {
        int n = scanner.nextInt();
        String choose = scanner.next();
        boolean[] arr = new boolean[3];
        int first = side(choose);
        arr[first] = true;
        for (int i = 0; i < n; i++) {
            String x=scanner.next();
            String y=scanner.next();
            int side1=side(x);
            int side2=side(y);
            if (arr[side1] ^ arr[side2]){
                arr[side1]=!arr[side1];
                arr[side2]=!arr[side2];
            }
        }
        int result=0;
        for (int i = 0; i < 3; i++) {
            if (arr[i]){
                result=i;
            }
        }
        System.out.println(beside(result));
    }

    public static int side(String c) {
        switch (c) {
            case "L":
                return 0;
            case "M":
                return 1;
            default:
                return 2;
        }
    }
    public static String beside(int x) {
        switch (x) {
            case 0:
                return "L";
            case 1:
                return "M";
            default:
                return "R";
        }
    }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
