---
title: textreplace
sidebar_label: textreplace
---

# textreplace

Animate substituting one text element with another by moving the source content to the target position while fading out the target. Creates a visual variable-substitution or term-replacement effect.

**Utility:** Copy source content to target position, target fades out

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `target` | `variable` | Yes | Text object to be replaced (will fade out) |
| `source` | `variable` | Yes | Source text object (content moves to target position) |
| `buff` | `buff(row, col)` | No | Position offset for replacement |
| `type` | `type(replace)` | No | Explicit replace mode |

## Variants

### Basic replace

```
textreplace(target, source)
```

Replace target with source content

### With offset and type

```
textreplace(target, source, buff(r, c), type(replace))
```

Replace with offset, explicit type

## Examples

### Replace label with selected term from equation

```
select_1 = select(write_2, "a^2-x^2", 1)
text_replace_6 = textreplace(label_3, select_1, buff(0, -2), type(replace))
```

### Replace variable in equation

```
M = write(at(2, 2), "x + 3 = 7", type(print))
val = write(at(1, 1), "4", type(print))
X = select(M, "x", 1)
textreplace(X, val)
```

### Substitute in formula

```
M = write(at(3, 2), "y = mx + b", type(print))
slope = write(at(1, 1), "2", type(print))
S = select(M, "m", 1)
textreplace(S, slope)
```
