---
title: point3d
sidebar_label: point3d
---

# point3d

Places a point in 3D space at explicit (x, y, z) coordinates, or at a parametric position on a line, vector, surface, or curve.

**Utility:** Create a point at (x, y, z) in 3D space

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d` | Yes | 3D graph container created with g3d() |
| `x` | `number` | Yes | X coordinate of the point |
| `y` | `number` | Yes | Y coordinate of the point |
| `z` | `number` | Yes | Z coordinate of the point |

## Variants

### Explicit coordinates

```
point3d(G, x, y, z)
```

Point at explicit (x, y, z) coordinates

### Point on line at ratio

```
point3d(G, line, t)
```

Point on a line3d at parametric ratio t (0 = start, 1 = end)

### Point on vector at ratio

```
point3d(G, vector, t)
```

Point on a vector3d at parametric ratio t (0 = start, 1 = end)

### Point on explicit surface

```
point3d(G, surface, x, y)
```

Point on a plot3d surface at (x, y) with z computed from the surface equation

### Point on parametric curve

```
point3d(G, curve, t, type(ratio))
```

Point on a parametric curve at parameter t as a ratio of the range

### Point on parametric surface

```
point3d(G, surface, u, v)
```

Point on a parametric surface at parameter values (u, v)

### With color

```
point3d(G, x, y, z, c(red))
```

Point with a custom color

## Examples

### Point at coordinates on a 3D graph

```
G = g3d(at(0, 0), 30, 30)
pt = point3d(G, 1, 2, 3)
```

### Point on a surface with computed z

```
G = g3d(at(0, 0), 30, 30)
S = plot3d(G, "x^2 + y^2", range(-3, 3), range(-3, 3))
pt = point3d(G, S, 1, 1)
```

### Point on a surface using variable coordinates (from tangent-plane lesson)

```
G = g3d(at(0, 0), 30, 30)
f = def(x, y, "x^2 + y^2")
P = plot3d(G, f, range(-3, 3), range(-3, 3))
x0 = 1
y0 = 1
pt = point3d(G, x0, y0, fun(f, x0, y0))
```

### Point on a line at the midpoint

```
G = g3d(at(0, 0), 30, 30)
L = line3d(G, point3d(G, 0, 0, 0), point3d(G, 4, 4, 4))
mid = point3d(G, L, 0.5)
```
