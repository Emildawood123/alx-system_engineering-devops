 # Define a file resource for your target file

 Your Puppet manifest file (e.g., replace_word.pp)


file { '/etc/security/limits.conf':
  # Ensure the file exists
  ensure => file,
  content => replace('4096', '5', file('/etc/security/limits.conf')),
}


file { '/etc/security/limits.conf':
  # Ensure the file exists
  ensure => file,
  content => replace('4096', '4', file('/etc/security/limits.conf')),
}
