# executes the shell pkill command to kill the process killmenow with puppet cm

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
