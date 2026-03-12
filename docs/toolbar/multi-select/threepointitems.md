---
title: "Point + Point + Point"
sidebar_label: "Point + Point + Point"
---

# Point + Point + Point

Operations available when you select a **point** and a **point** together.

## How to Use

```
  1. Click on a point object to select it
  2. Hold Shift and click on a point object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Angle** | Handler for exactly 3 points selection |
| **Polygon** | Create an angle from three points (middle point is vertex) |
| **Polyline** | Create a polygon (triangle) from three points |

## Expression Details

**Create an angle from three points (middle point is vertex)**

```
angle(G, P1, P2, P3, type(interior), radius(0.2))
```

**Create a polygon (triangle) from three points**

```
polygon(G, P1, P2, P3)
```

**Create a polyline from three points**

```
polyline(G, P1, P2, P3)
```
