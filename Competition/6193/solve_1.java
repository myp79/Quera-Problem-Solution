import java.util.Scanner;

public class solve_1 {
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        String string = input.nextLine();
        StringBuilder password = new StringBuilder();
        int[] repeat = new int[26];
        for (int i = 0; i < string.length(); i++) {
            int characterNum = string.charAt(i);
            if (characterNum >= 65 && characterNum <= 90) {
                repeat[characterNum - 65]++;
            } else if (characterNum >= 97 && characterNum <= 122) {
                repeat[characterNum - 97]++;
            }
        }
        for (int i = 0; i < string.length(); i++) {
            int characterNum = string.charAt(i);
            int y = 0;
            if (characterNum >= 65 && characterNum <= 90) {
                y = (repeat[characterNum - 65] * (characterNum - 65) + 1) % 26;
                password.append((char) (y + 65));
            } else if (characterNum >= 97 && characterNum <= 122) {
                y = (repeat[characterNum - 97] * (characterNum - 97) + 1) % 26;
                password.append((char) (y + 97));
            }
        }
        System.out.println(password);
    }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
