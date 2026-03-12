---
title: "Plane 3D + Point 3D"
sidebar_label: "Plane 3D + Point 3D"
---

# Plane 3D + Point 3D

Operations available when you select a **plane3d** and a **point3d** together.

## How to Use

```
  1. Click on a plane3d object to select it
  2. Hold Shift and click on a point3d object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Project** | Handler for 3D plane + 3D point selection |
| **Reflect** | Project point onto plane (foot of perpendicular) |
| **Distance** | Reflect point across plane |
| **Distance** | Distance from point to plane |

## Expression Details

**Project point onto plane (foot of perpendicular)**

```
project3d(plane, point)
```

**Reflect point across plane**

```
reflect3d(plane, point)
```

**Distance from point to plane**

```
distance3d(plane, point)
```
