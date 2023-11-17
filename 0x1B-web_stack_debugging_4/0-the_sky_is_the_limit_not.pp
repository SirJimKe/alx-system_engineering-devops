# Set a limit for the worker processes in the Nginx configuration
exec { 'set limit to 2000':
  path      => '/bin',
  command   => "sed -i 's/15/2000/' /etc/default/nginx",
  onlyif    => "test $(grep -c 'worker_processes 2000;' /etc/default/nginx) -eq 0",
  logoutput => true,
}

# Restart Nginx if the limit is changed
exec { 'reboot nginx':
  command     => '/usr/sbin/service nginx restart',
  refreshonly => true,
  subscribe   => Exec['set limit to 2000'],
  logoutput   => true,
}
