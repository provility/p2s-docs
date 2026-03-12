---
title: plot (implicit)
sidebar_label: plot (implicit)
---

# plot (implicit)

Renders an implicit curve defined by an equation f(x, y) = 0 on a 2D graph. Supports arbitrary algebraic curves including circles, ellipses, hyperbolas, and higher-order relations.

**Utility:** Plot an implicit curve f(x, y) = 0 on a 2D graph

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d reference` | Yes | The 2D graph container to plot on |
| `equation` | `string` | Yes | Implicit equation as ASCII math string - e.g., "x^2 + y^2 - 25" |
| `color` | `c(colorName)` | No | Stroke color - e.g., c(red) |

## Variants

### Basic implicit plot

```
plot(G, "f(x,y)")
```

Plot the implicit curve where f(x,y) = 0

### With color

```
plot(G, "f(x,y)", c(red))
```

Implicit curve with custom stroke color

### From a string variable

```
eq = "x^2 + y^2 - 25"
plot(G, eq)
```

Implicit curve from a previously assigned string variable

## Examples

### Circle of radius 5

```
G = g2d(at(2, 2), 20, 20)
plot(G, "x^2 + y^2 - 25")
```

### Hyperbola xy = 1

```
G = g2d(at(2, 2), 20, 20)
plot(G, "x*y - 1")
```

### Lemniscate of Bernoulli

```
G = g2d(at(2, 2), 20, 20)
a = 3
plot(G, "(x^2 + y^2)^2 - a^2*(x^2 - y^2)", c(red))
```

### Folium of Descartes

```
G = g2d(at(2, 2), 20, 20)
a = 3
plot(G, "x^3 + y^3 - a*x*y")
```
