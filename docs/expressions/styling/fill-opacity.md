---
title: fo
sidebar_label: fo
---

# fo

Inline modifier that controls fill opacity, from 0 (fully transparent) to 1 (fully opaque).

**Utility:** Set fill transparency on shapes using inline modifier

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `opacity` | `number (0-1)` | Yes | Opacity value from 0 (transparent) to 1 (opaque) |

## Variants

### Fully transparent fill

```
fo(0)
```

Fill is completely invisible, only stroke shows

### Light tint fill

```
fo(0.1)
```

Very light, barely visible fill

### Semi-transparent fill

```
fo(0.5)
```

Half-transparent fill

### Fully opaque fill

```
fo(1)
```

Completely solid fill with no transparency

### Combined with fill color

```
polygon(G, A, B, C, fc(yellow), fo(0.3))
```

Semi-transparent yellow fill on a polygon

### In effects panel

```
fill(A, fo(0.5))
```

Animate fill opacity change on an existing shape

## Examples

### Polygon with very light fill for linear programming

```
P = polygon(G, point(G, 0, 0), A, B, fo(0.1))
```

### Triangle with invisible fill and stroke

```
T = sss(G, 5, 4, 3, c(red), so(0), fo(0))
```

### Rectangle with full opacity fill image

```
r1 = rect(G, 12, 4, 4, 3, fi("tree", 0.7), fo(1), s(0.1))
```

### Plot with semi-transparent fill

```
plot(G5, eq5, c(orange), fo(0.3))
```

### Write expression with fill opacity

```
w = write(at(2, 3), "Hello x^2", fc(orange), fo(0.5), pd(10))
```
