class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        record = collections.defaultdict(list)
        
        for i in access_times:
            record[i[0]].append(int(i[1]))

        res = []

        for i in record.keys():
            if len(record[i]) >= 3:
                time = record[i]
                time.sort()
                for j in range(2,len(time)):
                    if (abs(time[j] - time[j-2]) < 100):
                        res.append(i)
                        break
        
        return res
