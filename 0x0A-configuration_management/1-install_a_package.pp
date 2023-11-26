# Install flask (2.1.0)
package {'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
exec { 'install_werkzeug':
command => '/usr/bin/pip3 install -q --upgrade werkzeug==2.1.1',
}
