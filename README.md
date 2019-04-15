# nginx

[![Build Status](https://img.shields.io/travis/Temelio/ansible-role-nginx/master.svg?label=travis_master)](https://travis-ci.org/Temelio/ansible-role-nginx)
[![Build Status](https://img.shields.io/travis/Temelio/ansible-role-nginx/develop.svg?label=travis_develop)](https://travis-ci.org/Temelio/ansible-role-nginx)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Updates](https://pyup.io/repos/github/Temelio/ansible-role-nginx/shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-nginx/)
[![Python 3](https://pyup.io/repos/github/Temelio/ansible-role-nginx/python-3-shield.svg)](https://pyup.io/repos/github/Temelio/ansible-role-nginx/)
[![Ansible Role](https://img.shields.io/ansible/role/8026.svg)](https://galaxy.ansible.com/Temelio/nginx/)
[![GitHub tag](https://img.shields.io/github/tag/temelio/ansible-role-nginx.svg)](https://github.com/Temelio/ansible-role-nginx/tags)

Install anc configure Nginx package.

## Requirements

This role requires Ansible 2.4 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- Debian Stretch
- Ubuntu Trusty
- Ubuntu Xenial
- Ubuntu Bionic

and use:
- Ansible 2.4.x
- Ansible 2.5.x
- Ansible 2.6.x
- Ansible 2.7.x

### Running tests

#### Using Docker driver

```
$ tox
```

## Role Variables

### Default role variables

```yaml
# General
#------------------------------------------------------------------------------

# Packages and repositories management
nginx_packages: "{{ _nginx_packages }}"
nginx_repository_cache_valid_time: "{{ _nginx_repository_cache_valid_time }}"
nginx_repositories_keys: "{{ _nginx_repositories_keys }}"
nginx_repositories: "{{ _nginx_repositories }}"

# Services management
nginx_service_name: "{{ _nginx_service_name }}"
nginx_service_state: 'started'
nginx_service_enabled: True

# Nginx configuration properties
nginx_config_permissions:
  files:
    owner: 'root'
    group: 'root'
    mode: '0644'
  folders:
    owner: 'root'
    group: 'root'
    mode: '0750'

nginx_config_paths:
  files:
    main: '/etc/nginx/nginx.conf'
    default:
      - '/etc/nginx/conf.d/default.conf'
      - '/etc/nginx/conf.d/example_ssl.conf'
  folders:
    sites_available: '/etc/nginx/sites-available'
    sites_enabled: '/etc/nginx/sites-enabled'


# Servers configuration management
#------------------------------------------------------------------------------

# Remove default servers configuration files
nginx_delete_default_config_files: True

# General
nginx_user: 'nginx'

# Nginx main configuration
nginx_conf:
  root:
    options: |
      user {{ nginx_user }};
      worker_processes 1;
      error_log /var/log/nginx/error.log info;
      pid /run/nginx.pid;
  events:
    options: |
      worker_connections 1024;
  http:
    default_server:
      enabled: True
      content: |
        return 404;
    options: |
      log_format main '$remote_addr - $remote_user [$time_local] "$request"
        $status $body_bytes_sent "$http_referer" "$http_user_agent"
        "$http_x_forwarded_for"';
      include /etc/nginx/mime.types;
      default_type application/octet-stream;
      access_log /var/log/nginx/access.log main;
      sendfile on;
      keepalive_timeout 65;
      include /etc/nginx/conf.d/*.conf;

nginx_servers: []
nginx_upstreams: []
```

## Configure servers

Today, management of configuration options is smaller and incomplete, but will grow later.

Example:
```yaml
nginx_servers:
  - name: "{{ ansible_fqdn }}"
    is_enabled: False
    options: |
      listen: 80;
      root /var/www/foo;
      server_name localhost;
    locations:
      - target: '/foo'
        options: |
          try_files $uri =404;
          root /var/www/foo;
      - target: '/bar'
        options: |
          try_files $uri =404;
          root /var/www/bar;
```

## Configure upstreams

Today, management of configuration options is smaller and incomplete, but will grow later.

Example:
```yaml
nginx_upstreams:
  - name: 'foo'
    is_enabled: False
    options: |
      server 127.0.0.1:8080;
```

## Configure maps


Example:
```yaml
nginx_maps:
  - name: 'foo'
    is_enabled: False
    target: '$uri $new_uri'
    options: |
      /foo /bar;
```

## Dependencies

None

## Example Playbook

```yaml
- hosts: servers
  roles:
    - { role: Temelio.nginx }
```

## License

MIT

## Author Information

A Chaussier, L Machetel (for Temelio company)
- http://www.temelio.com
