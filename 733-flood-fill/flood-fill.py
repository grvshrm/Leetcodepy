class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        m, n = len(image), len(image[0])
        
        def dfs(image, sr, sc, color, parent_color):
            nonlocal m, n
            if image[sr][sc] == parent_color:
                image[sr][sc] = color
                for del_row, del_col in zip([0, 0, -1, 1], [-1, 1, 0, 0]):
                    row = sr + del_row
                    col = sc + del_col
                    if row >= 0 and row <m and col >= 0 and col < n:
                        dfs(image, row, col, color, parent_color)
        dfs(image, sr, sc, color, image[sr][sc])
        return image