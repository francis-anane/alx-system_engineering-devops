# Fix error 500 on a GET request, on an apache server

exec{'Fix_500_err':
    provider => shell,
    command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
