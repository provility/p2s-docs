---
title: "Point 3D + Point 3D"
sidebar_label: "Point 3D + Point 3D"
---

# Point 3D + Point 3D

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
| **Line** | Handler for two 3D point selection |
| **Vector** | Create a 3D line between two points |
| **Distance** | Create a 3D vector from first point to second point |
| **Distance Trace** | Distance trace between two 3D points |
| **Midpoint** | Show distance between two 3D points |
| **Measure** | Create midpoint between two 3D points |
| **Cone** | Create a measurement indicator between two 3D points |
| **Frustum** | Create a cone between two points (base center + apex) |

## Expression Details

**Create a 3D line between two points**

```
line3d(G, P1, P2, type(segment|line|ray))
```

**Create a 3D vector from first point to second point**

```
vector3d(G, P1, P2)
```

**Distance trace between two 3D points**

```
trace3d(G, P1, type(distance), P2)
```

**Show distance between two 3D points**

```
distance3d(G, P1, P2)
```

**Create midpoint between two 3D points**

```
midpoint3d(G, P1, P2)
```

**Create a measurement indicator between two 3D points**

```
measure3d(G, P1, P2, "label", buff(value))
```

**Create a cone between two points (base center + apex)**

```
cone(G, radius, P1, P2)
```

**Create a frustum between two points**

```
frustum(G, baseRadius, topRadius, P1, P2)
```
