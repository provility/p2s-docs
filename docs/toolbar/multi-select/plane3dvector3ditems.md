---
title: "Plane 3D + Vector 3D"
sidebar_label: "Plane 3D + Vector 3D"
---

# Plane 3D + Vector 3D

Operations available when you select a **plane3d** and a **vector3d** together.

## How to Use

```
  1. Click on a plane3d object to select it
  2. Hold Shift and click on a vector3d object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Angle** | Handler for 3D plane + 3D vector selection |
| **Reflect** | Create angle between plane and vector |

## Expression Details

**Create angle between plane and vector**

```
angle3d(G, plane, vector)
```

**Reflect vector across plane**

```
reflect3d(plane, vector)
```
