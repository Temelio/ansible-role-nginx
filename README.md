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

## Configure servers

Today, management of configuration options is smaller and incomplete, but will grow later.

Example:

    nginx_servers:

## Dependencies

None

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

