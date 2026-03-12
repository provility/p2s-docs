---
title: rightangle
sidebar_label: rightangle
---

# rightangle

Draws a right-angle square indicator at a 90-degree vertex or at the intersection of two perpendicular lines. This is a visual annotation with an optional size parameter.

**Utility:** Draw the right angle square marker at 90-degree intersections

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The 2D graph container |
| `vertex_or_line1` | `point \| line` | Yes | Vertex point (mode 1) or first line (mode 2) |
| `point1_or_line2` | `point \| line` | Yes | First arm point (mode 1) or second line (mode 2) |
| `point2` | `point` | No | Second arm point (mode 1 only) |
| `size` | `number` | No | Size of the right angle indicator square (default 0.5) |

## Variants

### Three points (vertex + two arms)

```js
rightangle(G, vertex, P1, P2)
```

Right angle at vertex between arms to P1 and P2

### Three points with custom size

```js
rightangle(G, vertex, P1, P2, 0.4)
```

Right angle indicator with size 0.4

### Two lines

```js
rightangle(G, L1, L2)
```

Right angle at the intersection of L1 and L2

### Two lines with custom size

```js
rightangle(G, L1, L2, 0.3)
```

Right angle at intersection with size 0.3

## Examples

### Set up graph for right angle demonstration

```js
graph_1 = g2d(at(10, 10), 20, 20)
```

### Create a horizontal line and a perpendicular

```js
L = line(graph_1, point(graph_1, -3, 0), point(graph_1, 4, 0))
```

### Create perpendicular through a point

```js
P = point(graph_1, 1, 3)
```

### Perpendicular line through P

```js
perp_1 = perp(graph_1, L, P)
```

### Mark right angle between the two lines

```js
rightangle_1 = rightangle(graph_1, L, perp_1, 0.4)
```

### Mark right angle using three points (vertex at origin)

```js
rightangle_2 = rightangle(graph_1, point(graph_1, 1, 0), point(graph_1, 4, 0), point(graph_1, 1, 3), 0.5)
```
