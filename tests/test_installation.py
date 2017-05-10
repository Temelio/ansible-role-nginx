"""
Role tests
"""

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_packages(host):
    """
    Test packages installation
    """

    packages = []

    if host.system_info.distribution in ('debian', 'ubuntu'):
        packages = ['nginx']

    for package in packages:
        assert host.package(package).is_installed


def test_repository_file(host):
    """
    Test about repository file poroperties
    """

    repo_files = []

    if host.system_info.distribution in ('debian', 'ubuntu'):
        repo_files = ['/etc/apt/sources.list.d/nginx.list']

    for repo_file in repo_files:
        assert host.file(repo_file).exists
        assert host.file(repo_file).is_file
        assert host.file(repo_file).user == 'root'
        assert host.file(repo_file).group == 'root'
        assert host.file(repo_file).mode == 0o644


def test_default_files_removed(host):
    """
    Test about default files deletion
    """

    default_files = []

    if host.system_info.distribution in ('debian', 'ubuntu'):
        default_files = [
            '/etc/nginx/conf.d/default.conf',
            '/etc/nginx/conf.d/example_ssl.conf',
        ]

    for default_file in default_files:
        assert host.file(default_file).exists is False


def test_service(host):
    """
    Test about service
    """

    service_name = 'nginx'

    assert host.service(service_name).is_enabled

    # Systemctl not available with Docker images
    if 'docker' != host.backend.NAME:
        assert host.service(service_name).is_running


def test_system_user(host):
    """
    Check if system user exists
    """

    if host.system_info.distribution in ('debian', 'ubuntu'):
        assert host.user('nginx').exists
        assert host.user('nginx').group == 'nginx'
        assert host.user('nginx').home == '/nonexistent'
        assert host.user('nginx').shell == '/bin/false'
