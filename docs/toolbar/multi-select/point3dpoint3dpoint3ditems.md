---
title: "Point 3D + Point 3D + Point 3D"
sidebar_label: "Point 3D + Point 3D + Point 3D"
---

# Point 3D + Point 3D + Point 3D

Operations available when you select a **point3d** and a **point3d** together.

## How to Use

```
  1. Click on a point3d object to select it
  2. Hold Shift and click on a point3d object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Plane** | Handler for three 3D point selection |
| **Angle** | Create a 3D plane through three non-collinear points |

## Expression Details

**Create a 3D plane through three non-collinear points**

```
plane3d(G, P1, P2, P3)
```

**Create a 3D angle with first point as vertex**

```
angle3d(G, vertex, P2, P3)
```
