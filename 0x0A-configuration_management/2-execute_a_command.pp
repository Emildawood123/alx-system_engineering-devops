# kill the process

exec { 'pkill killmenow':
  path     => '/usr/bin',
  command  => 'pkill killmenow',
  returns  => [0, 1],
  provider => shell,
}