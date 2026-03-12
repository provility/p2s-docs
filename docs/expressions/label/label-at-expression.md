---
title: label
sidebar_label: label
---

# label

Place a text annotation at arbitrary graph coordinates or computed positions, with support for dynamic variable substitution, formatted numeric output, and LaTeX math rendering.

**Utility:** Label with dynamic content, at arbitrary positions, or as text operation target

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `graph` | `g2d` | Yes | Graph container |
| `position` | `at(x, y) \| at(expr) \| point() inline` | Yes | Any expression resolving to 2D coordinates |
| `text` | `string` | Yes | Content string. Supports :var, :\{expr\}, :\{expr:.Nf\}, ASCII math, LaTeX. |
| `buff` | `buff(col, row)` | No | Offset from anchor position |
| `rotation` | `rotation(degrees)` | No | Rotate label text |
| `renderType` | `type(write) \| type(print)` | No | Animation mode |

## Variants

### Label at absolute coordinates

```js
label(G, at(3, 4), "text")
```

Place label at specific graph coordinates

### Label with variable substitution

```js
label(G, at(P), ":x")
```

Display live variable value, updates on change

### Label with mixed text and variable

```js
label(G, at(P), "x = :x")
```

Combine static text with dynamic variable

### Label with computed expression

```js
label(G, at(A), "Area = :{w*h}")
```

Display computed value from expression

### Label with formatted decimal

```js
label(G, at(P), ":{x:.2f}")
```

Display computed value with 2 decimal places

### Label with LaTeX math

```js
label(G, at(P), "\\sqrt{x^2+y^2}")
```

Display LaTeX-rendered math expression

### Label as placeholder for textupdate

```js
L = label(G, at(P), "?")
```

Create placeholder label, update content later with textupdate

### Label as textcopy destination

```js
L = label(G, at(P), "A")
textcopy(write_select, L)
```

Label receives copied content from write selection

### Instant KaTeX label

```js
label(G, at(P), "x^2 + y^2", type(print))
```

Render label instantly without animation

### Label string variable reference

```js
label(K, point(K, 2, fun(eq, 2)), eq_s, buff(-2))
```

Use a string variable as label content

## Examples

### Label at coordinates with at()

```js
label(G, at(3, 4), "Origin")
```

### Dynamic variable display at point

```js
label(G, at(A), "x = :x")
```

### Computed area with expression template

```js
label(G, at(A), "Area = :{w*h}")
```

### Formatted decimal output

```js
label(G, at(P), ":{x:.2f}")
```

### Placeholder label updated later

```js
L = label(graph_1, at(point_1), "?", buff(0, 0.5))
textupdate(L, "sqrt(a^2-x^2)")
```

### Label as textcopy target from equation selection

```js
label_1 = label(graph_1, at(point_1), "A", buff(0.5, 0.5))
text_arrange_1 = textcopy(write_2_select_1, label_1)
```

### Label correlated with equation term via correlate

```js
label_5 = label(graph_1, at(item(triangle_1, type(edge), 3)), "x", buff(-0.2, -1.1), rotation(0))
select_9 = select(write_7, "x", 1)
correlate_1 = correlate(select_9, label_5, type(circle))
```

### Label at inline point on function curve

```js
eq_s = "1/x^2"
eq = def(x, eq_s)
label(K, point(K, 2, fun(eq, 2)), eq_s, buff(-2))
```

### Label edge placeholder then replace from write selection

```js
label_3 = label(graph_1, at(item(triangle_1, type(edge), 1)), "?", buff(0, 0.5), rotation(0))
select_1 = select(write_2, "a^2-x^2", 1)
text_replace_6 = textreplace(label_3, select_1, buff(0, -2), type(replace))
```

### Empty label for receiving copied content

```js
L2 = label(G, 4, 4, "")
textcopy(L2, L1)
```
