import unittest
from types import SimpleNamespace

from mosaic.components.capabilities.capability_catalogue_and_resolver import CapabilityCatalogueAndResolver
from mosaic.components.capabilities.mcp_execution_gateway import MCPExecutionGateway
from mosaic.components.orchestration.ada_session_target_context_store import AdaSessionTargetContextStore
from mosaic.mocks.mock_ada_capability_catalogue import MockAdaCapabilityCatalogue
from mosaic.mocks.mock_capability_provider_invoker import MockCapabilityProviderInvoker


class TestMCPExecutionGateway(unittest.IsolatedAsyncioTestCase):
    async def test_openshift_events_are_available(self) -> None:
        result = await self._create_gateway().execute_capability(
            capability_name='openshift.events.read',
            semantic_arguments={
                'cluster_name': 'prod-east',
                'time_window_minutes': 30,
            },
            tool_context=self._context(),
        )

        self.assertEqual(result['status'], 'success')
        evidence = result['evidence']
        self.assertIsInstance(evidence, dict)
        if isinstance(evidence, dict):
            self.assertEqual(evidence['status'], 'success')
            self.assertEqual(
                evidence['source'],
                'mock-kubernetes-mcp',
            )

    async def test_database_runbook_can_be_searched_and_read(self) -> None:
        gateway = self._create_gateway()
        search_result = await gateway.execute_capability(
            capability_name='database.runbook.search',
            semantic_arguments={
                'request': 'Restore a PostgreSQL database from backup.',
            },
            tool_context=self._context(),
        )
        read_result = await gateway.execute_capability(
            capability_name='database.runbook.read',
            semantic_arguments={
                'runbook_id': 'DB-RB-0042',
                'version': '3.1.0',
            },
            tool_context=self._context(),
        )

        self.assertEqual(search_result['status'], 'success')
        self.assertEqual(read_result['status'], 'success')
        evidence = read_result['evidence']
        self.assertIsInstance(evidence, dict)
        if isinstance(evidence, dict):
            runbook = evidence['runbook']
            self.assertIsInstance(runbook, dict)
            if isinstance(runbook, dict):
                self.assertEqual(runbook['runbook_id'], 'DB-RB-0042')
                self.assertEqual(runbook['version'], '3.1.0')

    def _create_gateway(self) -> MCPExecutionGateway:
        mock_catalogue = MockAdaCapabilityCatalogue.create()
        return MCPExecutionGateway(
            capability_catalogue_and_resolver=CapabilityCatalogueAndResolver(
                capabilities=mock_catalogue.capabilities,
                providers=mock_catalogue.providers,
            ),
            provider_invoker=MockCapabilityProviderInvoker(),
            session_target_context_store=AdaSessionTargetContextStore(),
        )

    def _context(self) -> SimpleNamespace:
        return SimpleNamespace(
            invocation_id='invocation-1',
            session=SimpleNamespace(id='test-session'),
            state={
                'mosaic:session-target': {
                    'schema_version': 1,
                    'target_id': 'openshift/dev',
                }
            },
        )


if __name__ == '__main__':
    unittest.main()
