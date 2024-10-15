||No.||Property||Description||Type||Threat Context||Common Property||GR Required||Jira Story
|1|DataProviderName|The name of the data provider.|String| |No| | |
|2|Description|A description of the data provider. Descriptions can have up to 31 characters.  A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't  end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.|String| |Yes| | |
|3|ExactSettings|Property description not available.|Boolean| |No| | |
|4|Engine|The type of database engine for the data provider. Valid values include "aurora",  "aurora-postgresql", "mysql", "oracle", "postgres",  "sqlserver", redshift, mariadb, mongodb, and docdb. A value of "aurora" represents Amazon Aurora MySQL-Compatible Edition.|String| |No| | |
|5|Settings|The settings in JSON format for a data provider.|[Settings|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-settings.html]| |No|Sub-property may require GR| |
|6|Tags|Property description not available.|[Array of Tag|http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-dataprovider-tag.html]| |Yes|Sub-property may require GR| |
|7|DataProviderIdentifier|The identifier of the data provider. Identifiers must begin with a letter  and must contain only ASCII letters, digits, and hyphens. They can't end with  a hyphen, or contain two consecutive hyphens.|String| |No|Yes| |
