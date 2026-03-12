---
title: plot3d
sidebar_label: plot3d
---

# plot3d

Plots surfaces and curves in 3D space, supporting explicit surfaces z=f(x,y), parametric curves and surfaces, and implicit surfaces f(x,y,z)=0.

**Utility:** Plot 3D surfaces (explicit, parametric, implicit) and parametric curves

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d` | Yes | 3D graph container created with g3d() |
| `equation` | `string \| definition` | Yes | Equation string in quotes, or a def() reference. For parametric types, provide three separate equation strings for x, y, z components. |
| `range` | `range(min, max)` | No | Domain range for each parameter. One range for curves (t) and explicit surfaces (x), two ranges for parametric surfaces (u, v) and explicit surfaces (x, y). |

## Variants

### Explicit surface z = f(x, y)

```js
plot3d(G, "equation", range(xMin, xMax), range(yMin, yMax))
```

Surface defined by z as a function of x and y

### Parametric curve

```js
plot3d(G, "x(t)", "y(t)", "z(t)", range(tMin, tMax))
```

Space curve defined by three parametric equations in t

### Parametric surface

```js
plot3d(G, "x(u,v)", "y(u,v)", "z(u,v)", range(uMin, uMax), range(vMin, vMax))
```

Surface defined by three parametric equations in u and v

### Implicit surface

```js
plot3d(G, "f(x,y,z)")
```

Surface defined implicitly where f(x, y, z) = 0

### Using a definition variable

```js
plot3d(G, f, range(xMin, xMax), range(yMin, yMax))
```

Surface using a def() function reference instead of a string

### With color styling

```js
plot3d(G, "x^2 + y^2", range(-3, 3), range(-3, 3), c(blue))
```

Surface with a custom color

## Examples

### Paraboloid surface (tangent-plane lesson)

```js
G = g3d(at(0, 0), 30, 30)
S = plot3d(G, "x^2 + y^2", range(-3, 3), range(-3, 3))
```

### Explicit surface using def() (point-3d-change lesson)

```js
G = g3d(at(0, 0), 30, 30)
f = def(x, y, "x^2 + y^2")
P = plot3d(G, f, range(-3, 3), range(-3, 3))
```

### Parametric curve for solid of revolution (solid-of-rev lesson)

```js
G = g3d(at(5, 5), 20, 20)
c1 = plot3d(G, "t", "0.5*t", "0", range(0, 4), c("green"))
```

### Parametric surface (sphere parameterization)

```js
G = g3d(at(0, 0), 30, 30)
sph = plot3d(G, "cos(u)*sin(v)", "sin(u)*sin(v)", "cos(v)", range(0, 2*pi), range(0, pi))
```

### Implicit surface (unit sphere)

```js
G = g3d(at(0, 0), 30, 30)
surface = plot3d(G, "x^2 + y^2 + z^2 - 1")
```
