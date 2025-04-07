class TreeNode:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def __str__(self):
        return f"{self.name} ({self.designation})"

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        # print(level)
        return level

    def print_tree(self, property_name):
        if property_name == 'both':
            value = self.name + " (" + self.designation + ")"
        elif property_name == 'name':
            value = self.name
        else:
            value = self.designation

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)



def build_management_tree():
    ceo = TreeNode('Nilupul', 'CEO')
    cto = TreeNode('Chinmay', 'CTO')
    hr_head = TreeNode('Gels', 'HR Head')

    ceo.add_child(cto)
    ceo.add_child(hr_head)

    infra_head = TreeNode('Vishwa', 'Infrastructure Head')
    application_head = TreeNode('Aamir', 'Application Head')
    cto.add_child(infra_head)
    cto.add_child(application_head)

    cloud_manager = TreeNode('Dhaval', 'Cloud Manager')
    app_manager = TreeNode('Abhijit', 'App Manager')
    infra_head.add_child(cloud_manager)
    infra_head.add_child(app_manager)


    recruitment_manager = TreeNode('Peter', 'Recruitment Manager')
    policy_manager = TreeNode('Waqas', 'Policy Manager')
    hr_head.add_child(recruitment_manager)
    hr_head.add_child(policy_manager)


    return ceo


root = build_management_tree()
root.print_tree('name')
root.print_tree('designation')
root.print_tree('both')
