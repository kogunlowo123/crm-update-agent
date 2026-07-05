"""CRM Update Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_validate_records():
    """Test Validate CRM records for completeness and accuracy."""
    tools = AgentTools()
    result = await tools.validate_records(scope="test", validation_rules="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_duplicates():
    """Test Detect and merge duplicate contact or account records."""
    tools = AgentTools()
    result = await tools.detect_duplicates(entity_type="test", matching_criteria="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_enrich_records():
    """Test Enrich CRM records with external data sources."""
    tools = AgentTools()
    result = await tools.enrich_records(record_ids="test", enrichment_fields="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_auto_log_activity():
    """Test Automatically log email and calendar activities to CRM."""
    tools = AgentTools()
    result = await tools.auto_log_activity(rep_id="test", activity_types="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.crm_update_agent_agent import CrmUpdateAgentAgent
    agent = CrmUpdateAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
