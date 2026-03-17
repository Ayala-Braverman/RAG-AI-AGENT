# UI Design Rules

This document defines rules for the user interface.

---

## Layout

The layout should follow a simple grid structure.

Main layout:

- header
- navigation sidebar
- content area

The sidebar should collapse on smaller screens.

---

## RTL Support

All Hebrew pages must use RTL direction.

Exceptions:

- code snippets
- API paths
- log outputs

Developers must test UI in both RTL and LTR modes.

---

## Color System

Primary color: blue

Usage:

- primary buttons
- active menu items
- links

Secondary color: light gray

Usage:

- backgrounds
- cards
- secondary buttons

Danger color: red

Usage:

- delete actions
- warnings

---

## Typography

Primary font:

Inter

Font sizes:

- Title: 24px
- Section title: 18px
- Body text: 14px

Text must maintain sufficient contrast.

---

## Accessibility

Accessibility requirements:

- all buttons must include aria-label
- images must include alt text
- keyboard navigation must be supported

Accessibility should follow WCAG guidelines.