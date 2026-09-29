class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n=len(gas)
        arr=[1]*n
        for i in range(n):
            arr[i]=gas[i]-cost[i]
                
        total=0
        tank=0
        start=0

        for i in range(n):
            total+=arr[i]
            tank+=arr[i]

            if tank<0:
                start=i+1
                tank=0
        if total<0:
            return -1
        return start