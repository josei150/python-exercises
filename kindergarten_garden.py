"""

Instructions
Given a diagram, determine which plants each child in the kindergarten class is responsible for.

The kindergarten class is learning about growing plants. The teacher thought it would be a good idea to give them actual seeds, 
plant them in actual dirt, and grow actual plants.

They've chosen to grow grass, clover, radishes, and violets.

To this end, the children have put little cups along the window sills, and planted one type of plant in each cup,
choosing randomly from the available types of seeds.
"""

class Garden:
    def __init__(self, diagram, students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]) -> None:
        self.row1 = diagram[:len(diagram) // 2]
        self.row2 = diagram[len(diagram) // 2 + 1:]
        self.students = sorted(students)
        self.kindergarten = {
            "V" : "Violets",
            "G" : "Grass",
            "C" : "Clover",
            "R" : "Radishes"
        }
        

    def plants(self, name):
        index = self.students.index(name) * 2
        list_plants = []
        list_plants.append(self.kindergarten[self.row1[index]])
        list_plants.append(self.kindergarten[self.row1[index + 1]])
        list_plants.append(self.kindergarten[self.row2[index]])
        list_plants.append(self.kindergarten[self.row2[index + 1]])
        return list_plants

if __name__ == "__main__":
    #garden = Garden("RC\nGG")
    #garden = Garden("VVCCGG\nVVCCGG")
    #print(garden.row1, garden.row2)
    
    #print(garden.plants("Charlie"))

    garden2 = Garden("VCRRGVRG\nRVGCCGCV", students=["Samantha", "Patricia", "Xander", "Roger"])
    print(garden2.plants("Patricia"))