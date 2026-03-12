---
title: plane3d
sidebar_label: plane3d
---

# plane3d

Defines a plane in 3D space through three non-collinear points. Represents a flat surface for cross-sections, reflections, and spatial partitioning.

**Utility:** Create a plane through three points in 3D space

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d` | Yes | 3D graph container created with g3d() |
| `point1` | `point3d` | Yes | First point on the plane |
| `point2` | `point3d` | Yes | Second point on the plane |
| `point3` | `point3d` | Yes | Third point on the plane (must not be collinear with the first two) |

## Variants

### Through three points

```
plane(G, P1, P2, P3)
```

Plane defined by three non-collinear points

### With color and fill

```
plane(G, P1, P2, P3, c(blue), f(lightblue))
```

Plane with stroke color and fill

### Parallel through point

```
pll3d(plane, point)
```

Create a plane parallel to an existing plane, passing through a new point

### Tangent plane to surface

```
tangentplane(G, surface, x, y, size)
```

Tangent plane to a plot3d surface at the point (x, y)

### Tangent plane at point variable

```
tangentplane(G, surface, point)
```

Tangent plane to a surface at an existing point

## Examples

### Plane through three points

```
G = g3d(at(0, 0), 30, 30)
P1 = point3d(G, 1, 0, 0)
P2 = point3d(G, 0, 1, 0)
P3 = point3d(G, 0, 0, 1)
pl = plane(G, P1, P2, P3)
```

### Tangent plane on a paraboloid (tangent-plane lesson)

```
G = g3d(at(0, 0), 30, 30)
S = plot3d(G, "x^2 + y^2", range(-3, 3), range(-3, 3))
tx = 1
ty = 1
pt = point3d(G, tx, ty, tx*tx + ty*ty)
T = tangentplane(G, S, pt)
change(tx, 1, -2)
```

### Parallel plane through a point

```
G = g3d(at(0, 0), 30, 30)
pl = plane(G, point3d(G, 1, 0, 0), point3d(G, 0, 1, 0), point3d(G, 0, 0, 1))
P = point3d(G, 2, 2, 2)
pl2 = pll3d(pl, P)
```

### Tangent plane at specific coordinates (point-3d-change lesson)

```
G = g3d(at(0, 0), 30, 30)
f = def(x, y, "x^2 + y^2")
P = plot3d(G, f, range(-3, 3), range(-3, 3))
x0 = 1
y0 = 1
T = tangentplane(G, P, x0, y0)
change(x0, 1, -2)
```
