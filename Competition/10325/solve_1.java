import java.util.Scanner;

public class solve_1 {
    public static void main(String [] args){
        Scanner input=new Scanner(System.in);
        int x=input.nextInt(),y=input.nextInt();
        if (y>10){
            System.out.print("Left ");
            System.out.print(10-x+1+" ");
            System.out.print(20-y+1);
        }
        else {
            System.out.print("Right ");
            System.out.print(10-x+1+" ");
            System.out.print(y);
        }

    }
}

/**
* @author Mohammad YousefiPour - Github.com/myp79
*/
