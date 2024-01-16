#replace phpp to php in the file


exec {'fix the apache':
  provider => shell,
  command  => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path     => ['/usr/local/bin/', '/bin/']
}
