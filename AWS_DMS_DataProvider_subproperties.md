||No.||Sub-property and Parent||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode\AWS_DMS_DataProvider\MicrosoftSqlServerSettings|Property description not available.|String| | | |
|2|ServerName\AWS_DMS_DataProvider\MicrosoftSqlServerSettings|Fully qualified domain name of the endpoint. For an Amazon RDS SQL Server instance, this is the output of DescribeDBInstances, in the Endpoint.Address field.|String| | | |
|3|Port\AWS_DMS_DataProvider\MicrosoftSqlServerSettings|Endpoint TCP port.|Integer| | | |
|4|DatabaseName\AWS_DMS_DataProvider\MicrosoftSqlServerSettings|Database name for the endpoint.|String| | | |
|5|CertificateArn\AWS_DMS_DataProvider\MicrosoftSqlServerSettings|Property description not available.|String| | | |
||No.||Sub-property and Parent||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode\AWS_DMS_DataProvider\MySqlSettings|Property description not available.|String| | | |
|2|ServerName\AWS_DMS_DataProvider\MySqlSettings|The host name of the endpoint database. |String| | | |
|3|Port\AWS_DMS_DataProvider\MySqlSettings|Endpoint TCP port.|Integer| | | |
|4|CertificateArn\AWS_DMS_DataProvider\MySqlSettings|Property description not available.|String| | | |
||No.||Sub-property and Parent||Description||Type||Threat Context||GR Required||Jira Story
|1|SecretsManagerOracleAsmAccessRoleArn\AWS_DMS_DataProvider\OracleSettings|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the SecretsManagerOracleAsmSecret. This SecretsManagerOracleAsmSecret has the secret value that allows access to the Oracle ASM of the endpoint.|String| | | |
|2|SecretsManagerOracleAsmSecretId\AWS_DMS_DataProvider\OracleSettings|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN, partial ARN, or friendly name of the SecretsManagerOracleAsmSecret  that contains the Oracle ASM connection details for the Oracle endpoint.|String| | | |
|3|SslMode\AWS_DMS_DataProvider\OracleSettings|Property description not available.|String| | | |
|4|SecretsManagerSecurityDbEncryptionSecretId\AWS_DMS_DataProvider\OracleSettings|Property description not available.|String| | | |
|5|ServerName\AWS_DMS_DataProvider\OracleSettings|Fully qualified domain name of the endpoint.|String| | | |
|6|Port\AWS_DMS_DataProvider\OracleSettings|Endpoint TCP port.|Integer| | | |
|7|DatabaseName\AWS_DMS_DataProvider\OracleSettings|Database name for the endpoint.|String| | | |
|8|AsmServer\AWS_DMS_DataProvider\OracleSettings|For an Oracle source endpoint, your ASM server address. You can set this value from the asm_server value. You set asm_server as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see Configuration for change data capture (CDC) on an Oracle source database.|String| | | |
|9|CertificateArn\AWS_DMS_DataProvider\OracleSettings|Property description not available.|String| | | |
|10|SecretsManagerSecurityDbEncryptionAccessRoleArn\AWS_DMS_DataProvider\OracleSettings|Property description not available.|String| | | |
||No.||Sub-property and Parent||Description||Type||Threat Context||GR Required||Jira Story
|1|SslMode\AWS_DMS_DataProvider\PostgreSqlSettings|Property description not available.|String| | | |
|2|ServerName\AWS_DMS_DataProvider\PostgreSqlSettings|The host name of the endpoint database. |String| | | |
|3|Port\AWS_DMS_DataProvider\PostgreSqlSettings|Endpoint TCP port. The default is 5432.|Integer| | | |
|4|DatabaseName\AWS_DMS_DataProvider\PostgreSqlSettings|Database name for the endpoint.|String| | | |
|5|CertificateArn\AWS_DMS_DataProvider\PostgreSqlSettings|Property description not available.|String| | | |
||No.||Sub-property and Parent||Description||Type||Threat Context||GR Required||Jira Story
|1|OracleSettings\AWS_DMS_DataProvider\Settings|Property description not available.|[OracleSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-oraclesettings.html]| | | |
|2|MicrosoftSqlServerSettings\AWS_DMS_DataProvider\Settings|Property description not available.|[MicrosoftSqlServerSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-microsoftsqlserversettings.html]| | | |
|3|MySqlSettings\AWS_DMS_DataProvider\Settings|Property description not available.|[MySqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-mysqlsettings.html]| | | |
|4|PostgreSqlSettings\AWS_DMS_DataProvider\Settings|Property description not available.|[PostgreSqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-postgresqlsettings.html]| | | |
