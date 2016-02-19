require 'serverspec'

if ENV['TRAVIS']
    set :backend, :exec
end

describe 'nginx Ansible role' do

    if ['debian', 'ubuntu'].include?(os[:family])
        describe 'Specific Debian and Ubuntu family checks' do

            it 'install role packages' do
                packages = Array[ 'nginx' ]

                packages.each do |pkg_name|
                    expect(package(pkg_name)).to be_installed
                end
            end

            describe file('/etc/apt/sources.list.d/nginx.list') do
                it { should exist }
                it { should be_file }
                it { should be_owned_by 'root' }
                it { should be_grouped_into 'root' }
                it { should be_mode 644 }
            end

            describe service('nginx') do
              it { should be_enabled }
              it { should be_running }
            end

            DEFAULT_FILES = Array[
                '/etc/nginx/conf.d/default.conf',
                '/etc/nginx/conf.d/example_ssl.conf'
            ]
            DEFAULT_FILES.each do |current_file|
                describe file(current_file) do
                    it { should_not exist }
                end
            end
        end
    end
end

describe iptables() do
    it { should have_rule '-A INPUT -p tcp -m tcp --dport 80 -j ACCEPT' }
    it { should have_rule '-A INPUT -p tcp -m tcp --dport 443 -j ACCEPT' }
end
