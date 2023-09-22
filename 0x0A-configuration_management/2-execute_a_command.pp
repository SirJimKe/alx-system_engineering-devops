# kills a process named killmenow


exec { 'kill_killmenow':
  command     => '/usr/bin/pkill killmenow',
  refreshonly => true,
  onlyif      => '/usr/bin/pgrep killmenow',
  path        => '/usr/bin:/bin',
}
