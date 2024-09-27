||No.||Property||Description||Type||Threat Context||GR Required||Jira Story
|1|CertificateIdentifier|A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.|String| |no| |
|2|CertificatePem|The contents of a .pem file, which contains an X.509 certificate.|String| |no| |
|3|CertificateWallet|The location of an imported Oracle Wallet certificate for use with SSL. An example is: filebase64("${path.root}/rds-ca-2019-root.sso")|String| |no| |
