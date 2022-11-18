class TreeNode:
    def __init__(self,location):
        self.location = location
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,level):
        if self.get_level() > level:
            return

        space = ' '*self.get_level()*3
        prefix = space + '|__' if self.parent else ''
        print(prefix + self.location)
        if self.children :
            for child in self.children:
                child.print_tree(level)

    

def build_tree():
    earth = TreeNode('Global')

    indstate1 = TreeNode('gujarat')
    indstate1.add_child(TreeNode('ahamadabad'))
    indstate1.add_child(TreeNode('baroda'))

    indstate2 = TreeNode('karnataka')
    indstate2.add_child(TreeNode('bengalore'))
    indstate2.add_child(TreeNode('Mysore'))

    country1 = TreeNode('India')
    country1.add_child(indstate1)
    country1.add_child(indstate2)

    usstate1 = TreeNode('New Jersey')
    usstate1.add_child(TreeNode('Princeton'))
    usstate1.add_child(TreeNode('Trenton'))

    usstate2 = TreeNode('California')
    usstate2.add_child(TreeNode('San Fransico'))
    usstate2.add_child(TreeNode('palo Alto'))
    usstate2.add_child(TreeNode('MOuntain View'))
    
    country2 = TreeNode('US')
    country2.add_child(usstate1)
    country2.add_child(usstate2)

    earth.add_child(country1)
    earth.add_child(country2)

    return earth

if __name__ == "__main__":
    earth = build_tree()
    earth.print_tree(1)





