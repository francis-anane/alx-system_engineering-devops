# set ulimit
exec {'set_ulimit':
  provider => shell,
  command  => 'sudo sed -i "s/holberton/#holberton/g" /etc/security/limits.conf'
}
