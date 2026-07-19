class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        return ''.join(c for c in s if c not in(x,y)) + y *s.count(y) + x * s.count(x)