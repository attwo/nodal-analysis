import numpy as np
import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def generate_data_for_tests():
    return {
                "vlp": {
                    "q_liq": [0, 30, 60, 90, 120, 150],
                    "p_wf": [200, 190, 180, 175, 185, 200]
                },
                "ipr": {
                    "q_liq": [0, 30, 60, 90, 120, 150],
                    "p_wf": [200, 180, 160, 140, 120, 100]
                }
            }


def test_calc_model_success(api_client: TestClient, generate_data_for_tests):
    resp = api_client.post('/nodal/calc', json=generate_data_for_tests)
    assert resp.status_code == 200
    content = resp.json()
    assert type(content) is list
    assert len(content) == 1
    item = content[0]
    assert item
    assert item['p_wf'] is not None
    assert item['q_liq'] is not None
