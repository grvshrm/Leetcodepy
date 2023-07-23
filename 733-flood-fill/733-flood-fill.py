class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if(image[sr][sc] != color):
            self.fill(image, sr, sc, image[sr][sc], color)
        return image
    
    def fill(self, image, sr, sc, prevColor, newColor):
        if(sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]) or image[sr][sc] != prevColor):
            return
        image[sr][sc] = newColor
        self.fill(image, sr - 1, sc, prevColor, newColor)
        self.fill(image, sr + 1, sc, prevColor, newColor)
        self.fill(image, sr, sc - 1, prevColor, newColor)
        self.fill(image, sr, sc + 1, prevColor, newColor)