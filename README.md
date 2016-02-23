# nginx

[![Build Status](https://travis-ci.org/Temelio/ansible-role-nginx.svg?branch=master)](https://travis-ci.org/Temelio/ansible-role-nginx)

Install nginx package.

## Requirements

This role requires Ansible 2.0 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role contains two tests methods :
- locally using Vagrant
- automatically with Travis

### Testing dependencies
- install [Vagrant](https://www.vagrantup.com)
- install [Vagrant serverspec plugin](https://github.com/jvoorhis/vagrant-serverspec)
    $ vagrant plugin install vagrant-serverspec
- install ruby dependencies
    $ bundle install

### Running tests

#### Run playbook and test

- if Vagrant box not running
    $ vagrant up

- if Vagrant box running
    $ vagrant provision

## Role Variables

### Default role variables

    nginx_repository_cache_valid_time: 3600
    nginx_repository_key_url: "http://nginx.org/keys/nginx_signing.key"
    nginx_repository_url: "http://nginx.org/packages/{{ ansible_distribution | lower }}/"
    nginx_repository_file:
      name: 'nginx.list'
      owner: 'root'
      group: 'root'
      mode: '0644'
    nginx_service_state: 'started'
    nginx_service_enabled: True

    # Firewall configuration
    #-----------------------
    nginx_firewall_managed_with_ferm: True
    nginx_ferm_input_rules_file: '/etc/ferm/input/nginx.conf'
    nginx_ferm_files_owner: 'root'
    nginx_ferm_files_group: 'root'
    nginx_ferm_files_mode: '0400'
    nginx_ferm_main_config_file: '/etc/ferm/ferm.conf'
    nginx_ferm_service_name: 'ferm'
    nginx_ferm_input_rules:
      - 'proto tcp mod tcp dport 80 ACCEPT;'
      - 'proto tcp mod tcp dport 443 ACCEPT;'

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
    nginx_site_available_path: '/etc/nginx/site-available'
    nginx_site_enabled_path: '/etc/nginx/site-enabled'

    nginx_ssl_certificate_files:
      - path: "{{ ansible_fqdn }}"
        content: ''
        owner: 'root'
        group: 'root'
        mode: '0600'
    nginx_ssl_key_files:
      - path: "{{ ansible_fqdn }}"
        content: ''
        owner: 'root'
        group: 'root'
        mode: '0600'
    nginx_ssl_self_signed_cn: "{{ ansible_fqdn }}"

    nginx_user: 'nginx'
    nginx_worker_processes: 1
    nginx_error_log_path: '/var/log/nginx/error.log'
    nginx_error_log_level: 'warn'
    nginx_pid_path: '/run/nginx.pid'

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


## Configure servers

Today, management of configuration options is smaller and incomplete, but will grow later.

Example:

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

## Dependencies

### Mandatory dependencies

None

### Mandatory dependencies

- Temelio.ferm

## Example Playbook

    - hosts: servers
      roles:
         - { role: achaussier.nginx }

## License

MIT

## Author Information

Alexandre Chaussier (for Temelio company)
- http://temelio.com
- alexandre.chaussier [at] temelio.com

