---
title: hide
sidebar_label: hide
---

# hide

Instantly hides one or more shapes on the canvas. Hidden shapes remain in the scene but are not rendered, and can be revealed later.

**Utility:** Instantly hide one or more shapes from the canvas

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `shapes` | `variable references` | Yes | One or more variable references to shapes to hide - e.g., A, B, L |

## Variants

### Hide single shape

```
hide(A)
```

Hide one shape instantly

### Hide multiple shapes

```
hide(A, B, C)
```

Hide several shapes at once

### Hide with duration (effects panel)

```
hide(A, B, t(1))
```

Hide shapes with a timed transition

## Examples

### Hide intersection points and construction lines for parabola ray animation

```
hide(L1, L2, L3, L4, L5, H1, H2, H3, H4, H5)
```

### Hide a computed selection result

```
hide(select_3)
```

### Hide single shape

```
hide(A)
```
