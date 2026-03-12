---
title: pointat
sidebar_label: pointat
---

# pointat

Returns a point on a circle or curve at a given x-coordinate. An optional index selects among multiple solutions at the same x-value.

**Utility:** Get a point on a circle or plot at a specific x-coordinate

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The 2D graph container |
| `shape` | `circle \| plot` | Yes | Shape to find the point on |
| `x` | `number` | Yes | The x-coordinate at which to find the point |
| `index` | `number (1-based)` | No | Which point to return when multiple exist (default 1) |

## Variants

### Point on circle (upper)

```
pointat(G, C, 3)
```

Upper point on circle C at x=3

### Point on circle (lower)

```
pointat(G, C, 3, 2)
```

Lower point on circle C at x=3

### Point on plot

```
pointat(G, P, 2)
```

Point on plot P at x=2

## Examples

### Set up graph and a circle

```
graph_1 = g2d(at(10, 10), 20, 20)
```

### Create a circle centered at origin with radius 5

```
C = circle(graph_1, point(graph_1, 0, 0), radius(5))
```

### Get the top point at x=3 yielding (3, 4)

```
top = pointat(graph_1, C, 3)
```

### Get the bottom point at x=3 yielding (3, -4)

```
bottom = pointat(graph_1, C, 3, 2)
```

### Draw a vertical chord connecting both points

```
chord = line(graph_1, top, bottom, type(segment))
```

### Get point on a parabola plot at x=3 yielding (3, 9)

```
P = plot(graph_1, "x^2", -5, 5)
```

### Point on the parabola at x=3

```
pt_on_plot = pointat(graph_1, P, 3)
```

### Draw a secant line between two points on the plot

```
secant = line(graph_1, pointat(graph_1, P, 2), pointat(graph_1, P, 3), type(segment))
```
