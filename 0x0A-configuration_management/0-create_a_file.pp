#creates a file in /tmp with specific permissions, owner and content

file { '/tmp/school':
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',

}
