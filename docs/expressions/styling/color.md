---
title: c
sidebar_label: c
---

# c

Inline modifier that sets the stroke color of a shape. Accepts CSS color names (unquoted) or hex color strings (quoted).

**Utility:** Set stroke/outline color on shapes using inline modifier

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `color` | `colorName \| "#hex"` | Yes | Color name (unquoted) or hex string (quoted) - e.g., red, blue, "#ff0000" |

## Variants

### Named color

```
c(red)
```

Set color using a standard color name

### Hex color

```
c("#ff0000")
```

Set color using a hex color code

### Inside shape expression

```
circle(G, 3, -2, 0, c(red))
```

Color applied as inline modifier to a shape

### Inside plot expression

```
plot(G, "x^2", c(blue))
```

Color applied to a plot curve

### Inside write expression

```
write(at(3, 2), "x^2 + y^2", type(write), c(blue))
```

Color applied to math text rendering

## Examples

### Red circle in Venn diagram

```
C1 = circle(G, 3, -2, 0, c(red))
```

### Blue plot curve

```
plot(G1, eq1, c(blue))
```

### Green tangent line

```
tangent(G, pl1, b, c(blue))
```

### Colored triangle with no stroke opacity

```
T = sss(G, 5, 4, 3, c(red), so(0), fo(0))
```

### Blue table with color

```
t = table(at(1, 7), "x", eq, slopeeq, range(2, 1.5, 1.1, 1.01, 1.001), c(blue))
```

### Colored text with write

```
write_only_1 = writeonly(at(11, 3), "sqrt(a^2-x^2) = sqrt(a^2-a^2sin^2(theta))", select("a^2sin^2(theta)", 1), type(write), c(blue))
```
