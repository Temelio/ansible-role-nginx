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
        end
    end
end

