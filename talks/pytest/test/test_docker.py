import docker
import pytest

@pytest.fixture(scope='session')
def docker_client():
    return docker.from_env()

@pytest.fixture(scope='session')
def postgres(docker_client):
    container = docker_client.containers.run("postgres:9.6", detach=True)
    yield container
    container.stop()
    container.remove()


def test_db(postgres):
    assert 'postgres:9.6' in postgres.image.tags
