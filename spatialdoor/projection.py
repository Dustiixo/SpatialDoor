"""A deterministic read-only boundary between owner records and DOOR views.

No file writes, OS interaction, network calls, agent dispatch or UI rendering.
This is a transport/identity contract for an eventual real native adapter.
"""

from __future__ import annotations

from collections.abc import Mapping


VIEWS = frozenset({"spatial", "historical", "computational"})
STATES = frozenset({"available", "stale", "offline"})


class ProjectionError(ValueError):
    """The owner record cannot safely be represented by this contract."""


def _required(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ProjectionError(f"missing or empty {field}")
    return value


def project_node(owner_record: Mapping, *, view: str) -> dict:
    """Derive a versioned node without mutating or claiming its owner authority.

    Callers must supply a pre-authorized, sanitized owner record. Merely
    returning the node does not validate its source hash or authorization.
    """
    if view not in VIEWS:
        raise ProjectionError(f"unsupported view: {view}")
    if not isinstance(owner_record, Mapping):
        raise ProjectionError("owner_record must be a mapping")
    source = owner_record.get("source")
    if not isinstance(source, Mapping):
        raise ProjectionError("source must be an object")
    node_id = _required(owner_record.get("node_id"), "node_id")
    source_owner = _required(source.get("owner_id"), "source.owner_id")
    source_id = _required(source.get("source_id"), "source.source_id")
    source_version = _required(source.get("revision"), "source.revision")
    state = owner_record.get("state")
    if state not in STATES:
        raise ProjectionError("state must be available, stale, or offline")
    label = owner_record.get("public_label")
    if not isinstance(label, str):
        raise ProjectionError("public_label must be sanitized text")
    if len(label) > 160:
        raise ProjectionError("public_label exceeds size boundary")
    return {
        "contract": "oxsukra.spatialdoor.projection.v0",
        "node_id": node_id,
        "view": view,
        "state": state,
        "label": label,
        "source": {
            "owner_id": source_owner,
            "source_id": source_id,
            "revision": source_version,
        },
        "authority": "read-only",
        "owner_action": None,
    }
