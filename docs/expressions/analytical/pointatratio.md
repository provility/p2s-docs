---
title: pointatratio
sidebar_label: pointatratio
---

# pointatratio

Returns a point at a specified proportional position along a line, circle circumference, or between two points. A ratio of 0.5 gives the midpoint; values outside [0,1] extrapolate on lines.

**Utility:** Get a point at a ratio along a line/circle or between two points

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The 2D graph container |
| `shape_or_p1` | `line \| circle \| point` | Yes | Shape to find point along (mode 1) or first point (mode 2) |
| `ratio_or_p2` | `number \| point` | Yes | Ratio 0-1 (mode 1) or second point (mode 2) |
| `ratio` | `number` | No | Ratio 0-1 when using two-point mode (mode 2) |

## Variants

### Midpoint of a line

```
pointatratio(G, L, 0.5)
```

Point at the midpoint of line L

### Quarter point on circle

```
pointatratio(G, C, 0.25)
```

Point at 90 degrees (top) of circle C

### Between two points

```
pointatratio(G, A, B, 0.5)
```

Midpoint between points A and B

### One-third point

```
pointatratio(G, A, B, 0.333)
```

Point one-third of the way from A to B

## Examples

### Set up graph for ratio demonstrations

```
graph_1 = g2d(at(10, 10), 20, 20)
```

### Create a line segment

```
L = line(graph_1, point(graph_1, -4, 0), point(graph_1, 4, 0), type(segment))
```

### Get the midpoint of the line

```
mid = pointatratio(graph_1, L, 0.5)
```

### Get the quarter point

```
quarter = pointatratio(graph_1, L, 0.25)
```

### Find midpoint between two arbitrary points

```
A = point(graph_1, -3, 2)
```

### Second point

```
B = point(graph_1, 5, -2)
```

### Midpoint between A and B

```
M = pointatratio(graph_1, A, B, 0.5)
```

### Point on a circle at ratio 0.25 (top)

```
C = circle(graph_1, point(graph_1, 0, 0), radius(3))
```

### Top of circle via ratio

```
top = pointatratio(graph_1, C, 0.25)
```
