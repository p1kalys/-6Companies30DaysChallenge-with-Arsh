class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        s = mass
        for i in asteroids:
            if i > s:
                return False
            s+=i
        return True
