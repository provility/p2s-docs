---
title: stroke
sidebar_label: stroke
---

# stroke

Standalone expression that animates the stroke color of existing shapes as a playable animation step. Takes shape references followed by a color name or hex string, with an optional opacity value between 0 and 1.

**Utility:** Animate stroke color change on existing shapes

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `shapes` | `variable references` | Yes | One or more variable references to existing shapes - e.g., A, B, L |
| `color` | `colorName \| "#hex"` | Yes | Color name (unquoted) or hex/color string (quoted) - e.g., red, "#ff0000" |
| `opacity` | `number (0-1)` | No | Stroke opacity from 0 (transparent) to 1 (opaque) |

## Variants

### Single shape, named color

```js
stroke(A, red)
```

Change stroke color of one shape to red

### Single shape, quoted color

```js
stroke(A, "red")
```

Change stroke color using a quoted string

### Single shape, hex color

```js
stroke(A, "#ff0000")
```

Change stroke color using a hex code

### With opacity

```js
stroke(A, blue, 0.5)
```

Change stroke color with 50% opacity

### Multiple shapes

```js
stroke(A, B, C, green)
```

Change stroke color of multiple shapes at once

### Multiple shapes with opacity

```js
stroke(A, B, red, 0.8)
```

Change stroke of multiple shapes with opacity

### Stroke width change

```js
strokewidth(A, 3)
```

Change stroke width of a shape to 3 pixels

### Stroke width multiple shapes

```js
strokewidth(A, B, C, 2)
```

Change stroke width of multiple shapes

## Examples

### Change stroke color of points and line to green

```js
stroke(A, B, L, "green")
```

### Highlight a selected math text item in red

```js
stroke(first, "red")
```

### Effects panel stroke color with duration

```js
effect_1 = stroke(A, B, c(red), t(1))
```

### Change stroke width of a shape

```js
strokewidth(A, 3)
```
