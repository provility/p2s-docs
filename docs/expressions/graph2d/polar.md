---
title: p2d
sidebar_label: p2d
---

# p2d

Creates a 2D polar coordinate graph with concentric radial gridlines, configurable radius bounds, and angular divisions.

**Utility:** Create a 2D polar coordinate graph for polar functions and polar point placement

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `position` | `at(row, col)` | Yes | Logical position on canvas |
| `height` | `number` | Yes | Height in logical row units |
| `width` | `number` | Yes | Width in logical column units |
| `radius` | `radius(rMax) \| radius(rMax, rStep)` | Yes | Maximum radius. Optional step controls concentric circle spacing. |
| `grid` | `grid()` | No | Show polar grid (concentric circles + radial lines) |
| `border` | `br(radius)` | No | Border shadow effect |

## Variants

### Polar graph with max radius

```
p2d(at(row, col), height, width, radius(rMax))
```

Polar graph with auto grid spacing

### Polar graph with step

```
p2d(at(row, col), height, width, radius(rMax, rStep))
```

Polar graph with custom concentric circle spacing

### Polar graph with grid

```
p2d(at(row, col), height, width, radius(rMax), grid())
```

Polar graph showing concentric circles and radial lines

### Polar graph with grid and shadow

```
p2d(at(row, col), height, width, radius(rMax), grid(), br(0.5))
```

Full-featured polar graph

## Examples

### Polar graph with grid for plotting

```
G = p2d(at(2, 4), 20, 20, range(0, 10, 1), grid())
```

### Plot a polar rose curve

```
G = p2d(at(2, 4), 20, 20, range(0, 10, 1), grid())
plot(G, "2 + cos(3*theta)")
```

### Point in polar coordinates on polar graph

```
point(G, 5, 30, type(polar))
```
