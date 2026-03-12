---
title: "Plane 3D + Plane 3D"
sidebar_label: "Plane 3D + Plane 3D"
---

# Plane 3D + Plane 3D

Operations available when you select a **plane3d** and a **plane3d** together.

## How to Use

```
  1. Click on a plane3d object to select it
  2. Hold Shift and click on a plane3d object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Dihedral Angle** | Handler for two 3D plane selection |
| **Intersect** | Create dihedral angle between two planes |

## Expression Details

**Create dihedral angle between two planes**

```
angle3d(G, plane1, plane2)
```

**Find intersection line of two planes**

```
intersect3d(G, plane1, plane2)
```
