---
title: nl
sidebar_label: nl
---

# nl

Creates a 1D number line with configurable range and tick marks for visualizing intervals, inequalities, and single-variable concepts.

**Utility:** Create a 1D number line container for intervals and single-variable visualization

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `position` | `at(row, col)` | Yes | Logical position using at(row, col) coordinates on the canvas grid |
| `height` | `number` | Yes | Height in logical row units (typically small, e.g., 6) |
| `width` | `number` | Yes | Width in logical column units (e.g., 19.4) |
| `range` | `range(min, max) \| range(min, max, step)` | No | Value range displayed on the number line with optional tick step |
| `grid` | `grid()` | No | Show tick marks on the number line |

## Variants

### Basic number line

```
nl(at(row, col), height, width, range(min, max))
```

Number line with specified range, no tick marks

### Number line with ticks

```
nl(at(row, col), height, width, range(min, max), grid())
```

Number line with tick marks shown

### Number line with custom step

```
nl(at(row, col), height, width, range(min, max, step), grid())
```

Number line with custom tick spacing

### Number line with border

```
nl(at(row, col), height, width, range(min, max), grid(), br(0.5))
```

Number line with border shadow

## Examples

### Basic number line from 0 to 10 with tick marks

```
nl_1 = nl(at(3.1, 9.4), 6, 19.4, range(0, 10), grid())
```

### Number line with an interval marked

```
nl_1 = nl(at(3.1, 9.4), 6, 19.4, range(0, 10), grid())
interval_1 = interval(nl_1, 2, 6, type(closed), buff(-19))
```
