||No.||Property||Description||Type||Threat Context||Common Property||GR Required||Jira Story
|1|TargetDataProviderDescriptors|Information about the target data provider, including the name or ARN, and AWS Secrets Manager parameters.|[Array of DataProviderDescriptor|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-migrationproject-dataproviderdescriptor.html]| |No|Sub-property may require GR| |
|2|MigrationProjectName|The name of the migration project.|String| |No| | |
|3|InstanceProfileName|The name of the associated instance profile.|String| |Yes| | |
|4|Description|A user-friendly description of the migration project.|String| |Yes| | |
|5|MigrationProjectIdentifier|The identifier of the migration project. Identifiers must begin with a letter  and must contain only ASCII letters, digits, and hyphens. They can't end with  a hyphen, or contain two consecutive hyphens.|String| |No|Yes| |
|6|SourceDataProviderDescriptors|Information about the source data provider, including the name or ARN, and AWS Secrets Manager parameters.|[Array of DataProviderDescriptor|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-migrationproject-dataproviderdescriptor.html]| |No|Sub-property may require GR| |
|7|TransformationRules|The settings in JSON format for migration rules. Migration rules make it possible for you to change  the object names according to the rules that you specify. For example, you can change an object name  to lowercase or uppercase, add or remove a prefix or suffix, or rename objects.|String| |No| | |
|8|SchemaConversionApplicationAttributes|The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.|[SchemaConversionApplicationAttributes|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-migrationproject-schemaconversionapplicationattributes.html]| |No|Sub-property may require GR| |
|9|InstanceProfileArn|The Amazon Resource Name (ARN) of the instance profile for your migration project.|String| |No|Yes| |
|10|Tags|Property description not available.|[Array of Tag|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-migrationproject-tag.html]| |Yes|Yes| |
|11|InstanceProfileIdentifier|The identifier of the instance profile for your migration project.|String| |Yes|Yes| |
