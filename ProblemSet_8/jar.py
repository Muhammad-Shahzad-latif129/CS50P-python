class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return f"🍪" * self._size

    def deposit(self, n):
        if n < 0:
            raise ValueError("Cannot deposit negative cookies")
        if self._size + n > self._capacity:
            raise ValueError("Exceeds Jar limit")
        self._size += n
        

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw negative cookies")
        if self._size - n < 0:
            raise ValueError("Not Enough cookies in the jar")
        self._size -= n
    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    cp = Jar()
    cp.deposit(4)
    print(cp)
    
# Test capacity validation
try:
    jar = Jar(-5)  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

# Test negative deposits/withdrawals
jar = Jar()
try:
    jar.deposit(-3)  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

try:
    jar.withdraw(-2)  # Should raise ValueError
except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
    main()