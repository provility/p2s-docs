---
title: curve3d
sidebar_label: curve3d
---

# curve3d

Creates a parametric space curve in 3D from three component equations x(t), y(t), z(t) over a parameter interval. Suitable for helices, trajectories, and arbitrary space curves.

**Utility:** Create a parametric space curve x(t), y(t), z(t) in 3D

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d` | Yes | 3D graph container created with g3d() |
| `x(t)` | `string` | Yes | X component as a function of t |
| `y(t)` | `string` | Yes | Y component as a function of t |
| `z(t)` | `string` | Yes | Z component as a function of t |
| `tRange` | `range(tMin, tMax)` | Yes | Parameter domain for t |

## Variants

### Basic parametric curve

```js
plot3d(G, "x(t)", "y(t)", "z(t)", range(tMin, tMax))
```

Space curve with three component functions of t

### With color

```js
plot3d(G, "x(t)", "y(t)", "z(t)", range(tMin, tMax), c(green))
```

Parametric curve with color styling

### Tangent vector on curve

```js
tangentvec(G, curve, t)
```

Tangent vector to the curve at parameter value t

### Point on curve

```js
point3d(G, curve, t, type(ratio))
```

Point on the curve at parametric ratio t

## Examples

### Straight-line curve for solid of revolution boundary (solid-of-rev lesson)

```js
G = g3d(at(5, 5), 20, 20)
c1 = plot3d(G, "t", "0.5*t", "0", range(0, 4), c("green"))
c2 = plot3d(G, "4", "t", "0", range(0, 2), c("green"))
```

### Parabolic curve for washer method (solid-of-rev lesson)

```js
G = g3d(at(5, 5), 20, 20)
c1 = plot3d(G, "t", "sqrt(t)", "0", range(0, 1), c("magenta"))
c2 = plot3d(G, "t", "t^2", "0", range(0, 1), c("green"))
```

### Helix curve

```js
G = g3d(at(0, 0), 30, 30)
helix = plot3d(G, "cos(t)", "sin(t)", "0.2*t", range(0, 4*pi))
```

### Curve with tangent vector

```js
G = g3d(at(0, 0), 30, 30)
curve = plot3d(G, "cos(t)", "sin(t)", "t", range(0, 2*pi))
tangent = tangentvec(G, curve, 1)
```
