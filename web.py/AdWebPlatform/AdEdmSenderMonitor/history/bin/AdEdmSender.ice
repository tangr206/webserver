#ifndef __AD_EDM_SENDER__
#define __AD_EDM_SENDER__

//#include <Util.ice>

module xce {
  module ad {
		struct EdmClientInfo{
		  string model;      //手机型号 Sony Ericsson MT15i
		  string uniqid;     //IMEI 012703000763966
		  string osVersion;  //OS版本   Android OS2.3.4
		  string screenSize; //屏幕尺寸 320*480
		  string from;       //渠道ID   9600101
		  string version;    //应用版本 4.5.1
		  string mac;        //mac地址  30-17-c8-fc-10-47
		  string type;     //终端类型,平台+展示载体+广告位+扩展位 AABBCCDDD
		};

		struct LbsLocation{
		  double longitude;  //经度
		  double latitude;   //纬度
		  double precision;  //精度
		};

		struct EdmReqPara{
		  int uid;               //用户唯一标识
		  long requestTime;  //请求时间 yyyymmddhh24miss  
		  string requestId;    //广告请求唯一标识 UID+时间 34326785520120308230121
		  string netStatus;    //AABB 网络状态 wifi:01 运营商移动:02  + 移动01 联通02 电信03
		  string appid;        //应用编号131826
		  string ip;            //用户的ip
		  LbsLocation locationRealTime;    //实时位置数据
		  EdmClientInfo client;
		
		  double res1;                  //保留字1 double
		  string res2;                   //保留字2 string
		};

		sequence<long> groups;
    dictionary<string, string> Str2StrMap;

		interface AdEdmSender {
			void SendEdmFor3G(int userId, EdmReqPara para, Str2StrMap params);
			void ExposeFor3G(int userId, long adgroupId, int index);                     //3g Edm 曝光接口
			void SendEdm(int userId, Str2StrMap params); //web Edm 发送接口
			void Expose(int userId, long adgroupId, int index);  //web Edm 曝光接口
			void SendEdmTest(int userId,Str2StrMap params);
			void ClearLoginCacheByUser(int userid);
			groups GetCandidateGroups(int userid);
		};

    interface AdEdmSenderMonitor {
      string PrintEdmDiscount();
      string PrintEdmInvertedIndex(int edmmembertype, int indextype);
      string PrintFrequencyRestric();
      string PrintFrequencyCache(int userid);
      string PrintMemberId();
      string PrintCampaignId();
      string PrintGroupId();
      string PrintAdLeftBlackList();
      string PrintSchoolPool();
      string PrintPlatformMap();
      string PrintEngineParametersCache();
      string PrintEngineConfig();
    };


  };
};
#endif
