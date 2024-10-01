||Property||Resources
|SslMode|AWS::DMS::DataProvider.MicrosoftSqlServerSettings \\ AWS::DMS::DataProvider.MySqlSettings \\ AWS::DMS::DataProvider.OracleSettings \\ AWS::DMS::DataProvider.PostgreSqlSettings \\ |
|ServerName|AWS::DMS::DataProvider.MicrosoftSqlServerSettings \\ AWS::DMS::DataProvider.MySqlSettings \\ AWS::DMS::DataProvider.OracleSettings \\ AWS::DMS::DataProvider.PostgreSqlSettings \\ AWS::DMS::Endpoint.GcpMySQLSettings \\ AWS::DMS::Endpoint.MicrosoftSqlServerSettings \\ AWS::DMS::Endpoint.MongoDbSettings \\ AWS::DMS::Endpoint.RedisSettings \\ |
|Port|AWS::DMS::DataProvider.MicrosoftSqlServerSettings \\ AWS::DMS::DataProvider.MySqlSettings \\ AWS::DMS::DataProvider.OracleSettings \\ AWS::DMS::DataProvider.PostgreSqlSettings \\ AWS::DMS::Endpoint.GcpMySQLSettings \\ AWS::DMS::Endpoint.MicrosoftSqlServerSettings \\ AWS::DMS::Endpoint.MongoDbSettings \\ AWS::DMS::Endpoint.RedisSettings \\ |
|DatabaseName|AWS::DMS::DataProvider.MicrosoftSqlServerSettings \\ AWS::DMS::DataProvider.OracleSettings \\ AWS::DMS::DataProvider.PostgreSqlSettings \\ AWS::DMS::Endpoint.GcpMySQLSettings \\ AWS::DMS::Endpoint.MicrosoftSqlServerSettings \\ AWS::DMS::Endpoint.MongoDbSettings \\ |
|CertificateArn|AWS::DMS::DataProvider.MicrosoftSqlServerSettings \\ AWS::DMS::DataProvider.MySqlSettings \\ AWS::DMS::DataProvider.OracleSettings \\ AWS::DMS::DataProvider.PostgreSqlSettings \\ |
|SecretsManagerOracleAsmAccessRoleArn|AWS::DMS::DataProvider.OracleSettings \\ AWS::DMS::Endpoint.OracleSettings \\ |
|SecretsManagerOracleAsmSecretId|AWS::DMS::DataProvider.OracleSettings \\ AWS::DMS::Endpoint.OracleSettings \\ |
|AsmServer|AWS::DMS::DataProvider.OracleSettings \\ AWS::DMS::Endpoint.OracleSettings \\ |
|DocsToInvestigate|AWS::DMS::Endpoint.DocDbSettings \\ AWS::DMS::Endpoint.MongoDbSettings \\ |
|ExtractDocId|AWS::DMS::Endpoint.DocDbSettings \\ AWS::DMS::Endpoint.MongoDbSettings \\ |
|SecretsManagerSecretId|AWS::DMS::Endpoint.DocDbSettings \\ AWS::DMS::Endpoint.GcpMySQLSettings \\ AWS::DMS::Endpoint.IbmDb2Settings \\ AWS::DMS::Endpoint.MicrosoftSqlServerSettings \\ AWS::DMS::Endpoint.MongoDbSettings \\ AWS::DMS::Endpoint.MySqlSettings \\ AWS::DMS::Endpoint.OracleSettings \\ AWS::DMS::Endpoint.PostgreSqlSettings \\ AWS::DMS::Endpoint.RedshiftSettings \\ AWS::DMS::Endpoint.SybaseSettings \\ AWS::DMS::MigrationProject.DataProviderDescriptor \\ |
|SecretsManagerAccessRoleArn|AWS::DMS::Endpoint.DocDbSettings \\ AWS::DMS::Endpoint.GcpMySQLSettings \\ AWS::DMS::Endpoint.IbmDb2Settings \\ AWS::DMS::Endpoint.MicrosoftSqlServerSettings \\ AWS::DMS::Endpoint.MongoDbSettings \\ AWS::DMS::Endpoint.MySqlSettings \\ AWS::DMS::Endpoint.OracleSettings \\ AWS::DMS::Endpoint.PostgreSqlSettings \\ AWS::DMS::Endpoint.RedshiftSettings \\ AWS::DMS::Endpoint.SybaseSettings \\ AWS::DMS::MigrationProject.DataProviderDescriptor \\ |
|NestingLevel|AWS::DMS::Endpoint.DocDbSettings \\ AWS::DMS::Endpoint.MongoDbSettings \\ |
|ServiceAccessRoleArn|AWS::DMS::Endpoint.DynamoDbSettings \\ AWS::DMS::Endpoint.ElasticsearchSettings \\ AWS::DMS::Endpoint.KinesisSettings \\ AWS::DMS::Endpoint.NeptuneSettings \\ AWS::DMS::Endpoint.RedshiftSettings \\ AWS::DMS::Endpoint.S3Settings \\ |
|ErrorRetryDuration|AWS::DMS::Endpoint.ElasticsearchSettings \\ AWS::DMS::Endpoint.NeptuneSettings \\ |
|AfterConnectScript|AWS::DMS::Endpoint.GcpMySQLSettings \\ AWS::DMS::Endpoint.MySqlSettings \\ AWS::DMS::Endpoint.PostgreSqlSettings \\ AWS::DMS::Endpoint.RedshiftSettings \\ |
|CleanSourceMetadataOnMismatch|AWS::DMS::Endpoint.GcpMySQLSettings \\ AWS::DMS::Endpoint.MySqlSettings \\ |
|ServerTimezone|AWS::DMS::Endpoint.GcpMySQLSettings \\ AWS::DMS::Endpoint.MySqlSettings \\ |
|EventsPollInterval|AWS::DMS::Endpoint.GcpMySQLSettings \\ AWS::DMS::Endpoint.MySqlSettings \\ |
|ParallelLoadThreads|AWS::DMS::Endpoint.GcpMySQLSettings \\ AWS::DMS::Endpoint.MySqlSettings \\ |
|Username|AWS::DMS::Endpoint.GcpMySQLSettings \\ AWS::DMS::Endpoint.MicrosoftSqlServerSettings \\ AWS::DMS::Endpoint.MongoDbSettings \\ |
|MaxFileSize|AWS::DMS::Endpoint.GcpMySQLSettings \\ AWS::DMS::Endpoint.IbmDb2Settings \\ AWS::DMS::Endpoint.MySqlSettings \\ AWS::DMS::Endpoint.NeptuneSettings \\ AWS::DMS::Endpoint.PostgreSqlSettings \\ AWS::DMS::Endpoint.RedshiftSettings \\ AWS::DMS::Endpoint.S3Settings \\ |
|Password|AWS::DMS::Endpoint.GcpMySQLSettings \\ AWS::DMS::Endpoint.MicrosoftSqlServerSettings \\ AWS::DMS::Endpoint.MongoDbSettings \\ |
|LoadTimeout|AWS::DMS::Endpoint.IbmDb2Settings \\ AWS::DMS::Endpoint.RedshiftSettings \\ |
|WriteBufferSize|AWS::DMS::Endpoint.IbmDb2Settings \\ AWS::DMS::Endpoint.RedshiftSettings \\ |
|MessageFormat|AWS::DMS::Endpoint.KafkaSettings \\ AWS::DMS::Endpoint.KinesisSettings \\ |
|IncludeTransactionDetails|AWS::DMS::Endpoint.KafkaSettings \\ AWS::DMS::Endpoint.KinesisSettings \\ |
|IncludeTableAlterOperations|AWS::DMS::Endpoint.KafkaSettings \\ AWS::DMS::Endpoint.KinesisSettings \\ |
|SslCaCertificateArn|AWS::DMS::Endpoint.KafkaSettings \\ AWS::DMS::Endpoint.RedisSettings \\ |
|IncludeControlDetails|AWS::DMS::Endpoint.KafkaSettings \\ AWS::DMS::Endpoint.KinesisSettings \\ |
|IncludePartitionValue|AWS::DMS::Endpoint.KafkaSettings \\ AWS::DMS::Endpoint.KinesisSettings \\ |
|NoHexPrefix|AWS::DMS::Endpoint.KafkaSettings \\ AWS::DMS::Endpoint.KinesisSettings \\ |
|PartitionIncludeSchemaTable|AWS::DMS::Endpoint.KafkaSettings \\ AWS::DMS::Endpoint.KinesisSettings \\ |
|IncludeNullAndEmpty|AWS::DMS::Endpoint.KafkaSettings \\ AWS::DMS::Endpoint.KinesisSettings \\ |
|AuthType|AWS::DMS::Endpoint.MongoDbSettings \\ AWS::DMS::Endpoint.RedisSettings \\ |
|FailTasksOnLobTruncation|AWS::DMS::Endpoint.OracleSettings \\ AWS::DMS::Endpoint.PostgreSqlSettings \\ |
|MapBooleanAsBoolean|AWS::DMS::Endpoint.PostgreSqlSettings \\ AWS::DMS::Endpoint.RedshiftSettings \\ |
|BucketName|AWS::DMS::Endpoint.RedshiftSettings \\ AWS::DMS::Endpoint.S3Settings \\ |
|ServerSideEncryptionKmsKeyId|AWS::DMS::Endpoint.RedshiftSettings \\ AWS::DMS::Endpoint.S3Settings \\ |
|BucketFolder|AWS::DMS::Endpoint.RedshiftSettings \\ AWS::DMS::Endpoint.S3Settings \\ |
|EncryptionMode|AWS::DMS::Endpoint.RedshiftSettings \\ AWS::DMS::Endpoint.S3Settings \\ |
