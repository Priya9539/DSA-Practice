class Solution:
    def pascalstriangle(self, numRows):
        # Initialize the main list to store the triangle
        triangle = []

        # Loop through each row
        for i in range(numRows):
            row = []

            # Each row has i + 1 elements
            for j in range(i + 1):
                # First and last elements of every row are always 1
                if j == 0 or j == i:
                    row.append(1)
                else:
                    # Middle elements are sum of two elements above
                    row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

            # Add the completed row to triangle
            triangle.append(row)

        # Return the final triangle
        return triangle


if __name__ == "__main__":
    n = 5
    sol = Solution()
    result = sol.pascalstriangle(n)
    print(result)

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)