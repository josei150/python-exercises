class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity: int) -> None:
        self.capacity: int = capacity
        self.buffer: list = []
        self.current_position: int = 0

    def read(self) -> str:
        if self.current_position + 1 > self.capacity or self.current_position > len(self.buffer) - 1:
            raise BufferEmptyException("Circular buffer is empty")

        value_in_position = self.buffer[self.current_position]
        del self.buffer[self.current_position]
        return value_in_position

    def write(self, data: str):
        if len(self.buffer) + 1 > self.capacity:
            raise BufferFullException("Circular buffer is full")

        self.buffer.append(data)

    def overwrite(self, data):
        if len(self.buffer) == self.capacity:
            del self.buffer[self.current_position]
            self.write(data)
        else:
            self.write(data)

    def clear(self):
        self.buffer = []
        self.current_position = 0


if __name__ == "__main__":
    buffer = CircularBuffer(2)
    buffer.write("52")
    buffer.write("51")
    print(buffer.read())
    print(len(buffer.buffer))
    print(buffer.read())
    print(len(buffer.buffer))
    buffer.write("53")
    print(len(buffer.buffer))

    #print(buffer.read())
    #buffer.clear()
    #print(buffer.read())
    #print(buffer.read())
