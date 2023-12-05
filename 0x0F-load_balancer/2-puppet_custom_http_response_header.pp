# Using Puppet to automate the task of creating a custom HTTP header response

#update packages
exec {'update':
  command => '/usr/bin/apt-get update',
}

# ensure nginx is installed
package {'nginx':
  ensure => 'present',
}

# add custom http header
file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  match => 'http {',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

#restart nginx
exec {'run':
  command => '/usr/sbin/service nginx restart',
}
