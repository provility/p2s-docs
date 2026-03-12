---
title: g3d
sidebar_label: g3d
---

# g3d

Creates a 3D graph container for rendering geometry, surfaces, and solids with configurable coordinate system, axis ranges, and gridline visibility.

**Utility:** Create a 3D graph container for 3D geometry and surface rendering

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `position` | `at(row, col)` | Yes | Logical position on the canvas using at(row, col) |
| `height` | `number` | Yes | Container height in logical row units (e.g., 20, 30) |
| `width` | `number` | Yes | Container width in logical column units (e.g., 20, 30) |
| `axes3d | ranges` | `axes3d(...) \| range(), range(), range()` | No | Axis configuration - either an axes3d() bundle or up to 3 individual range() expressions for x, y, z |
| `type` | `type(lhs) \| type(rhs) \| type(space)` | No | Coordinate system: lhs (default, Z up), rhs (Y up), or space (bare, no axes) |

## Variants

### Basic with defaults

```js
g3d(at(row, col), height, width)
```

LHS coordinate system with default -5 to 5 ranges on all axes

### With individual ranges

```js
g3d(at(row, col), height, width, range(-10, 10), range(-10, 10), range(-5, 5))
```

Custom x, y, z ranges using separate range() expressions

### With axes3d bundle

```js
g3d(at(row, col), height, width, axes3d(range3d(range(-10, 10), range(-10, 10), range(-5, 5))))
```

Ranges bundled inside axes3d with range3d

### With gridlines enabled

```js
g3d(at(row, col), height, width, axes3d(range3d(range(-5, 5), range(-5, 5), range(-5, 5)), "gridlines", "lhs"))
```

LHS system with visible gridlines on the 3D axes

### RHS coordinate system

```js
g3d(at(row, col), height, width, range(-5, 5), range(-5, 5), range(-5, 5), type(rhs))
```

Right-Hand System: X right, Y up, Z towards viewer

### Space mode (no axes)

```js
g3d(at(row, col), height, width, type(space))
```

Bare 3D space with no axes or grid, for solids and group animations

## Examples

### Full-screen 3D graph for tangent plane visualization

```js
G = g3d(at(0, 0), 30, 30)
```

### 3D graph positioned at row 5, col 5 for solid of revolution

```js
G = g3d(at(5, 5), 20, 20)
```

### Space mode for box-fold animation with group transforms

```js
S = g3d(at(0, 0), 30, 30, type(space))
```

### 3D graph with custom ranges and gridlines

```js
G = g3d(at(0, 0), 25, 25, axes3d(range3d(range(-10, 10), range(-10, 10), range(-5, 5)), "gridlines", "lhs"))
```

### RHS system with gridlines for standard math visualization

```js
G = g3d(at(0, 0), 30, 30, axes3d(range3d(range(-5, 5), range(-5, 5), range(-5, 5)), "gridlines", "rhs"))
```

### 3D graph with separate range expressions

```js
G = g3d(at(5, 5), 20, 20, range(-3, 3), range(-3, 3), range(-3, 3))
```
