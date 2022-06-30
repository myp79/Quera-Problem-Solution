import java.util.Scanner;

public class solve_1 {
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        String n = input.nextLine();
        int x = Integer.parseInt(String.valueOf(n));
        String[] string = new String[x];
        for (int i = 0; i < string.length; i++) {
            string[i] = input.nextLine();
            if (!string[i].equals("")) {
                string[i] = string[i].toLowerCase();
                String[] split = string[i].split("[ ]");
                for (int j = 0; j < split.length; j++) {
                    if (!split[j].equals("")) {
                        int first = split[j].charAt(0);
                        if (first >= 97 && first <= 122) {
                            first -= 32;
                            String replace = "";
                            replace = replace.concat(String.valueOf((char) first));
                            split[j] = split[j].replaceFirst("^[a-zA-Z]", replace);
                        }
                    }
                }
                string[i] = "";
                for (String s : split) {
                    string[i] = string[i] + s + " ";
                }
            }
        }
        for (String s : string) {
            System.out.println(s);
        }
    }
}
/**
 * @author Mohammad YousefiPour - Github.com/myp79
 */
