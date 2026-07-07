"""
DIGM 131 - Assignment 3: Function Library (scene_functions.py)
===============================================================

OBJECTIVE:
    Create a library of reusable functions that each generate a specific
    type of scene element. This module will be imported by main_scene.py.

REQUIREMENTS:
    1. Implement at least 5 reusable functions.
    2. Every function must have a complete docstring with Args and Returns.
    3. Every function must accept parameters for position and/or size so they can be reused at different locations and scales.
    4. Every function must return the name(s) of the Maya object(s) it creates.
    5. Follow PEP 8 naming conventions (snake_case for functions/variables).

GRADING CRITERIA:
    - [30%] At least 5 functions, each creating a distinct scene element.
    - [25%] Functions accept parameters and use them (not hard-coded values).
    - [20%] Every function has a complete docstring (summary, Args, Returns).
    - [15%] Functions return the created object name(s).
    - [10%] Clean, readable code following PEP 8.
"""

import maya.cmds as cmds
import math



def create_building(width=4, height=8, depth=4, position=(0, 0, 0)):
    """Create a simple building from a cube, placed on the ground plane.

    The building is a single scaled cube whose base sits at ground level
    (y = 0) at the given position.

    Args:
        width (float): Width of the building along the X axis.
        height (float): Height of the building along the Y axis.
        depth (float): Depth of the building along the Z axis.
        position (tuple): (x, y, z) ground-level position. The building
            base will rest at this point; y is typically 0.

    Returns:
        str: The name of the created building transform node.
    """
    building = cmds.polyCube(name="building",width=width, height=height, depth=depth)[0]
    cmds.move(position[0], height / 2.0, position[2], building)
    return building

def create_tree(trunk_height=2.0,trunk_radius=.5,canopy_radius=1.2,position=(0, 0, 0)):
    """Create a simple tree using a cylinder trunk and a sphere canopy.

    Args:
        trunk_radius (float): Radius of the cylindrical trunk.
        trunk_height (float): Height of the trunk cylinder.
        canopy_radius (float): Radius of the sphere used for the canopy.
        position (tuple): (x, y, z) ground-level position for the tree base.

    Returns:
        str: The name of a group node containing the trunk and canopy.
    """
    trunk = cmds.polyCylinder(name="trunk",radius=trunk_radius, height=trunk_height)[0]
    cmds.move(position[0], trunk_height / 2.0, position[2], trunk)
    canopy = cmds.polySphere(name="canopy",radius=canopy_radius)[0]
    canopy_y = trunk_height + canopy_radius * 0.6
    cmds.move(position[0], canopy_y, position[2], canopy)
    return trunk, canopy

def create_fence(length=10, height=1.5, post_count=6, position=(0, 0, 0)):
    """Create a simple fence made of posts and rails.

    The fence runs along the X axis starting at the given position.

    Args:
        length (float): Total length of the fence along the X axis.
        height (float): Height of the fence posts.
        post_count (int): Number of vertical posts (must be >= 2).
        position (tuple): (x, y, z) starting position of the fence.

    Returns:
        str: The name of a group node containing all fence parts.
    """
    post = cmds.polyCylinder(name="post",radius=0.1, height=height)[0]
    cmds.move(position[0], height / 2.0, position[2], post)
    post2 = cmds.polyCylinder(name="post2",radius=0.1, height=height)[0]
    rail = cmds.polyCube(name="rail",width=height, height=.2, depth=.2)[0]
    cmds.move(position[0]+height/2, height-height/2 + 0.25, position[2], rail)
    cmds.move(position[0] + height, height / 2.0, position[2], post2)
    return post, post2, rail

def create_lamppost(x, z, height=3.0):
    """Create a lamppost and return the pole and lamp node names."""
    pole = cmds.polyCylinder(name="pole",radius=0.1, height=height)[0]
    cmds.move(x, height / 2.0, z, pole)

    lamp = cmds.polySphere(name="lamp",radius=0.25)[0]
    cmds.move(x, height + 0.25, z, lamp)
    return pole, lamp
    """Create a street lamp using a cylinder pole and a sphere light.

      Args:
        pole_height (float): Height of the lamp pole.
       light_radius (float): Radius of the sphere representing the light.
        position (tuple): (x, y, z) ground-level position.

    Returns:
          str: The name of a group node containing the pole and light.'''
    """
    pole = cmds.polyCylinder(radius=0.1, height=pole_height)[0]
    cmds.move(position[0], position[1]+ pole_height / 2.0, position[2], pole)
    lamp = cmds.polySphere(radius=light_radius)[0]
    cmds.move(position[0], position[1]+ pole_height + 0.25, position[2], lamp)
    return pole, lamp
     
    
        
def place_in_circle(create_func, count, radius, center_x=0, center_z=0):
    """Call create_func repeatedly, placing results in a circle.

    create_func must accept (x, z) as its first two arguments.
    Returns a list of whatever create_func returns.
    """
    results = []
    for i in range(count):
        angle = (2 * math.pi / count) * i
        x = center_x + math.cos(angle) * radius
        z = center_z + math.sin(angle) * radius
        result = create_func(x, z)
        results.append(result)
    return results