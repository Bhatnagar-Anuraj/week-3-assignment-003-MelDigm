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
# Comment example
import maya.cmds as cmds
import scene_functions as sf
# ---------------------------------------------------------------------------
# Scene Setup
# ---------------------------------------------------------------------------

cmds.file(new=True, force=True)


def create_scene():
    ground = cmds.polyPlane(name="ground", width=60, height=60,
                        subdivisionsX=1, subdivisionsY=1)[0]
    building = sf.create_building(position=(0,0,4))
    tree = sf.create_tree(3, -5)
    fence = sf.create_fence(-6, -3)
    lamp = sf.create_lamppost(0, 7)
    circle= sf.place_in_circle(sf.create_lamppost, count=6, radius=5, center_x=0, center_z=5) # ring of lampposts
    return ground, building, tree, fence, lamp, circle
create_scene()

# ---------------------------------------------------------------------------
# Final viewport framing (do not remove).
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    cmds.viewFit(allObjects=True)
    print("Main scene built successfully!")
