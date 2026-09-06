class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        a = [intervals[0]]
        start1 = a[0][0]
        end1 = a[0][1]
        for i in range(1, len(intervals)):
            start2 = intervals[i][0]
            end2 = intervals[i][1]
            if (end1>=start2):
                end1 = max(end1,end2)
                a[-1] = [start1,end1]

            else:
                start1 = start2
                end1 = end2
                a.append([start1,end1])
        return a