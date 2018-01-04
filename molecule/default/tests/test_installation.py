"""
Role tests
"""

import os
import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name,distributions', [
    ('nginx', ['debian', 'ubuntu']),
])
def test_packages(host, name, distributions):
    """
    Test packages installation
    """

    if host.system_info.distribution in distributions:
        assert host.package(name).is_installed
    else:
        pytest.skip('Test not work with this distribution')


@pytest.mark.parametrize('file_path,distributions', [
    ('/etc/apt/sources.list.d/nginx_org_packages_debian.list', ['debian']),
    ('/etc/apt/sources.list.d/nginx_org_packages_ubuntu.list', ['ubuntu']),
])
def test_repository_file(host, file_path, distributions):
    """
    Test about repository file poroperties
    """

    if host.system_info.distribution in distributions:
        repo_file = host.file(file_path)
        assert repo_file.exists
        assert repo_file.is_file
        assert repo_file.user == 'root'
        assert repo_file.group == 'root'
        assert repo_file.mode == 0o644
    else:
        pytest.skip('Test not work with this distribution')


@pytest.mark.parametrize('file_path,distributions', [
    ('/etc/nginx/conf.d/default.conf', ['debian', 'ubuntu']),
    ('/etc/nginx/conf.d/example_ssl.conf', ['debian', 'ubuntu']),
])
def test_default_files_removed(host, file_path, distributions):
    """
    Test default files are removed
    """

    if host.system_info.distribution in distributions:
        assert host.file(file_path).exists is False
    else:
        pytest.skip('Test not work with this distribution')


@pytest.mark.parametrize('name,distributions', [
    ('nginx', ['debian', 'ubuntu']),
])
def test_service(host, name, distributions):
    """
    Test about service
    """

    if host.system_info.distribution in distributions:
        nginx_service = host.service(name)
        assert nginx_service.is_enabled

        # Systemctl not available with Docker images
        if 'docker' != host.backend.NAME:
            assert nginx_service.is_running
    else:
        pytest.skip('Test not work with this distribution')


@pytest.mark.parametrize('name,group,home,shell,distributions', [
    ('nginx', 'nginx', '/nonexistent', '/bin/false', ['debian', 'ubuntu']),
])
def test_system_user(host, name, group, home, shell, distributions):
    """
    Check if system user exists
    """

    if host.system_info.distribution in distributions:
        nginx_user = host.user(name)
        assert nginx_user.exists
        assert nginx_user.group == group
        assert nginx_user.home == home
        assert nginx_user.shell == shell
    else:
        pytest.skip('Test not work with this distribution')
