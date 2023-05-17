import pytest
from app import app, chat

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'ChatGPT Web App' in response.data

def test_results(client):
    response = client.post('/', data={'question': 'Test question'})
    assert response.status_code == 200
    assert b'Question: Test question' in response.data

def test_chat():
    question = 'Test question'
    response = chat(question)
    assert isinstance(response, str)
    assert response.strip() != ''

if __name__ == '__main__':
    pytest.main()
