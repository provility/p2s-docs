---
title: range
sidebar_label: range
---

# range

Defines the visible axis range with minimum and maximum bounds, optional tick step spacing, and scale type such as trigonometric or logarithmic.

**Utility:** Set axis range with min, max, optional step, and optional scale type for a graph axis

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `min` | `number \| expression` | Yes | Minimum value on the axis (e.g., -5, -2*pi) |
| `max` | `number \| expression` | Yes | Maximum value on the axis (e.g., 5, 2*pi) |
| `step` | `number \| expression` | No | Tick spacing on the axis (e.g., 1, 0.5, pi/4). If omitted, step is calculated automatically. |
| `scale` | `"trig" \| "log" \| "ln" \| "im"` | No | Scale type for axis labels. 'trig' shows pi-fraction labels, 'log' is base-10 log, 'ln' is natural log, 'im' shows imaginary unit labels. |

## Variants

### Basic range (min and max)

```
range(min, max)
```

Set axis bounds with automatic tick step

### Range with step

```
range(min, max, step)
```

Set axis bounds with explicit tick spacing

### Trig range with pi labels

```
range(-2*pi, 2*pi, pi/4, "trig")
```

Pi-based axis labels for trigonometric function plots

### Range for plot domain restriction

```
plot(G, "f(x)", range(a, b))
```

When used inside plot(), restricts the plotted domain

## Examples

### Standard symmetric range

```
G = g2d(at(2, 2), 20, 20, range(-5, 5), range(-5, 5))
```

### Range with custom step on both axes

```
G = g2d(at(2, 3), 30, 30, range(-2, 2, 0.5), range(-2, 2, 1))
```

### Asymmetric range for positive-heavy data

```
G = g2d(at(1, 14), 12, 18, range(-1, 5, 1), range(-1, 15, 2))
```

### Single x-range only (y defaults)

```
G = g2d(at(2, 2), 20, 30, range(-1, 10))
```

### Trig range for sine/cosine plotting

```
G = g2d(at(2, 2), 20, 30, range(-2*pi, 2*pi, pi/4, "trig"), range(-2, 2))
```

### Inverse trig range on y-axis

```
G = g2d(at(2, 2), 20, 30, range(-1, 1), range(-pi, pi, pi/4, "trig"))
```

### Range used in polar plot domain

```
plot(G, "theta", range(0, 4*pi))
```
