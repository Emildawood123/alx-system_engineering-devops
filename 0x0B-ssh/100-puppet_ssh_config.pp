# Configure SSH client to
include stdlib

file_line { 'Turn off pass auth':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
  replace => true,
}

file_line { 'configure private key':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => true,
}
