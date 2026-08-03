class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        cars = sorted(list(zip(position, speed)), reverse=True)

        for p, s in cars:
            if not fleet:
                t = (target - p)/s
                fleet.append((p, t))
            else:
                t = (target - p)/s
                last_p, last_t = fleet[-1]
                if t > last_t:
                    fleet.append((p, t))
        return len(fleet)