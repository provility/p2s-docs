---
title: center
sidebar_label: center
---

# center

Compute the geometric center or midpoint of a shape, or the midpoint between two specified points.

**Utility:** Get center/midpoint of a shape or midpoint between two points

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `shape` | `line \| vector \| arc \| circle \| ellipse \| hyperbola \| polygon` | Yes | Shape to find center/midpoint of (first form) |
| `graph` | `g2d` | No | Graph container (second form: center(graph, p1, p2)) |
| `p1` | `point` | No | First point (second form) |
| `p2` | `point` | No | Second point (second form) |

## Variants

### Midpoint of line

```
center(L)
```

Returns midpoint of line segment L

### Center of circle

```
center(C)
```

Returns center of circle C

### Center of ellipse

```
center(E)
```

Returns center of ellipse E

### Incenter of triangle

```
center(T)
```

Returns incenter of triangle T (3-vertex polygon)

### Centroid of polygon

```
center(P)
```

Returns centroid of polygon P (4+ vertices)

### Midpoint between two points

```
center(G, p1, p2)
```

Returns midpoint between points p1 and p2

## Examples

### Midpoint of a line segment

```
L = line(G, 0, 0, 6, 6)
M = center(L)
```

### Center of a circle

```
C = circle(G, 3, 2, 4)
cp = center(C)
```

### Midpoint between two points

```
A = point(G, 1, 1)
B = point(G, 5, 3)
M = center(G, A, B)
```

### Incenter of a triangle

```
T = polygon(G, 0, 0, 4, 0, 2, 3)
I = center(T)
```
