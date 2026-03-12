---
title: line3d
sidebar_label: line3d
---

# line3d

Creates a line segment in 3D space between two endpoints defined by their spatial coordinates.

**Utility:** Create a line segment between two 3D points

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d` | Yes | 3D graph container created with g3d() |
| `point1` | `point3d` | Yes | Start point of the line segment |
| `point2` | `point3d` | Yes | End point of the line segment |

## Variants

### From two point variables

```js
line3d(G, P1, P2)
```

Line segment from point P1 to point P2

### From inline points

```js
line3d(G, point3d(G, x1, y1, z1), point3d(G, x2, y2, z2))
```

Line with inline point definitions

### With color

```js
line3d(G, P1, P2, c(blue))
```

Line with a custom color

### Forward movement

```js
forward3d(line, distance)
```

Shift line along its direction by distance

### Backward movement

```js
backward3d(line, distance)
```

Shift line opposite to its direction by distance

### Perpendicular shift

```js
perpshift3d(line, distance, ax, ay, az)
```

Shift line sideways perpendicular to its direction and an axis vector (ax, ay, az)

### Reverse direction

```js
reverse3d(line)
```

Flip the direction of the line (swap start and end)

### Place at point

```js
placeat3d(line, point)
```

Copy line to a new starting location

### Parallel through point

```js
pll3d(line, point)
```

Create a parallel line passing through a point

## Examples

### Line between two 3D points

```js
G = g3d(at(0, 0), 30, 30)
P1 = point3d(G, 0, 0, 0)
P2 = point3d(G, 3, 4, 5)
L = line3d(G, P1, P2)
```

### Line with forward extension

```js
G = g3d(at(0, 0), 30, 30)
L = line3d(G, point3d(G, 0, 0, 0), point3d(G, 1, 0, 0))
fwd = forward3d(L, 2)
```

### Parallel line through a point

```js
G = g3d(at(0, 0), 30, 30)
L = line3d(G, point3d(G, 0, 0, 0), point3d(G, 3, 0, 0))
P = point3d(G, 0, 2, 0)
L2 = pll3d(L, P)
```

### Point on a line at the midpoint

```js
G = g3d(at(0, 0), 30, 30)
L = line3d(G, point3d(G, 0, 0, 0), point3d(G, 4, 4, 4))
mid = point3d(G, L, 0.5)
```
