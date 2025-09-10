# Parent class
class Craft:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def craft_info(self):
        return f"{self.name} made with {self.material}"


# Child class
class Crochet(Craft):
    def __init__(self, name, material, yarn_color, hours_spent):
        super().__init__(name, material)  # call parent constructor
        self.yarn_color = yarn_color
        self.hours_spent = hours_spent

    def start_project(self):
        return f"Started crocheting a {self.name} with {self.yarn_color} yarn"

    def finish_project(self):
        return f"Finished {self.name}! Took {self.hours_spent} hours."

    def __str__(self):
        return f"{self.craft_info()} | Yarn Color: {self.yarn_color} | Hours Spent: {self.hours_spent}"

