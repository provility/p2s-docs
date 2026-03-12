---
title: sphere
sidebar_label: sphere
---

# sphere

Creates a sphere in 3D space centered at a given point with a specified radius.

**Utility:** Create a sphere at a center point with a given radius

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d` | Yes | 3D graph container created with g3d() |
| `radius` | `number` | Yes | Radius of the sphere |
| `center` | `point3d` | Yes | Center point of the sphere |

## Variants

### Sphere at a point variable

```
sphere(G, radius, point)
```

Sphere centered at an existing point3d with given radius

### Sphere with inline center

```
sphere(G, radius, point3d(G, x, y, z))
```

Sphere with inline center point definition

### Sphere from click (center + radius prompt)

```
sphere(G, center, radius)
```

Sphere created from a clicked point with a prompted radius

### With color

```
sphere(G, radius, point, c(blue))
```

Sphere with a custom color

## Examples

### Sphere at a point with radius 2

```
G = g3d(at(0, 0), 30, 30)
P = point3d(G, 0, 0, 0)
sph = sphere(G, 2, P)
```

### Sphere with inline center

```
G = g3d(at(0, 0), 30, 30)
sph = sphere(G, 3, point3d(G, 1, 2, 0))
```

### Two concentric spheres with different colors

```
G = g3d(at(0, 0), 30, 30)
P = point3d(G, 0, 0, 0)
s1 = sphere(G, 2, P, c("blue"))
s2 = sphere(G, 4, P, c("red"))
```
