
from data_input.metadata import objects


def convert_object_into_list(objects):
    """
    Convert objects back into a list
    Args:
        objects: List of object instances
    Return:
        list: Coordinates [x1, y1, z1, x2, y2, z2, ...]
    """
    list_results = []
    for o in objects:
        list_results.append(o.x)
        list_results.append(o.y)
        list_results.append(o.z)
    return list_results

def sort_coordinate(objects):
   """
   Used for the object class to extract the coordinations (x,y,z) of the class into a list.

   Arg:
    object class

   Return: list(float)
   """
   x = []
   y = []
   z = []
   object_names = []
   volumes = []
   for o in objects:
      x.append(o.x)
      y.append(o.y)
      z.append(o.z)
      object_names.append(type(o).__name__)
      volumes.append(o.volume())
      
   return (x, y, z, object_names, volumes)