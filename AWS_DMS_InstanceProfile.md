||No.||Property||Description||Type||Threat Context||GR Required||Jira Story
|1|SubnetGroupIdentifier|The identifier of the subnet group that is associated with the instance profile.|String| |Yes| |
|2|Description|A description of the instance profile. Descriptions can have up to 31 characters.  A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't  end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.|String| | | |
|3|InstanceProfileName|The user-friendly name for the instance profile.|String| | | |
|4|KmsKeyArn|The Amazon Resource Name (ARN) of the AWS KMS key that is used to encrypt  the connection parameters for the instance profile.|String| |Yes| |
|5|NetworkType|Specifies the network type for the instance profile. A value of IPV4  represents an instance profile with IPv4 network type and only supports IPv4 addressing.  A value of IPV6 represents an instance profile with IPv6 network type  and only supports IPv6 addressing. A value of DUAL represents an instance  profile with dual network type that supports IPv4 and IPv6 addressing.|String| | | |
|6|AvailabilityZone|The Availability Zone where the instance profile runs.|String| | | |
|7|PubliclyAccessible|Specifies the accessibility options for the instance profile. A value of true represents an instance profile with a public IP address. A value of false represents an instance profile with a private IP address. The default value is true.|Boolean| | | |
|8|VpcSecurityGroups|The VPC security groups that are used with the instance profile.  The VPC security group must work with the VPC containing the instance profile.|Array of String| |Yes| |
|9|Tags|Property description not available.|[Array of Tag|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-instanceprofile-tag.html]| |Yes| |
|10|InstanceProfileIdentifier|The identifier of the instance profile. Identifiers must begin with a letter  and must contain only ASCII letters, digits, and hyphens. They can't end with  a hyphen, or contain two consecutive hyphens.|String| |Yes| |
