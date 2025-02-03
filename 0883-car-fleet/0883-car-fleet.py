class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        counter, prev = 0, 0

        for p, s in cars:
            time = (target - p) / s
            if prev < time:
                counter += 1
                prev = time
        
        return counter
