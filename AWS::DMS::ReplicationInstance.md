||No.||Property||Description||Type||Threat Context||GR Required||Jira Story|1|ReplicationInstanceIdentifier|The replication instance identifier. This parameter is stored as a lowercase string.|String|||||2|EngineVersion|The engine version number of the replication instance.|String|||||3|KmsKeyId|An AWS KMS key identifier that is used to encrypt the data on the replication instance.|String|||||4|AvailabilityZone|The Availability Zone that the replication instance will be created in.|String|||||5|PreferredMaintenanceWindow|The weekly time range during which system maintenance can occur, in UTC.|String|||||6|AutoMinorVersionUpgrade|A value that indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window. This parameter defaults to true.|Boolean|||||7|ReplicationSubnetGroupIdentifier|A subnet group to associate with the replication instance.|String|||||8|AllocatedStorage|The amount of storage (in gigabytes) to be initially allocated for the replication instance.|Integer|||||9|ResourceIdentifier|A display name for the resource identifier at the end of the EndpointArn response parameter that is returned in the created Endpoint object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as Example-App-ARN1. For example, this value might result in the EndpointArn value arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1. If you don't specify a ResourceIdentifier value, AWS DMS generates a default identifier value for the end of EndpointArn.|String|||||10|VpcSecurityGroupIds| Specifies the virtual private cloud (VPC) security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance.|Array of String|||||11|AllowMajorVersionUpgrade|Indicates that major version upgrades are allowed. Changing this parameter does not result in an outage, and the change is asynchronously applied as soon as possible.|Boolean|||||12|ReplicationInstanceClass|The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example, to specify the instance class dms.c4.large, set this parameter to "dms.c4.large". For more information on the settings and capacities for the available replication instance classes, see  Selecting the right AWS DMS replication instance for your migration  in the  AWS Database Migration Service User Guide.|String|||||13|PubliclyAccessible| Specifies the accessibility options for the replication instance. A value of true represents an instance with a public IP address. A value of false represents an instance with a private IP address. The default value is true.|Boolean|||||14|MultiAZ| Specifies whether the replication instance is a Multi-AZ deployment. You can't set the AvailabilityZone parameter if the Multi-AZ parameter is set to true.|Boolean|||||15|Tags|One or more tags to be assigned to the replication instance.|Array of <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationinstance-tag.html">Tag</a>||||