import pytest
from pydantic import BaseModel, Field

class SearchToolArgs(BaseModel):
    query: str = Field(description="Search term")
    limit: int = Field(default=5, ge=1, le=20)

def mock_agent_output():
    # Simulates structured output from an LLM tool call
    return {"query": "django deployment", "limit": 5}

def test_agent_tool_calling_schema():
    raw_call = mock_agent_output()
    validated = SearchToolArgs(**raw_call)
    assert validated.query == "django deployment"
    assert validated.limit == 5