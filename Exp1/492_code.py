class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        # Start width from the square root of area and count downwards
        w = int(area**0.5)
        while area % w != 0:
            w -= 1
        # Return [Length, Width] where Length >= Width and difference is minimized
        return [area // w, w]
