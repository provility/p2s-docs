---
title: "Plot + Plot"
sidebar_label: "Plot + Plot"
---

# Plot + Plot

Operations available when you select a **plot** and a **plot** together.

## How to Use

```
  1. Click on a plot object to select it
  2. Hold Shift and click on a plot object
  3. Right-click to open the context menu
  4. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Intersect** | Handler for two-plot selection |
| **Area Between** | Find intersection points of two plots |

## Expression Details

**Handler for two-plot selection**

```
Note: Riemann traces are only applicable to single plot (areaunder).
```

**Find intersection points of two plots**

```
intersect(G, P1, P2, n)
```

**Area between two plots**

```
areabetween(G, P1, P2)
```
