---
title: writeonly
sidebar_label: writeonly
---

# writeonly

Render a mathematical expression animating only the selected portions while all other terms appear as invisible phantom placeholders. Useful for emphasizing specific terms in step-by-step derivations.

**Utility:** Render expression animating only selected portions, rest as phantoms

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `position` | `at(row, col)` | Yes | Position using logical row, col coordinates |
| `content` | `string` | Yes | Full ASCII math expression including all terms |
| `filters` | `select("pattern", index), ...` | Yes | One or more select filters specifying which terms to animate |
| `renderType` | `type(write) \| type(print)` | Yes | type(write) for animated, type(print) for instant |
| `color` | `c(colorName)` | No | Color for animated portions - e.g., c(blue) |

## Variants

### Single term animation

```
writeonly(at(row, col), "full expression", select("term", 1), type(write))
```

Animate only the matched term

### With color highlight

```
writeonly(at(row, col), "expression", select("term", 1), type(write), c(blue))
```

Animate term in specified color

## Examples

### Animate only the substituted term in trig identity

```
write_only_1 = writeonly(at(11, 3), "sqrt(a^2-x^2) = sqrt(a^2-a^2 sin^2(theta))", select("a^2 sin^2(theta)", 1), type(write), c(blue))
```

### Reveal only the answer portion

```
writeonly(at(5, 2), "x^2 + 2x + 1 = (x+1)^2", select("(x+1)^2", 1), type(write))
```

### Highlight derivative result

```
writeonly(at(4, 3), "d/dx[sin(x)] = cos(x)", select("cos(x)", 1), type(write), c(red))
```

### Show factored form emphasis

```
writeonly(at(6, 4), "x^2 - 4 = (x-2)(x+2)", select("(x-2)(x+2)", 1), type(write))
```
