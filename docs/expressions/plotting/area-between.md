---
title: areabetween
sidebar_label: areabetween
---

# areabetween

Shades the enclosed region between two plotted curves, automatically computing intersection boundaries. Used for visualizing definite integrals and area comparisons between functions.

**Utility:** Shade the area between two curves on a 2D graph

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d reference` | Yes | The 2D graph container |
| `plot1` | `plot reference` | Yes | First plot variable - the upper or lower curve |
| `plot2` | `plot reference` | Yes | Second plot variable - the other bounding curve |
| `color` | `string` | No | Fill color name - e.g., "purple". Default is blue |
| `opacity` | `number` | No | Fill opacity from 0 to 1. Default is 0.3 |

## Variants

### Basic area between two curves

```
f = plot(G, "f(x)")
g = plot(G, "g(x)")
areabetween(G, f, g)
```

Shade the region between f and g with default styling

### With custom color and opacity

```
f = plot(G, "f(x)")
g = plot(G, "g(x)")
areabetween(G, f, g, "purple", 0.5)
```

Shade with custom color and opacity

## Examples

### Area between x^2 and x

```
G = g2d(at(2, 2), 30, 30)
f = plot(G, "x^2")
g = plot(G, "x")
areabetween(G, f, g)
```

### Area between sine and cosine

```
G = g2d(at(2, 2), 30, 30)
f = plot(G, "sin(x)")
g = plot(G, "cos(x)")
areabetween(G, f, g, "purple", 0.4)
```

### Area between a parabola and a line

```
G = g2d(at(2, 2), 30, 30)
f = plot(G, "x^2")
g = plot(G, "2*x + 3")
areabetween(G, f, g, "green")
```
