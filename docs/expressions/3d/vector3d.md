---
title: vector3d
sidebar_label: vector3d
---

# vector3d

Creates a directed vector in 3D space from a tail point to a head point, representing displacement, velocity, force, or other directed quantities.

**Utility:** Create a directed vector (arrow) from one 3D point to another

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d` | Yes | 3D graph container created with g3d() |
| `start` | `point3d` | Yes | Tail (start) point of the vector |
| `end` | `point3d` | Yes | Head (end) point of the vector |

## Variants

### Between two points

```
vector3d(G, P1, P2)
```

Vector from P1 to P2

### Position vector from origin

```
vector3d(G, point3d(G, 0, 0, 0), P1)
```

Position vector from origin to point P1

### With inline points

```
vector3d(G, point3d(G, x1, y1, z1), point3d(G, x2, y2, z2))
```

Vector with inline point definitions

### With color

```
vector3d(G, P1, P2, c(red))
```

Vector with a custom color

### Forward movement

```
forward3d(vector, distance)
```

Shift vector along its direction by distance

### Reverse direction

```
reverse3d(vector)
```

Flip vector direction (swap start and end)

### Place at point

```
placeat3d(vector, point)
```

Copy vector to a new starting location

## Examples

### Vector between two points

```
G = g3d(at(0, 0), 30, 30)
P1 = point3d(G, 1, 0, 0)
P2 = point3d(G, 3, 2, 1)
v = vector3d(G, P1, P2)
```

### Position vector from origin

```
G = g3d(at(0, 0), 30, 30)
P = point3d(G, 3, 4, 5)
v = vector3d(G, point3d(G, 0, 0, 0), P)
```

### Vector placed at a new point

```
G = g3d(at(0, 0), 30, 30)
v = vector3d(G, point3d(G, 0, 0, 0), point3d(G, 1, 1, 0))
P = point3d(G, 2, 0, 0)
v2 = placeat3d(v, P)
```

### Reversed vector

```
G = g3d(at(0, 0), 30, 30)
v = vector3d(G, point3d(G, 0, 0, 0), point3d(G, 3, 2, 1))
v_rev = reverse3d(v)
```
