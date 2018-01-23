# fixes Apache 500 error by fixing typo in wordpress
exec { 'fix typo':
  command => "sed -i '137s/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/bin/:/bin/',
}
