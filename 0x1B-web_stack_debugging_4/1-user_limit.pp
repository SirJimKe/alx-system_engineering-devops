# Increase hard and soft file limit for Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton\\shard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin',
  unless  => 'grep "^holberton\\shard\\s*50000" /etc/security/limits.conf',
}

exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/^holberton\\ssoft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin:/bin',
  unless  => 'grep "^holberton\\ssoft\\s*50000" /etc/security/limits.conf',
}
