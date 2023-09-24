# Client configuration file

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  match   => '^#?PasswordAuthentication',
  require => Package['openssh-server'],
}

file_line { 'Declare identity file':
  path    => '~/.ssh/config',
  line    => 'IdentityFile ~/.ssh/school',
  match   => '^#?IdentityFile',
  require => File['~/.ssh/config'],
}
