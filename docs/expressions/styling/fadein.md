---
title: fadein
sidebar_label: fadein
---

# fadein

Animated visibility transition that gradually reveals one or more hidden shapes with a smooth fade-in effect.

**Utility:** Gradually fade in hidden shapes with smooth animation

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `shapes` | `variable references` | Yes | One or more variable references to hidden shapes to fade in - e.g., A, B, L |

## Variants

### Fade in single shape

```js
fadein(A)
```

Fade in one shape with animation

### Fade in multiple shapes

```js
fadein(A, B, C)
```

Fade in several shapes simultaneously

## Examples

### Fade in a construction line after hiding it

```js
fadein(L1)
```

### Fade in multiple shapes together

```js
fadein(point_1, line_1, label_1)
```

### Hide then fade in as part of an animation sequence

```js
seq(hide(A, B), fadein(A), fadein(B))
```
