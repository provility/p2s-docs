---
title: vector3d
sidebar_label: vector3d
---

# vector3d

Creates a directed 3D vector arrow between two points in a 3D graph, defined by six coordinates or two point expressions. The vector renders as an arrow and stores start and end positions.

**Utility:** Create a directed 3D vector arrow between two points

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d` | Yes | 3D graph container created with g3d() |
| `start and end` | `x1, y1, z1, x2, y2, z2 \| point3d, point3d` | Yes | Six numeric coordinates (x1, y1, z1, x2, y2, z2) or two point3d expressions defining start and end |

## Variants

### From six coordinates

```
vector3d(G, x1, y1, z1, x2, y2, z2)
```

Vector from (x1,y1,z1) to (x2,y2,z2)

### From two point3d variables

```
vector3d(G, P1, P2)
```

Vector from point3d P1 to point3d P2

### From origin

```
vector3d(G, 0, 0, 0, 3, 4, 5)
```

Vector starting at origin pointing to (3,4,5)

### With color styling

```
vector3d(G, 0, 0, 0, 1, 0, 0, c(red))
```

Red-colored vector along x-axis

## Examples

### Create a vector from origin to point (3, 2, 1)

```
G = g3d(at(0, 0), 30, 30)
V = vector3d(G, 0, 0, 0, 3, 2, 1)
```

### Create a vector between two existing 3D points

```
G = g3d(at(0, 0), 30, 30)
P1 = point3d(G, 1, 0, 0)
P2 = point3d(G, 4, 3, 2)
V = vector3d(G, P1, P2)
```

### Create three basis vectors along x, y, z axes with colors

```
G = g3d(at(0, 0), 30, 30)
i = vector3d(G, 0, 0, 0, 1, 0, 0, c(red))
j = vector3d(G, 0, 0, 0, 0, 1, 0, c(green))
k = vector3d(G, 0, 0, 0, 0, 0, 1, c(blue))
```
