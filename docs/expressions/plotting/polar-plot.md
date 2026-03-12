---
title: plot (polar)
sidebar_label: plot (polar)
---

# plot (polar)

Renders a polar function r = f(theta) on a polar or Cartesian grid. Supports theta range restriction, filled polar regions, and curves such as roses, cardioids, limacons, and spirals.

**Utility:** Plot a polar function r = f(theta) on a 2D or polar graph

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `p2d or g2d reference` | Yes | A polar grid (p2d) or standard 2D graph (g2d) |
| `equation` | `string` | Yes | Polar equation as ASCII math string - e.g., "2 + cos(3*theta)" |
| `range` | `range(thetaMin, thetaMax)` | No | Theta interval - e.g., range(0, 2*pi). Defaults to 0..2*pi |
| `color` | `c(colorName)` | No | Stroke color |
| `fillColor` | `fc(colorName)` | No | Fill color for filled polar regions |

## Variants

### Polar on polar grid (single string)

```js
plot(G, "r(theta)")
```

On a p2d grid, a single expression is treated as r = f(theta)

### Polar on polar grid with range

```js
plot(G, "theta", range(0, 4*pi))
```

Archimedean spiral: r = theta over multiple revolutions

### Polar as parametric (two strings)

```js
plot(G, "theta", "r(theta)")
```

Parametric form where first string is theta variable and second is r expression

### Filled polar region

```js
plot(G, "theta", "2 + cos(3*theta)", fc(yellow))
```

Polar curve with filled interior

## Examples

### Three-petal rose on polar grid

```js
G = p2d(at(2, 4), 20, 20, range(0, 10, 1), grid())
plot(G, "2 + cos(3*theta)")
```

### Archimedean spiral over two full turns

```js
G = p2d(at(2, 4), 20, 20, range(0, 10, 1), grid())
plot(G, "theta", range(0, 4*pi))
```

### Filled polar rose using parametric form

```js
G = p2d(at(2, 4), 20, 20, range(0, 10, 1), grid())
plot(G, "theta", "2 + cos(3*theta)", fc(yellow))
```

### Polar on standard g2d using parametric conversion

```js
G = g2d(at(2, 2), 20, 20)
plot(G, "t", "2 + cos(3*t)")
```
