---
title: areaunder
sidebar_label: areaunder
---

# areaunder

Shades the region between a curve and the x-axis over a specified x-interval, representing the definite integral. Supports custom color and opacity for visualizing signed area and accumulation.

**Utility:** Shade the area under a curve between two x-values

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d reference` | Yes | The 2D graph container |
| `plotVariable` | `plot reference` | Yes | A previously assigned plot variable - e.g., f from f = plot(G, "x^2") |
| `xmin` | `number` | Yes | Left bound of the shaded interval |
| `xmax` | `number` | Yes | Right bound of the shaded interval |
| `color` | `string` | No | Fill color name - e.g., "blue", "red". Default is blue |
| `opacity` | `number` | No | Fill opacity from 0 to 1. Default is 0.3 |

## Variants

### Basic area under curve

```
f = plot(G, "f(x)")
areaunder(G, f, xmin, xmax)
```

Shade area under f(x) between xmin and xmax with default blue fill

### With custom color

```
f = plot(G, "f(x)")
areaunder(G, f, xmin, xmax, "red")
```

Shade with a custom fill color

### With custom color and opacity

```
f = plot(G, "f(x)")
areaunder(G, f, xmin, xmax, "green", 0.5)
```

Shade with custom color and opacity

## Examples

### Area under x^2 from 0 to 2

```
G = g2d(at(2, 2), 30, 30)
f = plot(G, "x^2")
areaunder(G, f, 0, 2)
```

### Area under sine curve from 0 to pi in red

```
G = g2d(at(2, 2), 30, 30)
f = plot(G, "sin(x)")
areaunder(G, f, 0, 3.14, "red", 0.4)
```

### Visualize signed area (negative region)

```
G = g2d(at(2, 2), 30, 30)
f = plot(G, "x^3 - x")
areaunder(G, f, -1, 1)
```
