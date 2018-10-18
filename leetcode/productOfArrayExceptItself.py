class Sol():
    """docstring for ClassName"""

    def findOtherProducts(self, nums):
        p = 1
        output = []
        for i in range(0, len(nums)):
            output.append(p)
            p = p * nums[i]
        p = 1
        print(output)
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output


prod = Sol()
print(prod.findOtherProducts([1, 2, 0, 4]))
