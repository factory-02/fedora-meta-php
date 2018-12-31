Name:                           fedora-meta-php
Version:                        1.0.0
Release:                        1%{?dist}
Summary:                        META-package for install PHP

License:                        GPLv3

Requires:                       php73-php
Requires:                       php73-php-gd
Requires:                       php73-php-imap
Requires:                       php73-php-intl
Requires:                       php73-php-mbstring
Requires:                       php73-php-mysqlnd
Requires:                       php73-php-odbc
Requires:                       php73-php-opcache
Requires:                       php73-php-pdo
Requires:                       php73-php-pecl-geoip
Requires:                       php73-php-pecl-imagick
Requires:                       php73-php-pecl-memcached
Requires:                       php73-php-pecl-redis4
Requires:                       php73-php-pecl-uploadprogress
Requires:                       php73-php-xml

%description
META-package for install PHP.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%changelog
* Mon Dec 31 2018 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
