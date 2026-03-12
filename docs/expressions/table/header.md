---
title: header
sidebar_label: header
---

# header

Defines custom column headers for a data table, with each label rendered as KaTeX supporting LaTeX math notation.

**Utility:** Define custom column headers for a table

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `labels` | `string (one or more)` | Yes | Header label strings - e.g., "n", "n^2", "\\sin(n)". Each label corresponds to one table column. |

## Variants

### Basic headers matching formulas

```js
header("x", "x^2")
```

Simple headers that match the formula columns

### LaTeX-formatted headers

```js
header("n", "n^2", "\\sin(n)")
```

Headers with LaTeX math notation for display

### Descriptive headers

```js
header("Input", "Output", "Error")
```

Human-readable column labels

## Examples

### Table with custom LaTeX headers

```js
T = table(at(0, 0), header("n", "n^2", "\\sin(n)"), "n", "n^2", "sin(n)", range(1, 10))
```

### Table with descriptive headers different from formulas

```js
T = table(at(2, 5), header("Time", "Position", "Velocity"), "t", "t^2/2", "t", range(0, 10, 1))
```
