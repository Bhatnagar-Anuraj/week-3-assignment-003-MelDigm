"""
DIGM 131 - Assignment 3: Function Library (scene_functions.py)
===============================================================

OBJECTIVE:
    Create a library of reusable functions that each generate a specific
    type of scene element. This module will be imported by main_scene.py.

REQUIREMENTS:
    1. Implement at least 5 reusable functions.
    2. Every function must have a complete docstring with Args and Returns.
    3. Every function must accept parameters for position and/or size so
       they can be reused at different locations and scales.
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
center_x = 0
center_z = 0
def place_in_circle(create_func, count=8, radius=10, center=(0, 0, 0),
                     **kwargs):
    """Place objects created by 'create_func' in a circular arrangement."""
    results = []
    for i in range(count):
        angle = (2 * math.pi / count) * i
        x = center_x + math.cos(angle) * radius
        z = center_z + math.sin(angle) * radius
        result = create_func(x, z)
        results.append(result)
    return results

def create_building(width=4, height=8, depth=4, position=(0, 0, 0)):
    """Create a rectangular building at (x, z)."""
    building = cmds.polyCube(width=width, height=height, depth=depth)[0]
    cmds.move(x, height / 2.0, z, building)
    return building

def create_tree(trunk_radius=0.3, trunk_height=3, canopy_radius=2,
                position=(0, 0, 0)):
    """Create a simple tree at the given X, Z position."""
    trunk_radius = 0.3
    trunk = cmds.polyCylinder(radius=trunk_radius, height=trunk_height)[0]
    cmds.move(x, trunk_height / 2.0, z, trunk)
    canopy = cmds.polySphere(radius=canopy_radius)[0]
    canopy_y = trunk_height + canopy_radius * 0.6
    cmds.move(x, canopy_y, z, canopy)
    return trunk, canopy

def create_fence(length=10, height=1.5, post_count=6, position=(0, 0, 0)):
    """Create a simple fence made of posts and rails. """
    post = cmds.polyCylinder(radius=0.1, height=height)[0]
    cmds.move(x, height / 2.0, z, post)
    post2 = cmds.polyCylinder(radius=0.1, height=height)[0]
    rail = cmds.polyCube(width=height, height=.2, depth=.2)[0]
    cmds.move(x, height-height/2 + 0.25, z, rail)
    cmds.move(x + height, height / 2.0, z, post2)
    return post, post2, rail

def create_lamp_post(pole_height=5, light_radius=0.5, position=(0, 0, 0)):
    """Create a street lamp using a cylinder pole and a sphere light."""
    pole = cmds.polyCylinder(radius=0.1, height=height)[0]
    cmds.move(x, height / 2.0, z, pole)
    lamp = cmds.polySphere(radius=0.25)[0]
    cmds.move(x, height + 0.25, z, lamp)
    return pole, lamp

