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
        def __init__(self, image, nextLocation):
            self.image = image
            self.nextLocation = nextLocation

        def on_interact(self):
            renpy.show_screen(self.nextLocation)
    
    class interactable(world_content):
        def __init__(self, image, label):
            self.image = image
            self.label = label

        def on_interact(self):
            renpy.jump(self.label)

define e = Character("Eileen")


# The game starts here.

label start:
    
    default testWorld = world_data("test world", "bg.png")
    default testObject = interactable("test/%s.png", "test_label")
    $ testWorld.add_content(testObject)

    show screen expression "world" pass(testWorld)
    pause
    

label test_label:
    "HI"
    "THIS IS A TEST LABEL"
    menu test_menu:
        "oh okay":
            "YAY"
        "what i hate you":
            "oh :("
    "END"