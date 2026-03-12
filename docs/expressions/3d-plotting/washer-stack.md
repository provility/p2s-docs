---
title: washerstack
sidebar_label: washerstack
---

# washerstack

Approximates a solid of revolution using the washer method by stacking annular cross-sections defined by outer and inner radius functions.

**Utility:** Visualize the washer method for volume between two curves of revolution

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d reference` | Yes | The 3D graph container |
| `outerEquation` | `string` | Yes | Outer radius function as quoted string - e.g., "sqrt(x)" |
| `innerEquation` | `string` | Yes | Inner radius function as quoted string - e.g., "x^2" |
| `axis` | `string` | Yes | Axis of revolution: "x" or "y" |
| `rangeMin` | `number` | Yes | Lower bound of integration |
| `rangeMax` | `number` | Yes | Upper bound of integration |
| `count` | `number` | Yes | Number of washers to display |
| `color` | `c(colorName)` | No | Washer color - e.g., c("orange") |

## Variants

### Washers along x-axis

```js
washerstack(S, "sqrt(x)", "x^2", "x", 0, 1, 10)
```

Washers between sqrt(x) and x^2 rotated around x-axis

### Washers along y-axis

```js
washerstack(S, "R(y)", "r(y)", "y", 0, 2, 8)
```

Washers between two functions of y rotated around y-axis

### Washers with color

```js
washerstack(S, "sqrt(x)", "x^2", "x", 0, 1, 10, c("orange"))
```

Colored washers

## Examples

### Washer method between sqrt(x) and x^2

```js
S = g3d(at(5, 5), 20, 20)
c1 = plot3d(S, "t", "sqrt(t)", "0", range(0, 1), c("magenta"))
c2 = plot3d(S, "t", "t^2", "0", range(0, 1), c("green"))
washerstack(S, "sqrt(x)", "x^2", "x", 0, 1, 10, c("orange"))
```
