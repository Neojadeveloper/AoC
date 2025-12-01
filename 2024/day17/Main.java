
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        String[] parts = getExample().split("\n\n");
        String[] regs = parts[0].split("\n");
        String program = parts[1];
        Map<Character, Integer> map = new HashMap<>();
        for (String reg : regs) {
            map.put(reg.charAt(9), Integer.parseInt(reg.split(" ")[2]));
        }
        List<Integer> list = new ArrayList<>();
        for (String s : program.substring(9).split(",")) {
            list.add(Integer.parseInt(s));
        }

        int i = 0;
        StringBuilder sb = new StringBuilder();
        while (true) {
            if (i >= list.size())
                break;
            Integer p1 = list.get(i);
            Integer p2 = list.get(i + 1);
            if (p2 == 4)
                p2 = map.get('A');
            else if (p2 == 5)
                p2 = map.get('B');
            else if (p2 == 6)
                p2 = map.get('C');
            if (p1 == 0) {
                int a = map.get('A');
                int b = (int) Math.pow(2, p2);
                map.put('A', a / b);
            } else if (p1 == 1) {
                int a = map.get('B');
                int b = p2;
                map.put('B', a ^ b);
            } else if (p1 == 2) {
                int a = p2;
                int b = 8;
                map.put('B', a % b);
            } else if (p1 == 3) {
                if (map.get('A') != 0) {
                    i = p2;
                    continue;
                }
            } else if (p1 == 4) {
                // if (p2 == 4) p2 = map.get('A');
                // else if (p2 == 5) p2 = map.get('B');
                // else if (p2 == 6) p2 = map.get('C');
                int a = map.get('B');
                int b = map.get('C');
                map.put('B', a ^ b);
            } else if (p1 == 5) {
                int a = p2;
                int b = 8;
                System.out.print(a % b);
                System.out.print(",");
                sb.append(a % b);
            } else if (p1 == 6) {
                int a = map.get('A');
                int b = (int) Math.pow(2, p2);
                map.put('B', a / b);
            } else if (p1 == 7) {
                int a = map.get('A');
                int b = (int) Math.pow(2, p2);
                map.put('C', a / b);
            }

            i += 2;
        }

        System.out.println(map);
        System.out.println(sb);
    }

    private static String getExample2() {
        return "Register A: 2024\n" +
                "Register B: 2024\n" +
                "Register C: 43690\n" +
                "\n" +
                "Program: 4,0";
    }

    private static String getExample() {
        return "Register A: 729\n" +
                "Register B: 0\n" +
                "Register C: 0\n" +
                "\n" +
                "Program: 0,1,5,4,3,0";
    }

    private static String getInput() {
        return "Register A: 38610541\n" +
                "Register B: 0\n" +
                "Register C: 0\n" +
                "\n" +
                "Program: 2,4,1,1,7,5,1,5,4,3,5,5,0,3,3,0";
    }
}