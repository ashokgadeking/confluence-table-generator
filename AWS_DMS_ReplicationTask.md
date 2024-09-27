||No.||Property||Description||Type||Threat Context||GR Required||Jira Story
|1|ReplicationTaskSettings|Overall settings for the task, in JSON format. For more information, see  Specifying Task Settings for AWS Database Migration Service Tasks in the  AWS Database Migration Service User Guide.|String| |no| |
|2|CdcStartPosition|Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.|String| |no| |
|3|CdcStopPosition|Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.|String| |no| |
|4|MigrationType|The migration type. Valid values: full-load | cdc | full-load-and-cdc|String| |no| |
|5|TargetEndpointArn|An Amazon Resource Name (ARN) that uniquely identifies the target endpoint.|String| |no| |
|6|ReplicationInstanceArn|The Amazon Resource Name (ARN) of a replication instance.|String| |no| |
|7|TaskData|Supplemental information that the task requires to migrate the data for certain source and target endpoints.  For more information, see Specifying Supplemental Data for Task Settings in the  AWS Database Migration Service User Guide.|String| |no| |
|8|CdcStartTime|Indicates the start time for a change data capture (CDC) operation.|Number| |no| |
|9|ResourceIdentifier|A display name for the resource identifier at the end of the EndpointArn response parameter that is returned in the created Endpoint object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as Example-App-ARN1. |String| |no| |
|10|TableMappings|The table mappings for the task, in JSON format. For more information, see  Using Table Mapping to Specify Task Settings in the  AWS Database Migration Service User Guide.|String| |no| |
|11|ReplicationTaskIdentifier|An identifier for the replication task.|String| |no| |
|12|SourceEndpointArn|An Amazon Resource Name (ARN) that uniquely identifies the source endpoint.|String| |no| |
|13|Tags|One or more tags to be assigned to the replication task.|[Array of Tag|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationtask-tag.html]| |Sub-property may require GR| |
