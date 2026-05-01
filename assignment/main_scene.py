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
def place_in_circle(create_func, count, radius, center_x=0, center_z=0):
    results = []
    for i in range(count):
        angle = (2 * math.pi / count) * i
        x = center_x + math.cos(angle) * radius
        z = center_z + math.sin(angle) * radius
        result = create_func(x, z)
        results.append(result)
    return results

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

place_in_circle(create_tree, count=8, radius=7)

# ---------------------------------------------------------------------------
# Final viewport framing (do not remove).
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    cmds.viewFit(allObjects=True)
    print("Main scene built successfully!")
