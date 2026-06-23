class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = sorted(list(zip(position, speed)), reverse=True)
        for p, s in cars:
            if not stack:
                t = (target - p)/s
                stack.append((p,t))
            else:
                last_car_p, last_car_t = stack[-1]
                current_t = (target - p)/s
                if current_t > last_car_t:
                    stack.append((p, current_t))
        return len(stack)
        