"""Test configuration for CRM Update Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "crm-update-agent", "category": "Sales"}
