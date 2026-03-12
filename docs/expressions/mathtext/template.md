---
title: template
sidebar_label: template
---

# template

Render text with dynamic variable placeholders that automatically update when referenced values change. Supports :varName substitution, :\{expr\} inline expression evaluation, and :.Nf decimal formatting.

**Utility:** Render dynamic text with variable placeholders and expression evaluation

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `position` | `at(row, col)` | Yes | Position using logical row, col coordinates |
| `templateString` | `string` | Yes | Text with placeholders - :var, :\{expr\}, :var:.Nf, :\{expr\}:.Nf |
| `color` | `c(colorName)` | No | Text color - e.g., c(blue), c(red) |
| `fontSize` | `f(size)` | No | Font size in pixels - e.g., f(24) |
| `notes` | `notes("text")` | No | Add notes/comments to the expression |

## Variants

### Simple variable

```js
template(at(row, col), "Value of a is :a")
```

Display variable value inline

### Expression evaluation

```js
template(at(row, col), "Sum = :{a+b}")
```

Compute and display expression result

### Formatted decimal

```js
template(at(row, col), "Area = :{pi*r^2}:.2f")
```

Expression with 2 decimal places

### Multiple placeholders

```js
template(at(row, col), "Point (:x, :y)")
```

Multiple variables in one template

### With styling

```js
template(at(row, col), "Result: :{x^2}:.1f", c(blue))
```

Colored template text

## Examples

### Display variable value

```js
a = 10
tpl_1 = template(at(2, 10), "Hello a is :a")
```

### Show computed sum with formatting

```js
a = 10
b = 5
tpl_2 = template(at(3, 10), "Sum = :{a+b}:.2f")
```

### Display circle area with pi

```js
r = 10
tpl_3 = template(at(4, 10), "Area = :{pi*r^2}:.1f")
```

### Show coordinates of a point

```js
x = 3
y = 4
tpl_4 = template(at(5, 2), "Point P = (:x, :y)", c(blue))
```

### Display ratio with precision

```js
num = 22
den = 7
tpl_5 = template(at(6, 2), "Ratio = :{num/den}:.4f")
```

### Dynamic measurement label

```js
length = 15
width = 8
tpl_6 = template(at(7, 3), "Perimeter = :{2*(length+width)} units")
```
