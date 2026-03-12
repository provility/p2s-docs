---
title: plot (parametric)
sidebar_label: plot (parametric)
---

# plot (parametric)

Renders a parametric curve defined by x(t) and y(t) component expressions over a parameter interval. Suited for spirals, cycloids, Lissajous figures, and other curves not expressible as y = f(x).

**Utility:** Plot a parametric curve x(t), y(t) on a 2D graph

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d reference` | Yes | The 2D graph container to plot on |
| `xExpr` | `string` | Yes | x-component as ASCII math string using variable t - e.g., "cos(t)" |
| `yExpr` | `string` | Yes | y-component as ASCII math string using variable t - e.g., "sin(t)" |
| `range` | `range(tMin, tMax)` | Yes | Parameter interval - e.g., range(0, 2*pi) |
| `color` | `c(colorName)` | No | Stroke color - e.g., c(green) |

## Variants

### Basic parametric curve

```
plot(G, "x(t)", "y(t)", range(tMin, tMax))
```

Plot a parametric curve over the given t interval

### With color

```
plot(G, "x(t)", "y(t)", range(tMin, tMax), c(green))
```

Parametric curve with custom stroke color

### From def() definitions

```
xf = def(t, "cos(t)")
yf = def(t, "sin(t)")
plot(G, xf, yf, range(0, 2*pi))
```

Parametric curve using function definitions

## Examples

### Unit circle as parametric curve

```
G = g2d(at(2, 2), 20, 20)
plot(G, "cos(t)", "sin(t)", range(0, 2*pi))
```

### Ellipse with parameters a and b

```
G = g2d(at(2, 2), 20, 20)
a = 3
b = 2
plot(G, "a*cos(t)", "b*sin(t)", range(0, 2*pi), c(green))
```

### Cycloid curve

```
G = g2d(at(2, 2), 20, 20)
plot(G, "t - sin(t)", "1 - cos(t)", range(0, 4*pi))
```

### Spiral curve

```
G = g2d(at(2, 2), 20, 20)
plot(G, "t*cos(t)", "t*sin(t)", range(0, 6*pi))
```
