
module xce
{
	module ad
	{
		sequence<long> ZoneSequence;
		sequence<long> creativeSequence;

		struct GroupInfo
		{
			long groupID;
			long memberID;
			long campaignID;
			long widgetID;
			long bidUnitID;
			int transType;
			int memberCategory;
      			int memberIndustry;
			int triggerType;
			double price;
			double ctr;
      			string extend;
			creativeSequence creatives;
		};

		struct TriggerInputInfo 
		{
			short age;
			short gender;
			short stage;
			short grade;
			int uid;
			string school;
			string ipArea;
			string currentArea;
      			string company;
      			string extend;

			ZoneSequence zones;
		};

		sequence<GroupInfo> GroupSequence;
		dictionary<long, GroupSequence> GroupDict;

		class IndexService 
		{
			int trigger(TriggerInputInfo input, out GroupDict ZoneInfoMap);
      			void Close(int uid, long creativeid);
		};

    		interface IndexMonitor {
      			string GetAdPoolInfo(int type);//0,广告商;1,广告计划;2,广告组
     			string GetAdZonePrice(long groupId);//广告组在广告位上的标价
      			string GetZoneAdNum();
      			string GetTriggerInfo();
      			string GetGameAdNum();
      			string GetGameMemNum();
      			string GetZoneIndex(long zoneId, int index);//广告位上对应的索引
      			string GetClosedAd();
    		};
	};
};

