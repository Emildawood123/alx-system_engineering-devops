# change 4096 for 4 and 5 (soft and hard)

exec { 'hard':
    provider => 'shell',
    command  => 'sed -i "s/5/4096/g" /etc/security/limits.conf',
}

exec { 'soft':
    provider => 'shell',
    command  => 'sed -i "s/4/4096/g" /etc/security/limits.conf',
}
