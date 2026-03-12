---
title: "Line 3D + Point 3D"
sidebar_label: "Line 3D + Point 3D"
---

# Line 3D + Point 3D

Operations available when you select a **line3d** and a **point3d** together.

## How to Use

```
  1. Click on a line3d object to select it
  2. Hold Shift and click on a point3d object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Parallel** | Handler for 3D line + 3D point selection |
| **Perpendicular** | Create parallel line through point |
| **Distance** | Create perpendicular line through point |

## Expression Details

**Create parallel line through point**

```
pll3d(line, point) or pll3d(line, point, length)
```

**Create perpendicular line through point**

```
perp3d(line, point, ax, ay, az) - needs axis to determine perpendicular direction
```

**Distance from point to line**

```
distance3d(line, point)
```
