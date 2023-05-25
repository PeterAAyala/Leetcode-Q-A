class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        pairSum = numbers[left] + numbers[right]
        while pairSum != target:
            if pairSum > target:
                right -= 1
                pairSum = numbers[left] + numbers[right]
            if pairSum < target:
                left += 1
                pairSum = numbers[left] + numbers[right]
        return [left+1, right+1]
        