import java.util.*;

class Solution {
    public List<Integer> solveQueries(int[] nums, int[] queries) {
        int n = nums.length;
        Map<Integer, List<Integer>> valToIndices = new HashMap<>();

        for (int i = 0; i < n; i++) {
            valToIndices.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }

        List<Integer> result = new ArrayList<>();

        for (int qIdx : queries) {
            int targetVal = nums[qIdx];
            List<Integer> indices = valToIndices.get(targetVal);

            if (indices.size() <= 1) {
                result.add(-1);
                continue;
            }

            int pos = Collections.binarySearch(indices, qIdx);
            
            int leftNeighbor, rightNeighbor;
            
            if (pos == 0) {
                leftNeighbor = indices.get(indices.size() - 1);
                rightNeighbor = indices.get(1);
            } else if (pos == indices.size() - 1) {
                leftNeighbor = indices.get(pos - 1);
                rightNeighbor = indices.get(0);
            } else {
                leftNeighbor = indices.get(pos - 1);
                rightNeighbor = indices.get(pos + 1);
            }

            int dist1 = Math.abs(qIdx - leftNeighbor);
            dist1 = Math.min(dist1, n - dist1);

            int dist2 = Math.abs(qIdx - rightNeighbor);
            dist2 = Math.min(dist2, n - dist2);

            result.add(Math.min(dist1, dist2));
        }

        return result;
    }
}