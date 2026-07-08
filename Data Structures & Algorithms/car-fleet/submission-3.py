class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = []

        position, speed = zip(*sorted(zip(position, speed), reverse=True))

        for i in range(len(position)):
            time.append((target-position[i])/speed[i])
        

        fleet=[]

        for i in range(len(time)):
            if not fleet or time[i] > fleet[-1]:
                fleet.append(time[i])
        

        return len(fleet)
