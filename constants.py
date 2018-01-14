WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
red = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRASS_GREEN = (76, 187, 23)
SKY_BLUE = (135, 206, 250)

"""
surf = pygame.transform.scale(surf, ((self.width*100)/(abs(self.z-player_z)+1), (self.height*100)/(abs(self.z-player_z)+1)))

"""



def list_sort(lst):
    print "run funttoin"
    ordered_lst = []

    for entity in lst:
        print entity
        counter = 0
        if len(ordered_lst) == 0:
            ordered_lst.append(entity)
        else:
            for ordered_entity in ordered_lst:
                print ordered_entity
                if entity.z > ordered_entity.z:
                    ordered_lst.insert(counter, entity)
                    break
                elif counter == len(ordered_lst) - 1:
                    ordered_lst.append(entity)
                    break
                counter += 1

    return ordered_lst