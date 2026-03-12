---
title: writesub
sidebar_label: writesub
---

# writesub

Render a mathematical expression with automatic find-and-replace substitution applied before display. Useful for showing algebraic variable replacements and term transformations inline.

**Utility:** Render math text with find-and-replace pattern substitution

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `position` | `at(row, col)` | Yes | Position using logical row, col coordinates |
| `content` | `string` | Yes | Full ASCII math expression in quotes - e.g., "x^2 + 2x + 1" |
| `find` | `string` | Yes | ASCII pattern to find within the expression - e.g., "x" |
| `replace` | `string` | Yes | ASCII replacement text - e.g., "y", "(a+b)" |
| `renderType` | `type(print) \| type(write)` | No | type(print) for instant KaTeX (default), type(write) for animated pen-tracing |
| `color` | `c(colorName)` | No | Text color - e.g., c(blue), c(red) |
| `fontSize` | `f(size)` | No | Font size in pixels - e.g., f(24) |

## Variants

### Basic substitution

```js
writesub(at(row, col), "content", "find", "replace")
```

Instant rendering with substitution

### Animated substitution

```js
writesub(at(row, col), "content", "find", "replace", type(write))
```

Pen-tracing animation with substitution

### Instant with print

```js
writesub(at(row, col), "content", "find", "replace", type(print))
```

Instant KaTeX rendering (default behavior)

### With styling

```js
writesub(at(row, col), "content", "find", "replace", type(write), c(blue))
```

Animated with color styling

## Examples

### Substitute variable x with y in quadratic

```js
sub_1 = writesub(at(3, 2), "x^2 + 2x + 1", "x", "y", type(write))
```

### Replace x with (a+b) in expression

```js
sub_2 = writesub(at(5, 2), "x^2 - 1", "x", "(a+b)", type(print))
```

### Substitute theta with pi/6 in trig expression

```js
sub_3 = writesub(at(7, 3), "sin(theta) + cos(theta)", "theta", "pi/6", type(write))
```

### Replace fraction in calculus expression

```js
sub_4 = writesub(at(9, 2), "int 1/x dx = ln|x|", "1/x", "u", type(write), c(blue))
```

### Variable substitution with color

```js
sub_5 = writesub(at(11, 4), "a^2 + b^2 = c^2", "a", "3", type(print), c(red))
```
