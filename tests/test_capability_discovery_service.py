"""Tests for bounded goal-scoped capability discovery."""

import unittest
from types import SimpleNamespace

from mosaic.components.capabilities.capability_catalogue_and_resolver import (
    CapabilityCatalogueAndResolver,
)
from mosaic.components.capabilities.capability_discovery_service import (
    CapabilityDiscoveryService,
)
from mosaic.mocks.mock_ada_capability_catalogue import (
    MockAdaCapabilityCatalogue,
)
from mosaic.models.capabilities.capability_discovery_configuration import (
    CapabilityDiscoveryConfiguration,
)
from mosaic.models.orchestration.orchestration_state import OrchestrationState


class TestCapabilityDiscoveryService(unittest.TestCase):
    """Verify skill-bounded discovery and metadata isolation."""

    def test_only_skill_declared_capabilities_are_exposed(self) -> None:
        """The wider runtime catalogue cannot enter model context."""
        resolver = self._create_resolver()

        result = resolver.discover_capability_candidates(
            required_capability_names=('openshift.router.logs.read',),
            optional_capability_names=(
                'prometheus.ingress.metrics.read',
            ),
        )

        names = [item['name'] for item in result['capabilities']]
        self.assertEqual(
            names,
            [
                'openshift.router.logs.read',
                'prometheus.ingress.metrics.read',
            ],
        )
        self.assertNotIn('openshift.ingress.status.read', names)
        self.assertNotIn('provider_name', str(result))
        self.assertNotIn('tool_name', str(result))

    def test_candidate_overflow_fails_without_truncation(self) -> None:
        """An oversized candidate set returns no partial metadata."""
        resolver = self._create_resolver(maximum_candidate_count=1)

        result = resolver.discover_capability_candidates(
            required_capability_names=(
                'openshift.ingress.status.read',
                'openshift.events.read',
            ),
            optional_capability_names=(),
        )

        self.assertEqual(result['status'], 'limit_exceeded')
        self.assertEqual(result['capabilities'], [])
        self.assertEqual(result['limit_name'], 'maximum_candidate_count')

    def test_service_adds_skill_requirements_from_trusted_state(self) -> None:
        """The model cannot omit capability names declared by loaded skills."""
        service = CapabilityDiscoveryService(
            capability_catalogue_and_resolver=self._create_resolver(),
        )
        state = OrchestrationState.start('invocation-1').model_copy(
            update={
                'skill_discovery_completed': True,
                'skill_batch_attempted': True,
                'skill_batch_loaded': True,
                'requested_skill_names': ('diagnose',),
                'loaded_skill_names': ('diagnose',),
                'required_capability_names': ('mq.queue.depth.read',),
                'optional_capability_names': ('database.runbook.search',),
            }
        )
        context = SimpleNamespace(
            state={'mosaic:orchestration': state.model_dump(mode='json')}
        )

        result = service.discover_capabilities(context)

        self.assertEqual(
            [item['name'] for item in result['capabilities']],
            ['mq.queue.depth.read', 'database.runbook.search'],
        )

    def test_service_rejects_discovery_without_a_loaded_skill(self) -> None:
        """Direct service use cannot bypass the skill gateway."""
        service = CapabilityDiscoveryService(
            capability_catalogue_and_resolver=self._create_resolver(),
        )
        state = OrchestrationState.start('invocation-1').model_copy(
            update={'skill_discovery_completed': True}
        )
        context = SimpleNamespace(
            state={'mosaic:orchestration': state.model_dump(mode='json')}
        )

        result = service.discover_capabilities(context)

        self.assertEqual(result['status'], 'skill_required')
        self.assertEqual(result['capabilities'], [])

    def _create_resolver(
        self,
        maximum_candidate_count: int = 20,
    ) -> CapabilityCatalogueAndResolver:
        """Create a resolver using the production-shaped mock catalogue."""
        return CapabilityCatalogueAndResolver(
            capabilities=MockAdaCapabilityCatalogue.create().capabilities,
            discovery_configuration=CapabilityDiscoveryConfiguration(
                maximum_candidate_count=maximum_candidate_count,
            ),
        )


if __name__ == '__main__':
    unittest.main()
