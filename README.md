# nginx

[![Build Status](https://travis-ci.org/Temelio/ansible-role-nginx.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-nginx)

Install nginx package.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Locally, you can run tests on Docker (default driver) or Vagrant.
Travis run tests using Docker driver only.

Currently, tests are done on:
- Debian Jessie
- Ubuntu Trusty
- Ubuntu Xenial

and use:
- Ansible 2.0.x
- Ansible 2.1.x
- Ansible 2.2.x
- Ansible 2.3.x

### Running tests

#### Using Docker driver

```
$ tox
```

#### Using Vagrant driver

```
$ MOLECULE_DRIVER=vagrant tox
```

## Role Variables

### Default role variables

```yaml
nginx_repository_cache_valid_time: 3600
nginx_repository_key_url: "http://nginx.org/keys/nginx_signing.key"
nginx_repository_url: "http://nginx.org/packages/{{ ansible_distribution | lower }}/"
nginx_repository_file:
  name: 'nginx.list'
  owner: 'root'
  group: 'root'
  mode: '0644'

nginx_packages_state: 'latest'

nginx_service_state: 'started'
nginx_service_enabled: True

nginx_add_default_server: True
nginx_default_server_options:
  - 'return 404;'

# Nginx configuration
nginx_config_files_owner: 'root'
nginx_config_files_group: 'root'
nginx_config_files_mode: '0644'
nginx_config_dir_owner: 'root'
nginx_config_dir_group: 'root'
nginx_config_dir_mode: '0750'
nginx_delete_default_config_files: True
nginx_default_config_files:
  - '/etc/nginx/conf.d/default.conf'
  - '/etc/nginx/conf.d/example_ssl.conf'
nginx_main_config_file_path: '/etc/nginx/nginx.conf'
nginx_sites_available_path: '/etc/nginx/sites-available'
nginx_sites_enabled_path: '/etc/nginx/sites-enabled'

nginx_user: 'nginx'
nginx_error_log_path: '/var/log/nginx/error.log'
nginx_error_log_level: 'warn'
nginx_pid_path: '/run/nginx.pid'

nginx_main_options:
  - "user {{ nginx_user }};"
  - 'worker_processes 1;'

nginx_events_options:
  - 'worker_connections 1024;'

nginx_http_options:
  - 'include /etc/nginx/mime.types;'
  - 'default_type application/octet-stream;'
  - 'access_log /var/log/nginx/access.log main;'
  - 'sendfile on;'
  - 'keepalive_timeout 65;'
  - 'include /etc/nginx/conf.d/*.conf;'

nginx_http_log_format_name: 'main'
nginx_http_log_format_string: '$remote_addr - $remote_user [$time_local] "$request" $status $body_bytes_sent "$http_referer" "$http_user_agent" "$http_x_forwarded_for"'

nginx_servers: []

```

## Configure servers

Today, management of configuration options is smaller and incomplete, but will grow later.

Example:
```yaml
nginx_servers:
  - name: "{{ ansible_fqdn }}"
    is_enabled: False
    listen:
      - 80
    locations:
      - target: '/foo'
        options:
          - 'try_files $uri =404'
          - 'root /var/www/foo'
      - target: '/bar'
        options:
          - 'try_files $uri =404'
          - 'root /var/www/bar'
    root: '/var/www/foo'
    server_name:
      - 'localhost'
    use_ssl: False
```

## Configure upstreams

Today, management of configuration options is smaller and incomplete, but will grow later.

Example:
```yaml
nginx_upstreams:
  - name: 'foo'
    is_enabled: False
    options:
      - 'server 127.0.0.1:8080;'
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

Alexandre Chaussier (for Temelio company)
- http://www.temelio.com
- alexandre.chaussier [at] temelio.com
