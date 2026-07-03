class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = list()
        for asteroid in asteroids:

            # Keep resolving collisions
            while stack and stack[-1] > 0 and asteroid < 0:

                # Top asteroid is smaller, so it explodes
                if stack[-1] < abs(asteroid):
                    stack.pop()

                # Both are equal, so both explode
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    break

                # Top asteroid is larger, current asteroid explodes
                else:
                    break

            else:
                # Executed only if the while loop wasn't terminated by break
                stack.append(asteroid)

        return stack