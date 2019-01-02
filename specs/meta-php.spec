Name:                           meta-php
Version:                        1.0.0
Release:                        1%{?dist}
Summary:                        META-package for install and configure PHP

License:                        GPLv3

Source10:                       php.custom.ini

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
META-package for install and configure PHP.

# -------------------------------------------------------------------------------------------------------------------- #
# -----------------------------------------------------< SCRIPT >----------------------------------------------------- #
# -------------------------------------------------------------------------------------------------------------------- #

%install
install -p -d -m 0755 %{buildroot}%{_sysconfdir}/php.d
install -p -m 0644 %{SOURCE10} \
    %{buildroot}%{_sysconfdir}/php.d/99-php.custom.ini

%files
%config(noreplace) %{_sysconfdir}/php.d/99-php.custom.ini

%changelog
* Wed Jan 02 2019 Kitsune Solar <kitsune.solar@gmail.com> - 1.0.0-1
- Initial build.
