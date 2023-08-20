# set ulimit to handle high amount of requests

exec {'set_ulimit':
  provider => shell,
  command  => 'sudo sed -i "s/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4097\"/" /etc/default/nginx',
  before   => Exec['server_restart'],
}

exec {'server_restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
