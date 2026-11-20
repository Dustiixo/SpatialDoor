# SpatialDoor — source-bound spatial projection

**Current repository status: contract prototype, not a native 3D desktop.**

SpatialDoor (DOOR) is the view layer for OXsukra/IXO. It should let a human
move through real projects, files, applications, history and computational
relationships in the same spatial fabric, including keyboard, pointer,
touch and controller inputs.

The underlying owner remains IXO or the external program that actually owns
the record. A beautiful node cannot grant permission, fabricate data, or
silently change an application.

## First executable contract

`spatialdoor/projection.py` creates a bounded, deterministic, sanitized
read-only representation of **one supplied source record** in three views:

- `spatial`: where the object lives and what is nearby.
- `historical`: the same object's revision and chronological context.
- `computational`: dependency and execution relationships, if supplied.

The current implementation only carries stable identity, source revision,
availability and a sanitized label. It does **not** render a world, traverse
real dependencies, open applications, synchronize timelines, manipulate the
screen, or verify source authenticity.

### Run local contract tests

```bash
python -m unittest discover -s tests -q
```

The next real acceptance test is **one native IXO project with one canonical
record appearing in three views**, surviving restart and source-offline
transitions without changing any owned state. Only after that proof should
screen strips, the PS2-style HUD, controller navigation, ECHOFOLD scene
recursion, glitch signals or the folding gesture fabric be added.

## Ownership and boundaries

SpatialDoor is distinct from IXO's runtime, ECHOFOLD.VME's cache, ORBITAL's
editor and the proposed visual mutation lab. Those can cooperate through
versioned contracts while keeping their own source/state.

No hardware acceptance, real compositor, GPU benchmark, native Windows
integration or authorized write path has been demonstrated by this repository.
