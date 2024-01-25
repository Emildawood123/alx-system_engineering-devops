 # Define a file resource for your target file

 Your Puppet manifest file (e.g., replace_word.pp)


file { '/etc/security/limits.conf':
  # Ensure the file exists
  ensure => file,
  content => replace('5', '4096', file('/etc/security/limits.conf')),
}


file { '/etc/security/limits.conf':
  # Ensure the file exists
  ensure => file,
  content => replace('4', '4096', file('/etc/security/limits.conf')),
}
