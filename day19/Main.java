import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        // Faylni o'qish
        File inputFile = new File("input.txt");

        try {
            List<String> towels = new ArrayList<>();
            List<String> towelSets = new ArrayList<>();

            BufferedReader br = new BufferedReader(new FileReader(inputFile));
            String line;

            // 1-qator: Qoidalar ro'yxatini o'qish
            if ((line = br.readLine()) != null) {
                // "r, wr, b, g, bwu, rb, gb, br" formatida bo'lgan qatorni bo'lish
                String[] towelArray = line.split(",\\s*");
                towels.addAll(Arrays.asList(towelArray));
            }

            // 2-qator: Qoidalardan keyin qatorlarni o'qish
            while ((line = br.readLine()) != null) {
                if (!line.trim().isEmpty()) { // bo'sh qatorlarni o'tkazib yuborish
                    towelSets.add(line.trim()); // .trim() metodini qo'llash
                }
            }

            br.close();

            // natijani konsolga chiqarish
            System.out.println("Towels: " + towels);
            System.out.println("Towel Sets: " + towelSets);

            // Keyin partTwo funksiyasini chaqirib, hisoblashni amalga oshirish mumkin
            partTwo(towels, towelSets);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void partTwo(List<String> towels, List<String> towelSets) {
        Long cnt = 0L;
        Map<String, Long> memo = new HashMap<>();

        for (String towelSet : towelSets) {
            Long l = cntMakeLine(towelSet, towels, memo);
            if (l > 0) {
                cnt += l;
            }
        }
        System.out.println("Total possible lines: " + cnt);
    }

    public static Long cntMakeLine(String line, List<String> rules, Map<String, Long> memo) {
        // Agar memo'da mavjud bo'lsa, saqlangan natijani qaytarish
        if (memo.containsKey(line)) {
            return memo.get(line);
        }

        // Bo'sh qator bo'lsa, 1 qaytariladi
        if (line.isEmpty()) {
            return 1L;
        }

        long cnt = 0;
        for (String rule : rules) {
            if (line.startsWith(rule)) {
                cnt += cntMakeLine(line.substring(rule.length()), rules, memo);
            }
        }

        // Natijani memo'ga saqlash
        memo.put(line, cnt);
        return cnt;
    }
}
