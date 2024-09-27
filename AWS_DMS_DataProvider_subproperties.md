||No.||Subprops of AWS_DMS_DataProvider MicrosoftSqlServerSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|Fully qualified domain name of the endpoint. For an Amazon RDS SQL Server instance, this is the output of DescribeDBInstances, in the Endpoint.Address field.|String| | | |
|3|Port|Endpoint TCP port.|Integer| | | |
|4|DatabaseName|Database name for the endpoint.|String| | | |
|5|CertificateArn|Property description not available.|String| | | |
||No.||Subprops of AWS_DMS_DataProvider MySqlSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|The host name of the endpoint database. |String| | | |
|3|Port|Endpoint TCP port.|Integer| | | |
|4|CertificateArn|Property description not available.|String| | | |
||No.||Subprops of AWS_DMS_DataProvider OracleSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SecretsManagerOracleAsmAccessRoleArn|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the SecretsManagerOracleAsmSecret. This SecretsManagerOracleAsmSecret has the secret value that allows access to the Oracle ASM of the endpoint.|String| | | |
|2|SecretsManagerOracleAsmSecretId|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN, partial ARN, or friendly name of the SecretsManagerOracleAsmSecret  that contains the Oracle ASM connection details for the Oracle endpoint.|String| | | |
|3|SslMode|Property description not available.|String| | | |
|4|SecretsManagerSecurityDbEncryptionSecretId|Property description not available.|String| | | |
|5|ServerName|Fully qualified domain name of the endpoint.|String| | | |
|6|Port|Endpoint TCP port.|Integer| | | |
|7|DatabaseName|Database name for the endpoint.|String| | | |
|8|AsmServer|For an Oracle source endpoint, your ASM server address. You can set this value from the asm_server value. You set asm_server as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see Configuration for change data capture (CDC) on an Oracle source database.|String| | | |
|9|CertificateArn|Property description not available.|String| | | |
|10|SecretsManagerSecurityDbEncryptionAccessRoleArn|Property description not available.|String| | | |
||No.||Subprops of AWS_DMS_DataProvider PostgreSqlSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|The host name of the endpoint database. |String| | | |
|3|Port|Endpoint TCP port. The default is 5432.|Integer| | | |
|4|DatabaseName|Database name for the endpoint.|String| | | |
|5|CertificateArn|Property description not available.|String| | | |
||No.||Subprops of AWS_DMS_DataProvider Settings||Description||Type||Threat Context||GR Required||Jira Story
|1|OracleSettings|Property description not available.|[OracleSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-oraclesettings.html]| |Sub-property may require GR| |
|2|MicrosoftSqlServerSettings|Property description not available.|[MicrosoftSqlServerSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-microsoftsqlserversettings.html]| |Sub-property may require GR| |
|3|MySqlSettings|Property description not available.|[MySqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-mysqlsettings.html]| |Sub-property may require GR| |
|4|PostgreSqlSettings|Property description not available.|[PostgreSqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-postgresqlsettings.html]| |Sub-property may require GR| |
||No.||Subprops of AWS_DMS_DataProvider MicrosoftSqlServerSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|Fully qualified domain name of the endpoint. For an Amazon RDS SQL Server instance, this is the output of DescribeDBInstances, in the Endpoint.Address field.|String| | | |
|3|Port|Endpoint TCP port.|Integer| | | |
|4|DatabaseName|Database name for the endpoint.|String| | | |
|5|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider MySqlSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|The host name of the endpoint database. |String| | | |
|3|Port|Endpoint TCP port.|Integer| | | |
|4|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider OracleSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SecretsManagerOracleAsmAccessRoleArn|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the SecretsManagerOracleAsmSecret. This SecretsManagerOracleAsmSecret has the secret value that allows access to the Oracle ASM of the endpoint.|String| |Yes| |
|2|SecretsManagerOracleAsmSecretId|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN, partial ARN, or friendly name of the SecretsManagerOracleAsmSecret  that contains the Oracle ASM connection details for the Oracle endpoint.|String| | | |
|3|SslMode|Property description not available.|String| | | |
|4|SecretsManagerSecurityDbEncryptionSecretId|Property description not available.|String| | | |
|5|ServerName|Fully qualified domain name of the endpoint.|String| | | |
|6|Port|Endpoint TCP port.|Integer| | | |
|7|DatabaseName|Database name for the endpoint.|String| | | |
|8|AsmServer|For an Oracle source endpoint, your ASM server address. You can set this value from the asm_server value. You set asm_server as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see Configuration for change data capture (CDC) on an Oracle source database.|String| | | |
|9|CertificateArn|Property description not available.|String| |Yes| |
|10|SecretsManagerSecurityDbEncryptionAccessRoleArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider PostgreSqlSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|The host name of the endpoint database. |String| | | |
|3|Port|Endpoint TCP port. The default is 5432.|Integer| | | |
|4|DatabaseName|Database name for the endpoint.|String| | | |
|5|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider Settings||Description||Type||Threat Context||GR Required||Jira Story
|1|OracleSettings|Property description not available.|[OracleSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-oraclesettings.html]| |Sub-property may require GR| |
|2|MicrosoftSqlServerSettings|Property description not available.|[MicrosoftSqlServerSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-microsoftsqlserversettings.html]| |Sub-property may require GR| |
|3|MySqlSettings|Property description not available.|[MySqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-mysqlsettings.html]| |Sub-property may require GR| |
|4|PostgreSqlSettings|Property description not available.|[PostgreSqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-postgresqlsettings.html]| |Sub-property may require GR| |
||No.||Subprops of AWS_DMS_DataProvider MicrosoftSqlServerSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|Fully qualified domain name of the endpoint. For an Amazon RDS SQL Server instance, this is the output of DescribeDBInstances, in the Endpoint.Address field.|String| | | |
|3|Port|Endpoint TCP port.|Integer| | | |
|4|DatabaseName|Database name for the endpoint.|String| | | |
|5|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider MySqlSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|The host name of the endpoint database. |String| | | |
|3|Port|Endpoint TCP port.|Integer| | | |
|4|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider OracleSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SecretsManagerOracleAsmAccessRoleArn|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the SecretsManagerOracleAsmSecret. This SecretsManagerOracleAsmSecret has the secret value that allows access to the Oracle ASM of the endpoint.|String| |Yes| |
|2|SecretsManagerOracleAsmSecretId|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN, partial ARN, or friendly name of the SecretsManagerOracleAsmSecret  that contains the Oracle ASM connection details for the Oracle endpoint.|String| |Yes| |
|3|SslMode|Property description not available.|String| | | |
|4|SecretsManagerSecurityDbEncryptionSecretId|Property description not available.|String| |Yes| |
|5|ServerName|Fully qualified domain name of the endpoint.|String| | | |
|6|Port|Endpoint TCP port.|Integer| | | |
|7|DatabaseName|Database name for the endpoint.|String| | | |
|8|AsmServer|For an Oracle source endpoint, your ASM server address. You can set this value from the asm_server value. You set asm_server as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see Configuration for change data capture (CDC) on an Oracle source database.|String| | | |
|9|CertificateArn|Property description not available.|String| |Yes| |
|10|SecretsManagerSecurityDbEncryptionAccessRoleArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider PostgreSqlSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|The host name of the endpoint database. |String| | | |
|3|Port|Endpoint TCP port. The default is 5432.|Integer| | | |
|4|DatabaseName|Database name for the endpoint.|String| | | |
|5|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider Settings||Description||Type||Threat Context||GR Required||Jira Story
|1|OracleSettings|Property description not available.|[OracleSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-oraclesettings.html]| |Sub-property may require GR| |
|2|MicrosoftSqlServerSettings|Property description not available.|[MicrosoftSqlServerSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-microsoftsqlserversettings.html]| |Sub-property may require GR| |
|3|MySqlSettings|Property description not available.|[MySqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-mysqlsettings.html]| |Sub-property may require GR| |
|4|PostgreSqlSettings|Property description not available.|[PostgreSqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-postgresqlsettings.html]| |Sub-property may require GR| |
||No.||Subprops of AWS_DMS_DataProvider MicrosoftSqlServerSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|Fully qualified domain name of the endpoint. For an Amazon RDS SQL Server instance, this is the output of DescribeDBInstances, in the Endpoint.Address field.|String| | | |
|3|Port|Endpoint TCP port.|Integer| | | |
|4|DatabaseName|Database name for the endpoint.|String| | | |
|5|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider MySqlSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|The host name of the endpoint database. |String| | | |
|3|Port|Endpoint TCP port.|Integer| | | |
|4|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider OracleSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SecretsManagerOracleAsmAccessRoleArn|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the SecretsManagerOracleAsmSecret. This SecretsManagerOracleAsmSecret has the secret value that allows access to the Oracle ASM of the endpoint.|String| |Yes| |
|2|SecretsManagerOracleAsmSecretId|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN, partial ARN, or friendly name of the SecretsManagerOracleAsmSecret  that contains the Oracle ASM connection details for the Oracle endpoint.|String| |Yes| |
|3|SslMode|Property description not available.|String| | | |
|4|SecretsManagerSecurityDbEncryptionSecretId|Property description not available.|String| |Yes| |
|5|ServerName|Fully qualified domain name of the endpoint.|String| | | |
|6|Port|Endpoint TCP port.|Integer| | | |
|7|DatabaseName|Database name for the endpoint.|String| | | |
|8|AsmServer|For an Oracle source endpoint, your ASM server address. You can set this value from the asm_server value. You set asm_server as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see Configuration for change data capture (CDC) on an Oracle source database.|String| | | |
|9|CertificateArn|Property description not available.|String| |Yes| |
|10|SecretsManagerSecurityDbEncryptionAccessRoleArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider PostgreSqlSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|The host name of the endpoint database. |String| | | |
|3|Port|Endpoint TCP port. The default is 5432.|Integer| | | |
|4|DatabaseName|Database name for the endpoint.|String| | | |
|5|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider Settings||Description||Type||Threat Context||GR Required||Jira Story
|1|OracleSettings|Property description not available.|[OracleSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-oraclesettings.html]| |Sub-property may require GR| |
|2|MicrosoftSqlServerSettings|Property description not available.|[MicrosoftSqlServerSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-microsoftsqlserversettings.html]| |Sub-property may require GR| |
|3|MySqlSettings|Property description not available.|[MySqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-mysqlsettings.html]| |Sub-property may require GR| |
|4|PostgreSqlSettings|Property description not available.|[PostgreSqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-postgresqlsettings.html]| |Sub-property may require GR| |
||No.||Subprops of AWS_DMS_DataProvider MicrosoftSqlServerSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|Fully qualified domain name of the endpoint. For an Amazon RDS SQL Server instance, this is the output of DescribeDBInstances, in the Endpoint.Address field.|String| | | |
|3|Port|Endpoint TCP port.|Integer| | | |
|4|DatabaseName|Database name for the endpoint.|String| | | |
|5|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider MySqlSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|The host name of the endpoint database. |String| | | |
|3|Port|Endpoint TCP port.|Integer| | | |
|4|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider OracleSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SecretsManagerOracleAsmAccessRoleArn|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the SecretsManagerOracleAsmSecret. This SecretsManagerOracleAsmSecret has the secret value that allows access to the Oracle ASM of the endpoint.|String| |Yes| |
|2|SecretsManagerOracleAsmSecretId|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN, partial ARN, or friendly name of the SecretsManagerOracleAsmSecret  that contains the Oracle ASM connection details for the Oracle endpoint.|String| |Yes| |
|3|SslMode|Property description not available.|String| | | |
|4|SecretsManagerSecurityDbEncryptionSecretId|Property description not available.|String| |Yes| |
|5|ServerName|Fully qualified domain name of the endpoint.|String| | | |
|6|Port|Endpoint TCP port.|Integer| | | |
|7|DatabaseName|Database name for the endpoint.|String| | | |
|8|AsmServer|For an Oracle source endpoint, your ASM server address. You can set this value from the asm_server value. You set asm_server as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see Configuration for change data capture (CDC) on an Oracle source database.|String| | | |
|9|CertificateArn|Property description not available.|String| |Yes| |
|10|SecretsManagerSecurityDbEncryptionAccessRoleArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider PostgreSqlSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|The host name of the endpoint database. |String| | | |
|3|Port|Endpoint TCP port. The default is 5432.|Integer| | | |
|4|DatabaseName|Database name for the endpoint.|String| | | |
|5|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider Settings||Description||Type||Threat Context||GR Required||Jira Story
|1|OracleSettings|Property description not available.|[OracleSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-oraclesettings.html]| |Sub-property may require GR| |
|2|MicrosoftSqlServerSettings|Property description not available.|[MicrosoftSqlServerSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-microsoftsqlserversettings.html]| |Sub-property may require GR| |
|3|MySqlSettings|Property description not available.|[MySqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-mysqlsettings.html]| |Sub-property may require GR| |
|4|PostgreSqlSettings|Property description not available.|[PostgreSqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-postgresqlsettings.html]| |Sub-property may require GR| |
||No.||Subprops of AWS_DMS_DataProvider MicrosoftSqlServerSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|Fully qualified domain name of the endpoint. For an Amazon RDS SQL Server instance, this is the output of DescribeDBInstances, in the Endpoint.Address field.|String| | | |
|3|Port|Endpoint TCP port.|Integer| | | |
|4|DatabaseName|Database name for the endpoint.|String| | | |
|5|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider MySqlSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|The host name of the endpoint database. |String| | | |
|3|Port|Endpoint TCP port.|Integer| | | |
|4|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider OracleSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SecretsManagerOracleAsmAccessRoleArn|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the SecretsManagerOracleAsmSecret. This SecretsManagerOracleAsmSecret has the secret value that allows access to the Oracle ASM of the endpoint.|String| |Yes| |
|2|SecretsManagerOracleAsmSecretId|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN, partial ARN, or friendly name of the SecretsManagerOracleAsmSecret  that contains the Oracle ASM connection details for the Oracle endpoint.|String| |Yes| |
|3|SslMode|Property description not available.|String| | | |
|4|SecretsManagerSecurityDbEncryptionSecretId|Property description not available.|String| |Yes| |
|5|ServerName|Fully qualified domain name of the endpoint.|String| | | |
|6|Port|Endpoint TCP port.|Integer| | | |
|7|DatabaseName|Database name for the endpoint.|String| | | |
|8|AsmServer|For an Oracle source endpoint, your ASM server address. You can set this value from the asm_server value. You set asm_server as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see Configuration for change data capture (CDC) on an Oracle source database.|String| | | |
|9|CertificateArn|Property description not available.|String| |Yes| |
|10|SecretsManagerSecurityDbEncryptionAccessRoleArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider PostgreSqlSettings||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode|Property description not available.|String| | | |
|2|ServerName|The host name of the endpoint database. |String| | | |
|3|Port|Endpoint TCP port. The default is 5432.|Integer| | | |
|4|DatabaseName|Database name for the endpoint.|String| | | |
|5|CertificateArn|Property description not available.|String| |Yes| |
||No.||Subprops of AWS_DMS_DataProvider Settings||Description||Type||Threat Context||GR Required||Jira Story
|1|OracleSettings|Property description not available.|[OracleSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-oraclesettings.html]| |Sub-property may require GR| |
|2|MicrosoftSqlServerSettings|Property description not available.|[MicrosoftSqlServerSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-microsoftsqlserversettings.html]| |Sub-property may require GR| |
|3|MySqlSettings|Property description not available.|[MySqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-mysqlsettings.html]| |Sub-property may require GR| |
|4|PostgreSqlSettings|Property description not available.|[PostgreSqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-postgresqlsettings.html]| |Sub-property may require GR| |
