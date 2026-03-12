---
title: media
sidebar_label: media
---

# media

Attaches an audio or video asset to an expression for synchronized media playback during animation.

**Utility:** Attach audio or video media to an expression for synchronized playback

## Arguments

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `assetName` | `string` | Yes | Name of the audio/video asset in the lesson's asset library, in quotes |

## Variants

### Inline on write expression

```js
write(at(row, col), "content", type(write), media("asset-name"))
```

Play audio while pen-tracing the expression

### Media with duration control

```js
write(at(row, col), "content", type(write), media("asset-name"), t(3))
```

Media with custom animation duration

## Examples

### Narrated trig substitution introduction

```js
write_2 = write(at(3.1, 2.2), "int sqrt(a^2-x^2) dx", type(write), media("trig-sub-intro"))
```

### Write expression with media and custom duration

```js
write_5 = write(at(12, 3), "2 hat(i) - hat(j) + 3 hat(k)", type(write), media("vector-intro"), t(5))
```
