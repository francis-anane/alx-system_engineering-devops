# Installing flask version 2.1.0 with puppet cm
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
