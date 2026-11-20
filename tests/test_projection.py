import unittest

from spatialdoor.projection import ProjectionError, project_node


def record():
    return {
        "node_id": "ixo:project:123",
        "public_label": "Project (redacted)",
        "state": "available",
        "source": {
            "owner_id": "ixo",
            "source_id": "project:123",
            "revision": "rev-7",
        },
        "secret": "must not appear in output",
        "permissions": ["admin"],
    }


class ProjectionTests(unittest.TestCase):
    def test_three_modes_same_identity(self):
        nodes = [project_node(record(), view=v)
                 for v in ("spatial", "historical", "computational")]
        self.assertEqual(1, len({n["node_id"] for n in nodes}))
        self.assertEqual(1, len({n["source"]["revision"] for n in nodes}))

    def test_sanitized_output_drops_private_properties(self):
        self.assertNotIn("secret", str(project_node(record(), view="spatial")))

    def test_untrusted_permissions_not_promoted(self):
        node = project_node(record(), view="spatial")
        self.assertEqual(node["authority"], "read-only")
        self.assertIsNone(node["owner_action"])
        self.assertNotIn("permissions", node)

    def test_input_not_mutated(self):
        source = record()
        project_node(source, view="spatial")
        self.assertEqual(source["source"]["revision"], "rev-7")

    def test_missing_revision_rejected(self):
        source = record()
        source["source"].pop("revision")
        with self.assertRaises(ProjectionError):
            project_node(source, view="spatial")

    def test_invalid_view_rejected(self):
        with self.assertRaises(ProjectionError):
            project_node(record(), view="execute")

    def test_offline_mode_preserved(self):
        source = record()
        source["state"] = "offline"
        self.assertEqual(project_node(source, view="historical")["state"], "offline")

    def test_unsanitized_label_type_rejected(self):
        source = record()
        source["public_label"] = {"raw_text": "private"}
        with self.assertRaises(ProjectionError):
            project_node(source, view="spatial")


if __name__ == "__main__":
    unittest.main()
