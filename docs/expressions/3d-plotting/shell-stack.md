---
title: shellstack
sidebar_label: shellstack
---

# shellstack

Approximates a solid of revolution using the cylindrical shell method by stacking concentric cylindrical shells with specified radius and height functions.

**Utility:** Visualize the cylindrical shell method for volume of revolution

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d reference` | Yes | The 3D graph container |
| `radiusEquation` | `string` | Yes | Radius function (distance from axis) as quoted string - e.g., "x" |
| `heightEquation` | `string` | Yes | Height function as quoted string - e.g., "x^2" |
| `axis` | `string` | Yes | Axis shells wrap around: "y" for shells around y-axis, "x" for shells around x-axis |
| `rangeMin` | `number` | Yes | Lower bound of integration |
| `rangeMax` | `number` | Yes | Upper bound of integration |
| `count` | `number` | Yes | Number of shells to display |
| `color` | `c(colorName)` | No | Shell color - e.g., c("cyan") |

## Variants

### Shells around y-axis

```
shellstack(S, "x", "x^2", "y", 0, 1, 8)
```

Cylindrical shells for y = x^2 rotated around y-axis

### Shells around x-axis

```
shellstack(S, "y", "f(y)", "x", 0, 2, 6)
```

Cylindrical shells rotated around x-axis

### Shells with color

```
shellstack(S, "x", "x^2", "y", 0, 1, 8, c("cyan"))
```

Colored cylindrical shells

## Examples

### Shell method for y = x^2 around y-axis

```
S = g3d(at(5, 5), 20, 20)
c1 = plot3d(S, "t^2+1", "t", "0", range(-1, 1), c("magenta"))
c2 = plot3d(S, "0", "t", "0", range(-1, 1), c("green"))
R = region3d(S, c1, c2, c("cyan"))
rl = revolution(S, R, "y", c("magenta"))
shellstack(S, "x", "x^2", "y", 0, 1, 8, c("cyan"))
```
