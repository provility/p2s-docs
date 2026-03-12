---
title: "Point 3D + Vector 3D"
sidebar_label: "Point 3D + Vector 3D"
---

# Point 3D + Vector 3D

Operations available when you select a **point3d** and a **vector3d** together.

## How to Use

```
  1. Click on a point3d object to select it
  2. Hold Shift and click on a vector3d object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Plane (normal)** | Handler for 3D point + 3D vector selection |
| **Line (direction)** | Create a 3D plane with vector as normal, passing through point |
| **Parallel Vector** | Create a 3D line through point in direction of vector |
| **Perpendicular Vector** | Create parallel vector through point |

## Expression Details

**Create a 3D plane with vector as normal, passing through point**

```
plane3d(G, vector, point)
```

**Create a 3D line through point in direction of vector**

```
line3d(G, point, vector)
```

**Create parallel vector through point**

```
pll3d(vector, point) or pll3d(vector, point, length)
```

**Create perpendicular vector through point**

```
perp3d(vector, point, ax, ay, az) - needs axis to determine perpendicular direction
```
