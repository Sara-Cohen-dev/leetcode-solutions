class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        parts = []
        balance = 0
        start = 0

        for i, char in enumerate(s):
            if char == '1':
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                inner = s[start + 1:i]
                special = '1' + self.makeLargestSpecial(inner) + '0'
                parts.append(special)
                start = i + 1

        parts.sort(reverse=True)
        return ''.join(parts)    