class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildBinaryTree(nums, index):
    if index >= len(nums) or nums[index] is None:
        return None

    root = TreeNode(nums[index])
    root.left = buildBinaryTree(nums, 2 * index + 1)  # Recursive call for left child
    root.right = buildBinaryTree(nums, 2 * index + 2)  # Recursive call for right child
    return root


def generateMarkdown(root, level=0):
    if root is None:
        return ""

    markdown = ""
    markdown += "  " * level  # Indentation based on the level
    markdown += "- " + str(root.val) + "\n"  # Add current node value

    markdown += generateMarkdown(root.left, level + 1)  # Recursive call for left subtree
    markdown += generateMarkdown(root.right, level + 1)  # Recursive call for right subtree

    return markdown


def main():
    # Test case: nums = [2,None,3,None,4,None,5,None,6]
    nums = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    root = buildBinaryTree(nums, 0)

    print(generateMarkdown(root))


if __name__ == "__main__":
    main()