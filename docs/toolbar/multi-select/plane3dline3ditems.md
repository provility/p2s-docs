---
title: "Plane 3D + Line 3D"
sidebar_label: "Plane 3D + Line 3D"
---

# Plane 3D + Line 3D

Operations available when you select a **plane3d** and a **line3d** together.

## How to Use

```
  1. Click on a plane3d object to select it
  2. Hold Shift and click on a line3d object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Angle** | Handler for 3D plane + 3D line selection |
| **Intersect** | Create angle between plane and line |
| **Reflect** | Find intersection point of plane and line |

## Expression Details

**Create angle between plane and line**

```
angle3d(G, plane, line)
```

**Find intersection point of plane and line**

```
intersect3d(G, plane, line)
```

**Reflect line across plane**

```
reflect3d(plane, line)
```
