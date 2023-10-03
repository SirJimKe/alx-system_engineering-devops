# 2-puppet_custom_http_response_header.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Custom fact to retrieve the hostname of the server
$server_hostname = $facts['hostname']

# Configure Nginx with a custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  mode    => '0644',
  content => server {
    listen 80;
    server_name _;

    location / {
        root /var/www/html;
        add_header X-Served-By '<%= @server_hostname %>';
    }
},
  notify  => Service['nginx'],
}

# Nginx service management
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}

