class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = " "*self.get_level() * 3
        prefix = spaces + "|--" if self.parent else ""
        print(prefix+self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


def build_product_tree():
    root = TreeNode("Electronics")
    

    # create children as Laptop
    laptop = TreeNode("Laptop")
    # add laptop as children to root
    root.add_child(laptop)

    # add childrens to laptop
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("HP"))
    laptop.add_child(TreeNode("ASUS"))
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("Lenovo"))

    # create children as Mobile
    mobile = TreeNode("Mobile")

    # Add Mobile as children to root
    root.add_child(mobile)

    # Add childrens to Mobile
    mobile.add_child(TreeNode("iPhone"))
    mobile.add_child(TreeNode("Google"))
    mobile.add_child(TreeNode("Samsung"))
    mobile.add_child(TreeNode("Vivo"))
    mobile.add_child(TreeNode("Redmi"))

    # Add Tv as children to root
    tv = TreeNode("TV")
    root.add_child(tv)

    # Add childrens to TV
    tv.add_child(TreeNode("SamSung"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("TLC"))
    tv.add_child(TreeNode("OnePlus"))

    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
    # print(root.get_level())
