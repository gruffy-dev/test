"""Tests for externally declared MCP provider configuration."""

import unittest

from pydantic import ValidationError

from mosaic.models.capabilities.mcp_provider_configuration import (
    McpProviderConfiguration,
)


class TestMcpProviderConfiguration(unittest.TestCase):
    """Verify provider connections contain no development defaults."""

    def test_explicit_provider_configuration_is_accepted(self) -> None:
        """A fully declared provider becomes immutable runtime input."""
        configuration = McpProviderConfiguration(
            provider_name='cluster-inventory',
            transport='streamable_http',
            header_strategy='ada_request_context',
            base_url='https://inventory.example/mcp',
            allowed_tool_names=('objects_list',),
        )

        self.assertEqual(configuration.provider_name, 'cluster-inventory')
        self.assertEqual(configuration.allowed_tool_names, ('objects_list',))

    def test_omitted_provider_fields_are_rejected(self) -> None:
        """No endpoint, identity, transport, or allowlist is inferred."""
        with self.assertRaises(ValidationError):
            McpProviderConfiguration()

    def test_untrusted_tool_name_is_rejected(self) -> None:
        """The allowlist accepts concrete lower-snake-case names only."""
        with self.assertRaises(ValidationError):
            McpProviderConfiguration(
                provider_name='cluster-inventory',
                transport='streamable_http',
                header_strategy='ada_request_context',
                base_url='https://inventory.example/mcp',
                allowed_tool_names=('objects-list',),
            )


if __name__ == '__main__':
    unittest.main()
