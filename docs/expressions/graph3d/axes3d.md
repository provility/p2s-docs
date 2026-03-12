---
title: axes3d
sidebar_label: axes3d
---

# axes3d

Bundles 3D axis ranges with gridline visibility and coordinate system options (LHS or RHS) into a single axis configuration for a 3D graph.

**Utility:** Bundle 3D axis ranges and display options for a g3d container

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `range3d` | `range3d(xRange, yRange, zRange)` | Yes | A range3d expression bundling three range() expressions for x, y, z axes |
| `grid3d` | `grid3d(c(color), s(width))` | No | Grid styling configuration for color and stroke width |
| `gridlines` | `"gridlines"` | No | String option to enable gridline rendering (default: hidden) |
| `nogrid` | `"nogrid"` | No | String option to hide everything including axes |
| `coordSystem` | `"lhs" \| "rhs"` | No | Coordinate system: lhs (default, Z up) or rhs (Y up) |

## Variants

### Axes only (default)

```
axes3d(range3d(range(-10, 10), range(-10, 10), range(-5, 5)))
```

Show axes with no gridlines (default behavior)

### With gridlines

```
axes3d(range3d(range(-5, 5), range(-5, 5), range(-5, 5)), "gridlines")
```

Show axes and gridlines

### Gridlines with LHS system

```
axes3d(range3d(range(-5, 5), range(-5, 5), range(-5, 5)), "gridlines", "lhs")
```

LHS coordinate system with visible gridlines

### RHS system with gridlines

```
axes3d(range3d(range(-5, 5), range(-5, 5), range(-5, 5)), "gridlines", "rhs")
```

RHS coordinate system with visible gridlines

### No grid at all

```
axes3d(range3d(range(-5, 5), range(-5, 5), range(-5, 5)), "nogrid")
```

Hide all axes and gridlines

### Styled gridlines

```
axes3d(range3d(range(-5, 5), range(-5, 5), range(-5, 5)), grid3d(c(gray)), "gridlines")
```

Gridlines with custom color styling

## Examples

### 3D graph with LHS gridlines

```
G = g3d(at(0, 0), 30, 30, axes3d(range3d(range(-5, 5), range(-5, 5), range(-5, 5)), "gridlines", "lhs"))
```

### 3D graph with RHS gridlines

```
G = g3d(at(0, 0), 30, 30, axes3d(range3d(range(-5, 5), range(-5, 5), range(-5, 5)), "gridlines", "rhs"))
```

### 3D graph with gray styled gridlines

```
G = g3d(at(5, 5), 20, 20, axes3d(range3d(range(-10, 10), range(-10, 10), range(-5, 5)), grid3d(c(gray)), "gridlines"))
```

### 3D graph with axes only, no gridlines

```
G = g3d(at(0, 0), 25, 25, axes3d(range3d(range(-10, 10), range(-10, 10), range(-10, 10))))
```
