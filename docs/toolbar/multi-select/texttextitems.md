---
title: "Texttextitems.Js"
sidebar_label: "Texttextitems.Js"
---

# Texttextitems.Js

Operations available when you select **TextTextItems.js** objects.

## How to Use

```
  1. Select multiple TextTextItems.js objects (Shift + click)
  2. Right-click to open the context menu
  3. Choose an operation from the menu
```

## Available Operations

| Operation | Description |
|-----------|-------------|
| **Text Replace** | TextTextItems - Unified handler for any two text objects |
| **Text Copy** | Get the first text object (any type) |
| **Text Update** | Replace first text with second's content (target fades out) |
| **Text Swap** | Copy second's content to first's position (target stays visible) |

## Expression Details

**TextTextItems - Unified handler for any two text objects**

```
Supports combinations of: label, write-output (write/print), text-selection (select)
```

**Get the first text object (any type)**

```
_getFirstText() {
```

**Replace first text with second's content (target fades out)**

```
textreplace(first, second)
```

**Copy second's content to first's position (target stays visible)**

```
textcopy(first, second)
```

**Update first text with a string**

```
textupdate(first, "content")
```

**Swap two text objects with new strings**

```
textswap(dest, source, "destString", "sourceString")
```
