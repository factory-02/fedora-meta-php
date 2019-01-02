Name:                           meta-php
Version:                        1.0.0
Release:                        1%{?dist}
Summary:                        META-package for install PHP

License:                        GPLv3

Requires:                       remi-release-29
Requires:                       php
Requires:                       php-gd
Requires:                       php-imap
Requires:                       php-intl
Requires:                       php-mbstring
Requires:                       php-mysqlnd
Requires:                       php-odbc
Requires:                       php-opcache
Requires:                       php-pdo
Requires:                       php-pecl-geoip
Requires:                       php-pecl-imagick
Requires:                       php-pecl-memcached
Requires:                       php-pecl-redis4
Requires:                       php-pecl-uploadprogress
Requires:                       php-xml

%description
META-package for install PHP.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%changelog
* Wed Jan 02 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
