# The script of the game goes in this file.

init python:
    from abc import ABC, abstractmethod
    class world_data:
        def __init__(self, name, image):
            self.name = name
            self.image = image
            self.contents = []
        
        def add_content(self, new):
            self.contents.append(new)
        
        def remove_content(self, target):
            self.contents.remove(target)

    class world_content(ABC):
        @abstractmethod
        def on_interact():
            pass
        
    class door(world_content):
        def __init__(self, image, pos, nextLocation):
            self.image = image
            self.pos = pos
            self.nextLocation = nextLocation

        def on_interact():
            renpy.show_screen(nextLocation)
    
    class interactable(world_content):
        def __init__(self, image, pos, label):
            self.image = image
            self.pos = pos
            self.label = label

        def on_interact():
            renpy.call(label)

define e = Character("Eileen")


# The game starts here.

label start:
    
    default testWorld = world_data("test world", "bg.png")
    default testObject = interactable("test/%s.png", (20, 20), "test_label")
    $ testWorld.add_content(testObject)

    "AJSKLJSDFJLDS"
    show screen expression "world" pass(testWorld)


label test_label:
    "HI"