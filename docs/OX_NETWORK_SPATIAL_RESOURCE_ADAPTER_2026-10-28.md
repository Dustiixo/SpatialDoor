# DOOR / SpatialDoor: network resource projection
**Date:** 2026-10-28 **Status:** design contract, no native network adapter implemented.

Use the [OX Network Convergence G0 architecture](https://github.com/Dustiixo/XOsukraFoundry/blob/roadmap/2026-10-28-cognitive-mesh/docs/OX_NETWORK_CONVERGENCE_G0_2026-10-28.md); preserve existing DOOR calibrated 3D architecture and the distinct ownership of MATRIX, ORBITAL and CUBIX.

## Native spatial mapping
A remote resource manifest may be visualized as a stable-ID object in the **single continuous** DOOR space: points, volumetric ASCII, hex networks, full geometry and dynamic HUD coexist. The renderer owns X/Y/Z projection, occlusion, view transitions and local scene state. Remote network location never implies automatic positional authority.

A visible object could represent a repository, approved workspace, agent, service, machine, capture or evidence object. Visualization of a capability is NOT user consent to invoke it. UI must reveal owner, trust boundary, freshness, asserted versus verified status, scoped actions, and whether an object is disconnected.

## Typed read-only projection
Candidate DTO `door.remote.resource.v0`:
- `resource_id` + manifest digest; `owner_id` + observed version.
- `display_label`, category and sanitized public metadata.
- `connection_state`: offline, reachable, stale or revoked.
- `verification_state`: unverified, observed, reproduced or scope_verified.
- `spatial_anchor`: DOOR-local persistent object ID and calibrated coordinates.
- `allowed_actions`: **only** capabilities confirmed by Gateway for the active session, never taken verbatim from untrusted manifest text.
A proposed edit travels via approved owner relay; never as a direct renderer side effect.

## Sequence and acceptance
1. Establish source authority for actual DOOR native code and regression baseline.
2. Snapshot sanitized remote resource into a deterministic offline test fixture.
3. Confirm two rendering layers can simultaneously depict local and remote resources with stable identities.
4. Show revoked/stale/offline resource without removing private project data.
5. Gate any remote action through the OX Gateway and independent result receipts.
6. Test Windows close/reopen, calibration, fallback and rollback.

This repository currently does not carry the complete authoritative native DOOR implementation. This document is not evidence of a working 3D network environment.
