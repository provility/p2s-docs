---
title: diskstack
sidebar_label: diskstack
---

# diskstack

Approximates a solid of revolution using the disk method by stacking circular cross-sectional slices perpendicular to the axis of rotation.

**Utility:** Visualize the disk method for volume of revolution

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g3d reference` | Yes | The 3D graph container |
| `region` | `region3d reference` | Yes | The region defining the disk profile, from region3d() |
| `axis` | `string` | Yes | Axis of revolution: "x" or "y" |
| `count` | `number` | Yes | Number of disks to display |
| `color` | `c(colorName)` | No | Disk color - e.g., c("green") |

## Variants

### Disk stack along x-axis

```
diskstack(G, R, "x", 10)
```

10 disks stacked along x-axis

### Disk stack along y-axis

```
diskstack(G, R, "y", 20)
```

20 disks stacked along y-axis

### Disk stack with color

```
diskstack(G, R, "x", 10, c("green"))
```

Colored disk stack

## Examples

### Disk method around x-axis with linear boundary

```
G = g3d(at(5, 5), 20, 20)
c1 = plot3d(G, "t", "0.5*t", "0", range(0, 4), c("green"))
c2 = plot3d(G, "4", "t", "0", range(0, 2), c("green"))
R = region3d(G, c1, c2, c("cyan"))
d1 = diskstack(G, R, "x", 20, c("green"))
```

### Disk method around y-axis with parabolic curve

```
G = g3d(at(5, 5), 20, 20)
c1 = plot3d(G, "t^2+1", "t", "0", range(-1, 1), c("magenta"))
c2 = plot3d(G, "0", "t", "0", range(-1, 1), c("green"))
R = region3d(G, c1, c2, c("cyan"))
d1 = diskstack(G, R, "y", 20, c("green"))
```
