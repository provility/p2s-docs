---
title: revolution
sidebar_label: revolution
---

# revolution

Generates a solid of revolution by rotating a bounded planar region around the x-axis or y-axis, with an optional sweep angle for partial rotations.

**Utility:** Create a solid of revolution by rotating a region around an axis

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d reference` | Yes | The 3D graph container |
| `region` | `region3d reference` | Yes | The region to revolve, created from two curve3d boundaries via region3d() |
| `axis` | `string` | Yes | Axis of revolution: "x" or "y" |
| `angle` | `number` | No | Sweep angle in degrees (default 360 for full revolution) |
| `color` | `c(colorName)` | No | Surface color - e.g., c("magenta") |

## Variants

### Full revolution around x-axis

```js
revolution(G, R, "x")
```

360-degree revolution around the x-axis

### Full revolution around y-axis

```js
revolution(G, R, "y")
```

360-degree revolution around the y-axis

### Partial revolution with angle

```js
revolution(G, R, "x", 180)
```

Half revolution (180 degrees) around x-axis

### Revolution with color

```js
revolution(G, R, "x", c("magenta"))
```

Full revolution with custom color

## Examples

### Solid of revolution around x-axis from linear boundary

```js
G = g3d(at(5, 5), 20, 20)
c1 = plot3d(G, "t", "0.5*t", "0", range(0, 4), c("green"))
c2 = plot3d(G, "4", "t", "0", range(0, 2), c("green"))
R = region3d(G, c1, c2, c("cyan"))
rl = revolution(G, R, "x", c("magenta"))
```

### Solid of revolution around y-axis from parabolic curve

```js
G = g3d(at(5, 5), 20, 20)
c1 = plot3d(G, "t^2+1", "t", "0", range(-1, 1), c("magenta"))
c2 = plot3d(G, "0", "t", "0", range(-1, 1), c("green"))
R = region3d(G, c1, c2, c("cyan"))
rl = revolution(G, R, "y", c("magenta"))
```
