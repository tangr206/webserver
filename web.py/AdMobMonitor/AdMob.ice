#ifndef __AD_MOB_ICE__
#define __AD_MOB_ICE__

//#include <Util.ice>

module xce{
module ad{

struct AdMobClientInfo{
  string model;      //手机型号 Sony Ericsson MT15i
  string uniqid;     //IMEI 012703000763966
  string osVersion;  //OS版本   Android OS2.3.4
  string screenSize; //屏幕尺寸 320*480
  string from;       //渠道ID   9600101
  string version;    //应用版本 4.5.1
  string mac;        //mac地址  30-17-c8-fc-10-47
  string type;		 //终端类型,平台+展示载体+广告位+扩展位 AABBCCDDD
};

struct Location{
  double longitude;  //经度
  double latitude;   //纬度
  double precision;  //精度
};

struct AdPageData{
  string clickUrl;  //用户点击广告banner后调整的地址
  string htmlData;  //广告页面代码
  string flag;      //用于标记点击后跳转的页面是否是人人站内页面 人人网01
};

sequence<long> GroupIdSeq;

struct AdMobReqPara{
  int uid;                      //用户唯一标识
  long requestTime;             //请求时间 yyyymmddhh24miss  
  long adzoneId;                //广告位唯一标识 网站8位+广告位4位 100000000099
  string requestId;             //广告请求唯一标识 UID+时间 34326785520120308230121
  string netStatus;             //AABB 网络状态 wifi:01 运营商移动:02  + 移动01 联通02 电信03
  string appid;                 //应用编号131826
  string sid;                   //用户身份密钥
  string locationHistory;		//历史位置数据
  string ipArea;				//用户的ip area code
  Location locationRealTime;    //实时位置数据
  GroupIdSeq lastGroupIds;		//历史展示的广告
  AdMobClientInfo client;

  double res1;                  //保留字1 double
  string res2;                  //保留字2 string
};

struct AdMobResPara{
  int uid;                //用户唯一标识
  long adgroupId;         //广告唯一标识
  long adzoneId;          //广告位唯一标识
  string requestId;       //广告请求编号
  long sendTime;          //广告下发时间 20120308230122
  AdPageData pageData;    //广告页面数据

  double res1;
  string res2;
};

struct AdMobFeedback{
  int uid;  //用户唯一标识
  long displayTime;  //广告展示时刻  20120308230121
  long adzoneId;  //广告位唯一标识 网站8位+广告位4位 100000000099
  long requestId; //广告请求唯一标识 UID+时间 34326785520120308230121
  long sendTime;  //广告下发时间 20120308230122
  string appid;      //应用编号131826
  string netStatus;  //AABB 网络状态 wifi:01 运营商移动:02  + 移动01 联通02 电信03
  string flagStatus; //广告展示状态 刷新次数+跳转次数+上次刷新或跳转后被展示的次数 AAABBBCCC
  AdMobClientInfo client;

  double res1;
  string res2;
};

interface AdMob {
  AdMobResPara GetAds(AdMobReqPara para);
  AdMobResPara GetAdsForTest(AdMobReqPara para);
  void PvFeedBack(AdMobFeedback para);

  void BindUser(int userid, long creativeid, long zoneid);
  void UnBindUser(int userid, long zoneid);
  void NotifyBindUser(int userid, long creativeid, long zoneid);
  void NotifyUnBindUser(int userid, long zoneid);
};

struct AdMobTargetInput {
  int type;
  long zoneid;
  
  short age;
  short gender;
  short stage;
  short grade;
  int uid;
  string school;
  string ipArea;
  string currentArea;
  string screenSize;
  string model;
  string osVersion;
  string netStatus;
  double lbsx;
  double lbsy;
};

struct AdMobTargetOutput {
  long groupID;
  long memberID;
  long campaignID;
  long bidUnitID;
  int transType;
  int memberCategory;
  double price;
};

sequence<AdMobTargetOutput> AdMobTargetOutputSeq;

interface AdMobMonitor {
  string GetPoolValue(int pool, long id);
  int GetPoolSize(int pool);
  string GetPoolAll(int pool, int size);

  string GetBrandCandidateGroups(AdMobReqPara para, int index);
  string GetSelfCandidateGroups(AdMobReqPara para, int index);

  AdMobTargetOutputSeq GetTargetGroups(AdMobTargetInput input);

  string GetRotateGroups(long zone);

  string GetBrandIndexInfo(int index, long zone);
  string GetSelfIndexInfo(int index, long zone);

};

}; //end of namespace ad
}; //end of namespace xce
#endif
