---
title: s
sidebar_label: s
---

# s

Inline modifier that sets the stroke (outline) thickness in pixels. Accepts a positive number for line width, ranging from 0.1 (very thin) to 10 (very thick), with a default of 1.

**Utility:** Set stroke width/thickness on shapes using inline modifier

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `width` | `number` | Yes | Stroke width in pixels - positive number, e.g., 0.5, 1, 2, 5 |

## Variants

### Thin stroke

```
s(0.1)
```

Very thin stroke, nearly invisible outline

### Default stroke

```
s(1)
```

Standard stroke width

### Medium stroke

```
s(2)
```

Medium thickness stroke

### Thick stroke

```
s(5)
```

Thick visible stroke

### Inside shape with other modifiers

```
rect(G, 12, 4, 4, 3, fi("tree", 0.7), fo(1), s(0.1))
```

Combine stroke width with fill image and fill opacity

## Examples

### Rectangle with thin stroke and fill image

```
r1 = rect(G, 12, 4, 4, 3, fi("tree", 0.7), fo(1), s(0.1))
```

### Arrow with thick stroke

```
arrow(at(T, 1, 1), at(P1), -2, c(red), s(5))
```

### Effects panel stroke width change

```
effect_1 = stroke(A, B, s(3))
```
