---
title: plot
sidebar_label: plot
---

# plot

Renders an explicit function y = f(x) from an ASCII math string on a 2D graph. Supports piecewise definitions, domain restrictions, excluded points (holes), and inequality region shading.

**Utility:** Plot an explicit function y = f(x) on a 2D graph

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d reference` | Yes | The 2D graph container to plot on |
| `equation` | `string \| def \| variable` | Yes | Function expression as a quoted ASCII math string, a def() reference, or a string variable |
| `range` | `range(min, max)` | No | Optional domain restriction for the x-axis |
| `color` | `c(colorName)` | No | Stroke color - e.g., c(blue), c(red) |
| `fillOpacity` | `fo(value)` | No | Fill opacity for inequality plots - e.g., fo(0.3) |

## Variants

### Simple explicit plot

```
plot(G, "f(x)")
```

Plot y = f(x) over the full visible x-range

### With domain restriction

```
plot(G, "f(x)", range(min, max))
```

Plot over a restricted x-domain

### From a def() definition

```
f = def(x, "x^2 + a")
plot(G, f)
```

Plot a previously defined function

### Piecewise function

```
plot(G, "expr1", "cond1", "expr2", "cond2")
```

Plot a piecewise function with alternating expression-condition pairs

### With hole (excluded point)

```
plot(G, "f(x)", "x != value")
```

Plot with an open circle at the excluded x-value

### Inequality region

```
plot(G, "y > f(x)")
```

Shade the region satisfying the inequality

### With color styling

```
plot(G, "f(x)", c(blue))
```

Plot with a custom stroke color

## Examples

### Plot a parabola

```
G = g2d(at(2, 2), 30, 30)
f = plot(G, "x^2")
```

### Plot sine function in blue

```
G = g2d(at(2, 3), 30, 30)
plot(G, "sin(x)", c(blue))
```

### Plot with restricted domain

```
G = g2d(at(2, 3), 30, 30)
plot(G, "x^2", range(-2, 2))
```

### Piecewise function: step function

```
G = g2d(at(2, 3), 20, 20)
plot(G, "1", "x>0", "-1", "x<0")
```

### Plot with a hole at x=1

```
G = g2d(at(2, 3), 30, 30)
plot(G, "(x^2-1)/(x-1)", "x != 1")
```

### Squeeze theorem: three curves together

```
G = g2d(at(2, 3), 30, 30, range(-2, 2, 0.5), range(-2, 2, 1))
plot(G, "x^2")
plot(G, "-x^2")
plot(G, "(x^2)sin(1/x)")
```

### Plot from a def() with parameter variable

```
G = g2d(at(2, 3), 30, 30)
a = -1
f = def(x, "x^2 + a")
g = def(x, "sin(x)")
h = f + g
plot(G, h)
```

### Inequality plot with fill opacity

```
G = g2d(at(2, 3), 14, 14)
plot(G, "y < x^2 + 1", c(orange), fo(0.3))
```
