---
title: project
sidebar_label: project
---

# project

Computes the orthogonal projection of a point onto a line or vector, returning the foot of the perpendicular. The result is the closest point on the target to the given point.

**Utility:** Project a point onto a line returning the foot of the perpendicular

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The 2D graph container |
| `line_or_vec` | `line \| vector` | Yes | Line or vector to project onto |
| `point` | `point` | Yes | Point to project |

## Variants

### Project point onto line

```
project(G, L, P)
```

Foot of perpendicular from P to line L

### Project point onto vector

```
project(G, V, P)
```

Foot of perpendicular from P onto vector V

### Project with styling

```
project(G, L, P, c(red))
```

Projected point colored red

## Examples

### Set up graph for projection demonstration

```
graph_1 = g2d(at(10, 10), 20, 20)
```

### Create a line to project onto

```
L = line(graph_1, point(graph_1, -4, -1), point(graph_1, 4, 1))
```

### Create a point above the line

```
P = point(graph_1, 1, 4)
```

### Project P onto L (foot of perpendicular)

```
D = project(graph_1, L, P)
```

### Draw the perpendicular segment from P to D

```
perp_seg = line(graph_1, P, D, type(segment), pd(4, 4))
```

### Mark the right angle at D

```
rightangle_1 = rightangle(graph_1, D, P, point(graph_1, 4, 1), 0.4)
```

### Project a triangle vertex onto opposite edge (altitude foot)

```
triangle_1 = sas(graph_1, 5, 60, 4, point(graph_1, -2, -2))
```

### Extract the edge and project vertex onto it

```
foot = project(graph_1, line(graph_1, item(triangle_1, type(edge), 1)), item(triangle_1, type(vertex), 3))
```
