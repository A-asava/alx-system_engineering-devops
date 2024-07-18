# Fix 500 error when a GET http request is sent to the apache server


exec {'replace':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
