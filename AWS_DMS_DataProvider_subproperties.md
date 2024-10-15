||No.||Subprops of AWS_DMS_DataProvider MicrosoftSqlServerSettings||Description||Type||Threat Context||Common Property||GR Required||Jira Story
|1|SslMode|Property description not available.|String| |Yes| | |
|2|ServerName|Fully qualified domain name of the endpoint. For an Amazon RDS SQL Server instance, this is the output of DescribeDBInstances, in the Endpoint.Address field.|String| |Yes| | |
|3|Port|Endpoint TCP port.|Integer| |Yes| | |
|4|DatabaseName|Database name for the endpoint.|String| |Yes| | |
|5|CertificateArn|Property description not available.|String| |Yes|Yes| |
||No.||Subprops of AWS_DMS_DataProvider MySqlSettings||Description||Type||Threat Context||Common Property||GR Required||Jira Story
|1|SslMode|Property description not available.|String| |Yes| | |
|2|ServerName|The host name of the endpoint database. |String| |Yes| | |
|3|Port|Endpoint TCP port.|Integer| |Yes| | |
|4|CertificateArn|Property description not available.|String| |Yes|Yes| |
||No.||Subprops of AWS_DMS_DataProvider OracleSettings||Description||Type||Threat Context||Common Property||GR Required||Jira Story
|1|SecretsManagerOracleAsmAccessRoleArn|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the SecretsManagerOracleAsmSecret. This SecretsManagerOracleAsmSecret has the secret value that allows access to the Oracle ASM of the endpoint.|String| |Yes|Yes| |
|2|SecretsManagerOracleAsmSecretId|Required only if your Oracle endpoint uses Automatic Storage Management (ASM). The full ARN, partial ARN, or friendly name of the SecretsManagerOracleAsmSecret  that contains the Oracle ASM connection details for the Oracle endpoint.|String| |Yes|Yes| |
|3|SslMode|Property description not available.|String| |Yes| | |
|4|SecretsManagerSecurityDbEncryptionSecretId|Property description not available.|String| |No|Yes| |
|5|ServerName|Fully qualified domain name of the endpoint.|String| |Yes| | |
|6|Port|Endpoint TCP port.|Integer| |Yes| | |
|7|DatabaseName|Database name for the endpoint.|String| |Yes| | |
|8|AsmServer|For an Oracle source endpoint, your ASM server address. You can set this value from the asm_server value. You set asm_server as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see Configuration for change data capture (CDC) on an Oracle source database.|String| |Yes| | |
|9|CertificateArn|Property description not available.|String| |Yes|Yes| |
|10|SecretsManagerSecurityDbEncryptionAccessRoleArn|Property description not available.|String| |No|Yes| |
||No.||Subprops of AWS_DMS_DataProvider PostgreSqlSettings||Description||Type||Threat Context||Common Property||GR Required||Jira Story
|1|SslMode|Property description not available.|String| |Yes| | |
|2|ServerName|The host name of the endpoint database. |String| |Yes| | |
|3|Port|Endpoint TCP port. The default is 5432.|Integer| |Yes| | |
|4|DatabaseName|Database name for the endpoint.|String| |Yes| | |
|5|CertificateArn|Property description not available.|String| |Yes|Yes| |
||No.||Subprops of AWS_DMS_DataProvider Settings||Description||Type||Threat Context||Common Property||GR Required||Jira Story
|1|OracleSettings|Property description not available.|[OracleSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-oraclesettings.html]| |No|Sub-property may require GR| |
|2|MicrosoftSqlServerSettings|Property description not available.|[MicrosoftSqlServerSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-microsoftsqlserversettings.html]| |No|Sub-property may require GR| |
|3|MySqlSettings|Property description not available.|[MySqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-mysqlsettings.html]| |No|Sub-property may require GR| |
|4|PostgreSqlSettings|Property description not available.|[PostgreSqlSettings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-postgresqlsettings.html]| |No|Sub-property may require GR| |
