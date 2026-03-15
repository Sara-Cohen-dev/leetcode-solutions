class Fancy:
    MOD = 10**9 + 7

    def __init__(self):
        self.seq = []
        self.mul = 1  # global multiplier
        self.add = 0  # global adder
        self.history = []  # store (mul_at_append, add_at_append) for each element

    def append(self, val: int) -> None:
        # Store the value along with the current global transformation
        self.seq.append(val)
        self.history.append((self.mul, self.add))

    def addAll(self, inc: int) -> None:
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.seq):
            return -1
        val = self.seq[idx]
        mul_at_append, add_at_append = self.history[idx]

        # Apply the transformation difference
        # current value = val * (self.mul / mul_at_append) + (self.add - add_at_append * (self.mul / mul_at_append))
        # Since we need modulo, use modular inverse
        inv = pow(mul_at_append, self.MOD - 2, self.MOD)
        current_val = (val * self.mul * inv + (self.add - add_at_append * self.mul * inv) % self.MOD) % self.MOD
        return current_val