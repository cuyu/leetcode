from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        rooms = []
        for i in sorted_intervals:
            for r in rooms:
                if i[0] < r[-1][1]:
                    continue
                else:
                    r.append(i)
                    break
            else:
                rooms.append([i])
        return len(rooms)


if __name__ == "__main__":
    Solution().minMeetingRooms([[0, 30], [15, 20], [5, 10]])
