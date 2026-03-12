---
title: cylinder
sidebar_label: cylinder
---

# cylinder

Creates a right circular cylinder with a given radius and height, positioned at a center point and oriented along the z-axis.

**Utility:** Create a cylinder at a center point with radius and height

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d` | Yes | 3D graph container created with g3d() |
| `radius` | `number` | Yes | Radius of the cylinder base |
| `height` | `number` | Yes | Height of the cylinder |
| `center` | `point3d` | Yes | Center base point of the cylinder |

## Variants

### Cylinder at a point

```js
cylinder(G, radius, height, point)
```

Cylinder at an existing point3d with radius and height

### Cylinder with inline center

```js
cylinder(G, radius, height, point3d(G, x, y, z))
```

Cylinder with inline center point

### With color

```js
cylinder(G, radius, height, point, c(green))
```

Cylinder with a custom color

## Examples

### Cylinder at the origin

```js
G = g3d(at(0, 0), 30, 30)
P = point3d(G, 0, 0, 0)
cyl = cylinder(G, 1, 5, P)
```

### Cylinder with inline center and color

```js
G = g3d(at(0, 0), 30, 30)
cyl = cylinder(G, 2, 4, point3d(G, 1, 1, 0), c("orange"))
```

### Tall narrow cylinder

```js
G = g3d(at(0, 0), 30, 30)
cyl = cylinder(G, 0.5, 8, point3d(G, 0, 0, 0))
```
