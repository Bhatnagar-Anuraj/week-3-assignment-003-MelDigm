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
import scene_functions as sf

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
trunk1 = cmds.polyCylinder(name="trunk1", radius=0.3, height=2.0)[0]
cmds.move(-4, 1.0, 0, trunk1)
canopy1 = cmds.polySphere(name="canopy1", radius=1.2)[0]
cmds.move(-4, 2.7, 0, canopy1)
def create_tree(x, z, trunk_height=2.0, canopy_radius=1.2):
    """Create a simple tree at the given X, Z position.

    Default parameter values (trunk_height=2.0) let callers omit arguments they're happy with.
    """
    trunk_radius = 0.3
    trunk = cmds.polyCylinder(radius=trunk_radius, height=trunk_height)[0]
    cmds.move(x, trunk_height / 2.0, z, trunk)

    canopy = cmds.polySphere(radius=canopy_radius)[0]
    canopy_y = trunk_height + canopy_radius * 0.6
    cmds.move(x, canopy_y, z, canopy)

    # We return the node names so the caller can modify them later if needed.
    return trunk, canopy
    
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
place_in_circle(create_tree, count=8, radius=7, center_x=0, center_z=5)
def create_building(x, z, width=2.0, height=5.0, depth=2.0):
    """Create a rectangular building at (x, z), sitting on the ground plane."""
    building = cmds.polyCube(width=width, height=height, depth=depth)[0]
    cmds.move(x, height / 2.0, z, building)
    return building

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

# ---------------------------------------------------------------------------
# Final viewport framing (do not remove).
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    cmds.viewFit(allObjects=True)
    print("Main scene built successfully!")
