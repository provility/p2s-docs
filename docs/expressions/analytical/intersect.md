---
title: intersect
sidebar_label: intersect
---

# intersect

Finds the intersection point of two geometric objects such as lines, circles, or curves. An optional index selects among multiple intersection points.

**Utility:** Find intersection point between two geometric objects (lines, circles, plots)

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The 2D graph container |
| `obj1` | `line \| circle \| plot` | Yes | First geometric object |
| `obj2` | `line \| circle \| plot \| vline` | Yes | Second geometric object |
| `index` | `number (1-based)` | No | Which intersection point to return (default 1). Useful when two objects intersect at multiple points. |

## Variants

### Line-line intersection

```
intersect(G, L1, L2)
```

Single intersection point of two lines

### Line-circle first intersection

```
intersect(G, L, C)
```

First intersection of line and circle

### Line-circle second intersection

```
intersect(G, L, C, 2)
```

Second intersection of line and circle

### Circle-circle intersection

```
intersect(G, C1, C2)
```

First intersection of two circles

### Plot-vline intersection

```
intersect(G, P, vline(G, x))
```

Point where a plot crosses a vertical line at x

## Examples

### Find intersection of two lines (linear programming vertex)

```
G = g2d(at(2, 2), 20, 30, range(-1, 10))
```

### Define constraint lines

```
L1 = line(G, point(G, 0, 0), point(G, 5, 0))
```

### Second constraint line

```
L3 = line(G, point(G, 0, 3), point(G, 4, 0))
```

### Find the corner point where constraints meet

```
A = intersect(G, L1, L3)
```

### Intersect two circles

```
circle_1 = circle(graph_1, point(graph_1, 1.4, 1.6), radius(2))
```

### Second circle partially overlapping

```
circle_2 = circle(graph_1, point(graph_1, 3.1, 2.8), radius(2))
```

### Get first intersection of the two circles

```
point_1 = intersect(graph_1, circle_1, circle_2)
```

### Find where a parabola crosses a vertical line

```
P = plot(G, "x^2/6 - 0.5", -7, 7)
```

### Intersect plot with vertical line at x = 2

```
H5 = intersect(G, P, vline(G, 2))
```
