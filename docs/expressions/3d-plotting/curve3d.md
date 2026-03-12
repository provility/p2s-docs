---
title: plot3d (parametric curve)
sidebar_label: plot3d (parametric curve)
---

# plot3d (parametric curve)

Draws a 3D parametric curve from component functions x(t), y(t), z(t) over a parameter range, or a parametric surface when given two parameter ranges (u, v).

**Utility:** Plot a 3D parametric curve (x(t), y(t), z(t)) over a parameter range

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d reference` | Yes | The 3D graph or space container |
| `xExpr` | `string` | Yes | x-component as function of t, e.g., "cos(t)" |
| `yExpr` | `string` | Yes | y-component as function of t, e.g., "sin(t)" |
| `zExpr` | `string` | Yes | z-component as function of t, e.g., "t" |
| `tRange` | `range(min, max)` | Yes | Parameter domain for t |
| `color` | `c(colorName)` | No | Curve color - e.g., c("green"), c("magenta") |

## Variants

### Parametric curve with one range (curve3d)

```
plot3d(G, "cos(t)", "sin(t)", "t", range(0, 2*pi))
```

3D helix curve parameterized by t

### Straight-line curve for revolution boundary

```
plot3d(G, "t", "0.5*t", "0", range(0, 4), c("green"))
```

2D line in 3D space used as boundary for region3d

### Parametric surface with two ranges (para3d)

```
plot3d(G, "cos(u)*sin(v)", "sin(u)*sin(v)", "cos(v)", range(0, 2*pi), range(0, pi))
```

Parametric surface using u and v parameters with two range() args

### Vertical line curve for closing a region

```
plot3d(G, "4", "t", "0", range(0, 2), c("green"))
```

Vertical line at x=4 used to close a region boundary

## Examples

### Boundary curves for solid of revolution around x-axis

```
G = g3d(at(5, 5), 20, 20)
c1 = plot3d(G, "t", "0.5*t", "0", range(0, 4), c("green"))
c2 = plot3d(G, "4", "t", "0", range(0, 2), c("green"))
```

### Parabolic curve for revolution around y-axis

```
G = g3d(at(5, 5), 20, 20)
c1 = plot3d(G, "t^2+1", "t", "0", range(-1, 1), c("magenta"))
c2 = plot3d(G, "0", "t", "0", range(-1, 1), c("green"))
```

### Curves for washer method between sqrt(x) and x^2

```
S = g3d(at(5, 5), 20, 20)
c1 = plot3d(S, "t", "sqrt(t)", "0", range(0, 1), c("magenta"))
c2 = plot3d(S, "t", "t^2", "0", range(0, 1), c("green"))
```

### Parametric sphere surface with two parameter ranges

```
G = g3d(at(0, 0), 30, 30)
S = plot3d(G, "cos(u)*sin(v)", "sin(u)*sin(v)", "cos(v)", range(0, 2*pi), range(0, pi))
```
