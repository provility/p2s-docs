---
title: perp
sidebar_label: perp
---

# perp

Constructs a perpendicular line through a given point, rotated 90 degrees from a reference direction. Useful for altitudes, normals, and right-angle constructions.

**Utility:** Create a perpendicular line or vector through a point relative to a reference line/vector

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The 2D graph container |
| `line_or_vec` | `line \| vector` | Yes | Reference line or vector to be perpendicular to |
| `point` | `point` | Yes | Point through which the perpendicular passes |
| `length` | `number` | No | Custom length for the perpendicular (defaults to reference length) |

## Variants

### Perpendicular through point (default length)

```
perp(G, L, P)
```

Line through P perpendicular to L, same length as L

### Perpendicular with custom length

```
perp(G, L, P, 5)
```

Perpendicular through P with length 5

### Perpendicular to a vector

```
perp(G, V, P)
```

Vector through P perpendicular to vector V

## Examples

### Create a line and draw a perpendicular through a point

```
graph_1 = g2d(at(10, 10), 20, 20)
```

### Define two points and a line segment

```
A = point(graph_1, -3, -1)
```

### Second point for line

```
B = point(graph_1, 4, 2)
```

### Draw line through A and B

```
L = line(graph_1, A, B)
```

### Define a point off the line

```
P = point(graph_1, 1, 4)
```

### Draw perpendicular through P to line L

```
perp_1 = perp(graph_1, L, P)
```

### Draw perpendicular with custom length 3

```
perp_2 = perp(graph_1, L, P, 3)
```

### Mark the right angle at the intersection

```
rightangle_1 = rightangle(graph_1, L, perp_1, 0.4)
```
