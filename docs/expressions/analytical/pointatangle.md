---
title: pointatangle
sidebar_label: pointatangle
---

# pointatangle

Returns a point on a circle at a specified angle in degrees measured counterclockwise from the positive x-axis. Useful for placing cardinal points, constructing inscribed polygon vertices, and angle demonstrations.

**Utility:** Get a point on a circle at a specific angle in degrees from center

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The 2D graph container |
| `shape` | `circle` | Yes | Circle to find the point on |
| `angle` | `number (degrees)` | Yes | Angle in degrees from center (0=right, 90=top, 180=left, 270=bottom) |

## Variants

### Point at right (0 degrees)

```
pointatangle(G, C, 0)
```

Rightmost point on the circle

### Point at top (90 degrees)

```
pointatangle(G, C, 90)
```

Top point on the circle

### Point at custom angle

```
pointatangle(G, C, 45)
```

Point at 45 degrees on the circle

### Point on ellipse at angle

```
pointatangle(G, ellipse(G, 0, 0, 4, 2), 45)
```

Point at 45 degrees on an ellipse

## Examples

### Set up graph and circle for angle points

```
graph_1 = g2d(at(10, 10), 20, 20)
```

### Create a circle centered at origin with radius 3

```
C = circle(graph_1, point(graph_1, 0, 0), radius(3))
```

### Point at the right (3, 0)

```
right = pointatangle(graph_1, C, 0)
```

### Point at the top (0, 3)

```
top = pointatangle(graph_1, C, 90)
```

### Point at 45 degrees

```
diag = pointatangle(graph_1, C, 45)
```

### Draw a radius line from center to the 45-degree point

```
radius_line = line(graph_1, point(graph_1, 0, 0), diag, type(segment))
```

### Place four cardinal points for an inscribed square

```
P0 = pointatangle(graph_1, C, 0)
```

### Top point of inscribed square

```
P90 = pointatangle(graph_1, C, 90)
```

### Left point of inscribed square

```
P180 = pointatangle(graph_1, C, 180)
```

### Bottom point of inscribed square

```
P270 = pointatangle(graph_1, C, 270)
```

### Draw the inscribed square from the four points

```
square_1 = polygon(graph_1, P0, P90, P180, P270)
```
