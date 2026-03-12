---
title: show
sidebar_label: show
---

# show

Instantly reveals one or more previously hidden shapes on the canvas. Supports a type(only) variant that shows specified shapes while hiding everything else.

**Utility:** Instantly show one or more hidden shapes on the canvas

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `shapes` | `variable references` | Yes | One or more variable references to shapes to show - e.g., A, B, L |
| `type` | `type(only)` | No | When type(only) is specified, shows these shapes and hides all others |

## Variants

### Show single shape

```
show(A)
```

Show one hidden shape instantly

### Show multiple shapes

```
show(A, B, C)
```

Show several hidden shapes at once

### Show only (focus mode)

```
show(A, B, type(only))
```

Show only these shapes, hide everything else

### Show with duration (effects panel)

```
show(A, B, type(only), t(1))
```

Show-only with a timed transition

## Examples

### Show a single hidden shape

```
show(A)
```

### Show multiple shapes at once

```
show(L1, L2, L3)
```

### Focus on specific shapes, hiding everything else

```
show(triangle_1, label_1, type(only))
```
