package day20;

import java.util.*;

public class Solution {
    private static Map<String, Object[]> memo = new HashMap<>();

    public static List<List<int[]>> bfsSearch(char[][] matrix, int[] start, int[] goal, boolean onePath) {
        String memoKey = Arrays.toString(start) + Arrays.toString(goal) + onePath;
        if (memo.containsKey(memoKey)) {
            return (List<List<int[]>>) memo.get(memoKey)[0];
        }

        int row = matrix.length;
        int col = matrix[0].length;
        int[][] directions = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
        Queue<Object[]> queue = new LinkedList<>();
        queue.add(new Object[] { start, new ArrayList<int[]>(List.of(start)) });
        List<List<int[]>> allPaths = new ArrayList<>();
        Map<int[], List<int[]>> cheats = new HashMap<>();

        while (!queue.isEmpty()) {
            Object[] current = queue.poll();
            int[] position = (int[]) current[0];
            List<int[]> path = (List<int[]>) current[1];

            if (Arrays.equals(position, goal)) {
                if (onePath) {
                    memo.put(memoKey, new Object[] { path, null });
                    return List.of(path);
                }
                allPaths.add(path);
                continue;
            }

            for (int[] direction : directions) {
                int newI = position[0] + direction[0];
                int newJ = position[1] + direction[1];
                if (newI >= 0 && newI < row && newJ >= 0 && newJ < col && matrix[newI][newJ] != '#') {
                    int[] newPos = { newI, newJ };
                    if (!pathContains(path, newPos)) {
                        List<int[]> newPath = new ArrayList<>(path);
                        newPath.add(newPos);
                        queue.add(new Object[] { newPos, newPath });
                    }
                } else if (matrix[newI][newJ] == '#' && !onePath) {
                    int di = newI + direction[0];
                    int dj = newJ + direction[1];
                    if (di >= 0 && di < row && dj >= 0 && dj < col && matrix[di][dj] != '#') {
                        int[] newPos = { newI, newJ };
                        if (!cheats.containsKey(newPos)) {
                            cheats.put(newPos, new ArrayList<>());
                        }
                        List<int[]> l = bfsSearch(matrix, new int[] { di, dj }, position, true).get(0);
                        cheats.put(newPos, l);
                    }
                }
            }
        }

        memo.put(memoKey, new Object[] { allPaths, cheats });
        return allPaths;
    }

    private static boolean pathContains(List<int[]> path, int[] pos) {
        for (int[] p : path) {
            if (Arrays.equals(p, pos)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        char[][] matrix = readInputData();
        int row = matrix.length;
        int col = matrix[0].length;
        int[] start = null;
        int[] goal = null;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 'S') {
                    start = new int[] { i, j };
                } else if (matrix[i][j] == 'E') {
                    goal = new int[] { i, j };
                }
            }
        }

        List<List<int[]>> paths = bfsSearch(matrix, start, goal, false);
        for (List<int[]> path : paths) {
            System.out.println(Arrays.deepToString(path.toArray()));
        }
    }

    private static char[][] readInputData() {
        // Implement this method to read input data and return the matrix
        return new char[][] {
                { 'S', '.', '.', '#', '.', '.', '.' },
                { '.', '#', '.', '#', '.', '#', '.' },
                { '.', '#', '.', '.', '.', '#', '.' },
                { '.', '.', '#', '#', '.', '.', '.' },
                { '#', '.', '#', 'E', '.', '#', '.' }
        };
    }
}