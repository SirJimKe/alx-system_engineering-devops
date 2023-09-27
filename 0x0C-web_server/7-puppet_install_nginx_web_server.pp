# Configure new ubuntu server

# Define the nginx class
class nginx {

  # Install Nginx package
  package { 'nginx':
    ensure => 'installed',
  }

  # Create a simple HTML file with "Hello World!"
  file { '/var/www/html/index.html':
    content => 'Hello World!',
    ensure  => 'file',
  }

  # Configure Nginx site
  file { '/etc/nginx/sites-available/default':
    ensure  => 'file',
    content =>
    "server {
        listen 80 default_server;
        server_name _;

        location / {
            root /var/www/html;
        }

        location /redirect_me {
            return 301 https://youtube.com;
        }

        error_page 404 /404.html;
    }",
    notify  => Service['nginx'],
  }

  # Enable the site
  exec { 'enable-default-site':
    command => '/usr/sbin/nginxensite default',
    require => File['/etc/nginx/sites-available/default'],
    notify  => Service['nginx'],
    onlyif  => '/usr/sbin/nginx -t',
  }

  # Create a custom 404 page
  file { '/var/www/html/404.html':
    content => "Ceci n'est pas une page",
    ensure  => 'file',
  }

  # restart nginx
  exec { 'restart service':
    command => 'service nginx restart',
    path    => '/usr/bin:/usr/sbin:/bin',
  }

  # Ensure Nginx service is running and restarted when the configuration changes
  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
  }
}

# Include the nginx class
include nginx
