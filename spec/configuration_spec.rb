require 'serverspec'

if ENV['TRAVIS']
    set :backend, :exec
end

describe file('/etc/nginx/site-available/foobar.conf') do

    it { should exist }
    it { should be_file }

    its(:content) {
        should match /^server\s+\{[\n\s]+
                          listen\s80;[\n\s]+
                          root\s\/var\/www\/foo;[\n\s]+
                          server_name\slocalhost;[\n\s]+
                          index\sindex.html;[\n\s]+
                          location\s\/foo\s\{[\n\s]+
                              try_files\s\$uri\s=404;[\n\s]+
                              root\s\/var\/www\/foo;[\n\s]+
                          \}[\n\s]+
                          location\s\/bar\s\{[\n\s]+
                              try_files\s\$uri\s=404;[\n\s]+
                              root\s\/var\/www\/bar;[\n\s]+
                          \}[\n\s]+
                      }$/mx
    }
end
