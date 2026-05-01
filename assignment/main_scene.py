"""
DIGM 131 - Assignment 3: Function Library (main_scene.py)
==========================================================

OBJECTIVE:
    Use the functions you wrote in scene_functions.py to build a complete
    scene. This file demonstrates how importing and reusing functions makes
    scene creation clean and readable.

REQUIREMENTS:
    1. Import scene_functions (the module you completed).
    2. Call each of your 5+ functions at least once.
    3. Use place_in_circle with at least one of your create functions.
    4. The final scene should contain at least 15 objects total.
    5. Comment your code explaining what you are building.

GRADING CRITERIA:
    - [30%] All 5+ functions from scene_functions.py are called.
    - [25%] place_in_circle is used at least once.
    - [20%] Scene contains 15+ objects and looks intentional.
    - [15%] Code is well-commented.
    - [10%] Script runs without errors from top to bottom.
"""

import maya.cmds as cmds
import math
#"import scene_functions as sf" made it not work and would make an error show up
# ---------------------------------------------------------------------------
# Scene Setup
# ---------------------------------------------------------------------------
cmds.file(new=True, force=True)

# Create a ground plane.
ground = cmds.polyPlane(name="ground", width=60, height=60,
                        subdivisionsX=1, subdivisionsY=1)[0]

# ---------------------------------------------------------------------------
# TODO: Build your scene below by calling functions from scene_functions.
#
# Example calls (uncomment and modify once your functions are implemented):
#
#   sf.create_building(width=5, height=10, depth=5, position=(-10, 0, 8))
#   sf.create_tree(position=(3, 0, -5))
#   sf.create_fence(length=12, post_count=7, position=(-6, 0, -3))
#   sf.create_lamp_post(position=(8, 0, 2))
#
#   # Place 8 trees in a circle of radius 15:
#   sf.place_in_circle(sf.create_tree, count=8, radius=15)
#
# Remember: call each function at least once, and aim for 15+ objects.
# ---------------------------------------------------------------------------
def create_tree(x, z, trunk_height=2.0, canopy_radius=1.2):
    """Create a simple tree at the given X, Z position."""
    trunk_radius = 0.3
    trunk = cmds.polyCylinder(radius=trunk_radius, height=trunk_height)[0]
    cmds.move(x, trunk_height / 2.0, z, trunk)
    canopy = cmds.polySphere(radius=canopy_radius)[0]
    canopy_y = trunk_height + canopy_radius * 0.6
    cmds.move(x, canopy_y, z, canopy)
    return trunk, canopy
create_tree(-4, 0)
create_tree(0, 0)
create_tree(4, 0)
create_tree(8, 0, trunk_height=3.5, canopy_radius=1.8) # a big tree
def place_in_circle(create_func, count, radius, center_x=0, center_z=0):
    results = []
    for i in range(count):
        angle = (2 * math.pi / count) * i
        x = center_x + math.cos(angle) * radius
        z = center_z + math.sin(angle) * radius
        result = create_func(x, z)
        results.append(result)
    return results
place_in_circle(create_tree, count=8, radius=7)

    
# Now we can build a street in just a few lines
create_building(-6, -6, height=8)
create_building(-2, -6, width=3, height=4, depth=3)
create_building(3, -6, height=10)

# =============================================================================
# SECTION 4: Return values — using what a function gives back
# =============================================================================

def create_lamppost(x, z, height=3.0):
    """Create a lamppost and return the pole and lamp node names."""
    pole = cmds.polyCylinder(radius=0.1, height=height)[0]
    cmds.move(x, height / 2.0, z, pole)

    lamp = cmds.polySphere(radius=0.25)[0]
    cmds.move(x, height + 0.25, z, lamp)
    return pole, lamp

# Capture the return values in variables
pole_node, lamp_node = create_lamppost(0, 5)
print("Created lamppost: pole={}, lamp={}".format(pole_node, lamp_node))

# Now we can do something with the returned names — like make the lamp glow
lamp_shader = cmds.shadingNode("lambert", asShader=True, name="lampGlow")
cmds.setAttr(lamp_shader + ".color", 1.0, 0.95, 0.6, type="double3")
cmds.select(lamp_node)
cmds.hyperShade(assign=lamp_shader)
# =============================================================================
# SECTION 5: Outline
# =============================================================================
import maya.cmds as cmds


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
    # TODO: Implement this function.
    #   1. Create a polyCube with the given width, height, and depth.
    #   2. Move it so its base sits on the ground at 'position'.
    #      Hint: offset Y by height / 2.0.
    #   3. Return the object name.
    pass


def create_tree(trunk_radius=0.3, trunk_height=3, canopy_radius=2,
                position=(0, 0, 0)):
    """Create a simple tree using a cylinder trunk and a sphere canopy.

    Args:
        trunk_radius (float): Radius of the cylindrical trunk.
        trunk_height (float): Height of the trunk cylinder.
        canopy_radius (float): Radius of the sphere used for the canopy.
        position (tuple): (x, y, z) ground-level position for the tree base.

    Returns:
        str: The name of a group node containing the trunk and canopy.
    """
    # TODO: Implement this function.
    #   1. Create a polyCylinder for the trunk and position it.
    #   2. Create a polySphere for the canopy, positioned on top of the trunk.
    #   3. Group trunk and canopy together using cmds.group().
    #   4. Move the group to 'position'.
    #   5. Return the group name.
    pass


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
    # TODO: Implement this function.
    #   1. Calculate spacing between posts: length / (post_count - 1).
    #   2. Loop to create 'post_count' thin, tall cubes as posts.
    #   3. Create a long, thin cube as a horizontal rail connecting them.
    #   4. Group everything and move to 'position'.
    #   5. Return the group name.
    pass


def create_lamp_post(pole_height=5, light_radius=0.5, position=(0, 0, 0)):
    """Create a street lamp using a cylinder pole and a sphere light.

    Args:
        pole_height (float): Height of the lamp pole.
        light_radius (float): Radius of the sphere representing the light.
        position (tuple): (x, y, z) ground-level position.

    Returns:
        str: The name of a group node containing the pole and light.
    """
    # TODO: Implement this function.
    #   1. Create a thin polyCylinder for the pole.
    #   2. Create a polySphere for the light, placed at the top of the pole.
    #   3. Group them, move to 'position', and return the group name.
    pass


def place_in_circle(create_func, count=8, radius=10, center=(0, 0, 0),
                     **kwargs):
    """Place objects created by 'create_func' in a circular arrangement.

    This is a higher-order function: it takes another function as an
    argument and calls it repeatedly to place objects around a circle.

    Args:
        create_func (callable): A function from this module (e.g.,
            create_tree) that accepts a 'position' keyword argument
            and returns an object name.
        count (int): Number of objects to place around the circle.
        radius (float): Radius of the circle.
        center (tuple): (x, y, z) center of the circle.
        **kwargs: Additional keyword arguments passed to create_func
            (e.g., trunk_height=4).

    Returns:
        list: A list of object/group names created by create_func.
    """
    # TODO: Implement this function.
    #   1. Import the math module (at the top of the file or here).
    #   2. Loop 'count' times. For each iteration:
    #       a. Calculate the angle: angle = 2 * math.pi * i / count
    #       b. Calculate x = center[0] + radius * math.cos(angle)
    #       c. Calculate z = center[2] + radius * math.sin(angle)
    #       d. Call create_func(position=(x, center[1], z), **kwargs)
    #       e. Append the returned name to a results list.
    #   3. Return the results list.
    pass
# ---------------------------------------------------------------------------
# Final viewport framing (do not remove).
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    cmds.viewFit(allObjects=True)
    print("Main scene built successfully!")
