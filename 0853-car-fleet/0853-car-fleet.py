class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []
        for i in range(len(position)):
            arr = (target-position[i])/speed[i]
            car.append((position[i],arr))
        car.sort(reverse=True)
        f = 0
        maxTime = 0
        for position,time in car:
            if time>maxTime:
                f += 1
                maxTime = time
        return f