---
title: range3d
sidebar_label: range3d
---

# range3d

Bundles three axis range definitions (x, y, z) into a single unit for configuring 3D coordinate bounds.

**Utility:** Bundle x, y, z range expressions for 3D axes configuration

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `xRange` | `range(min, max)` | Yes | X-axis range expression |
| `yRange` | `range(min, max)` | Yes | Y-axis range expression |
| `zRange` | `range(min, max)` | Yes | Z-axis range expression |

## Variants

### Uniform ranges

```js
range3d(range(-5, 5), range(-5, 5), range(-5, 5))
```

Same range on all three axes

### Asymmetric ranges

```js
range3d(range(-10, 10), range(-10, 10), range(-5, 5))
```

Different range for z-axis (e.g., height-limited)

### With step sizes

```js
range3d(range(-10, 10, 2), range(-10, 10, 2), range(-5, 5, 1))
```

Custom step size on each axis for tick marks

### With trig scale

```js
range3d(range(-2*pi, 2*pi, pi/4, "trig"), range(-10, 10), range(-5, 5))
```

Trigonometric labels on x-axis

## Examples

### Standard symmetric 3D range inside axes3d

```js
G = g3d(at(0, 0), 30, 30, axes3d(range3d(range(-5, 5), range(-5, 5), range(-5, 5))))
```

### Wide x-y range with limited z for surface plots

```js
G = g3d(at(0, 0), 30, 30, axes3d(range3d(range(-10, 10), range(-10, 10), range(-5, 5)), "gridlines"))
```

### Narrow range for close-up 3D visualization

```js
G = g3d(at(5, 5), 20, 20, axes3d(range3d(range(-3, 3), range(-3, 3), range(-3, 3)), "gridlines", "lhs"))
```

### Trig-labeled x-axis for 3D parametric surfaces

```js
G = g3d(at(0, 0), 25, 25, axes3d(range3d(range(-2*pi, 2*pi, pi/4, "trig"), range(-10, 10), range(-5, 5))))
```
