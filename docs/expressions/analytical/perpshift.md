---
title: perpshift
sidebar_label: perpshift
---

# perpshift

Offsets a line or vector laterally by a specified perpendicular distance, preserving its orientation and length.

**Utility:** Shift a vector or line perpendicular to its direction by a specified distance

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | The 2D graph container |
| `vec_or_line` | `vector \| line` | Yes | Vector or line to shift perpendicularly |
| `distance` | `number` | Yes | Distance to shift (positive=left/CCW, negative=right/CW) |

## Variants

### Shift vector left

```js
perpshift(G, V, 2)
```

Shift vector V perpendicular by 2 units to the left

### Shift vector right

```js
perpshift(G, V, -2)
```

Shift vector V perpendicular by 2 units to the right

### Shift line

```js
perpshift(G, L, 1.5)
```

Shift line L perpendicular by 1.5 units

## Examples

### Set up graph and a horizontal vector

```js
graph_1 = g2d(at(10, 10), 20, 20)
```

### Create a horizontal vector

```js
V = vector(graph_1, 0, 0, 5, 0)
```

### Shift vector 2 units upward (left of direction)

```js
V_up = perpshift(graph_1, V, 2)
```

### Shift vector 2 units downward (right of direction)

```js
V_down = perpshift(graph_1, V, -2)
```

### Shift a line segment perpendicular

```js
L = line(graph_1, point(graph_1, -3, 0), point(graph_1, 3, 0), type(segment))
```

### Create parallel offset of the line

```js
L_shifted = perpshift(graph_1, L, 1.5)
```
