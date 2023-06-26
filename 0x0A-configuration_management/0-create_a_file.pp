# creates a file in /tmp with puppet cm

file { '/tmp/school':
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content =>'I love Puppet',
}
