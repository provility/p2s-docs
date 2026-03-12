---
title: fadeout
sidebar_label: fadeout
---

# fadeout

Animated visibility transition that gradually hides one or more visible shapes with a smooth fade-out effect.

**Utility:** Gradually fade out visible shapes with smooth animation

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `shapes` | `variable references` | Yes | One or more variable references to visible shapes to fade out - e.g., A, B, L |

## Variants

### Fade out single shape

```js
fadeout(A)
```

Fade out one shape with animation

### Fade out multiple shapes

```js
fadeout(A, B, C)
```

Fade out several shapes simultaneously

## Examples

### Fade out a construction line

```js
fadeout(L1)
```

### Fade out multiple shapes together

```js
fadeout(point_1, line_1, label_1)
```

### Fade out then fade in as transition

```js
seq(fadeout(step1_shapes), fadein(step2_shapes))
```
