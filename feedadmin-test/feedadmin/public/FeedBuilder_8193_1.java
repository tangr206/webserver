import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Iterator;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import MyUtil.MceException;

import xce.feed.FeedTypeConfigNotFoundException;
import xce.feed.NotAllowedToSendException;
import xce.feed.FeedReply;
/**
 * 此FeedBuilder_8193_1用于构建发送stype为8193，数据版本为1的新鲜事
 * 新鲜事说明：销售提出的音乐新鲜事
 * @author antonio
 *
 */

class FeedBuilder_8193_1 {
	/**新鲜事的类型*/
	public final static int stype = 8193;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  private Map<String,String> _config = new HashMap<String, String>();
  public FeedBuilder_8193_1 () {
    
        _flag.put("appId" , false);
        _flag.put("from.id" , false);
        _flag.put("from.name" , false);
        _flag.put("from.tinyimg" , false);
        _flag.put("from.profileUrl" , false);
        _flag.put("title" , false);
        _flag.put("musicUrl" , false);
        _flag.put("time" , false);
        _flag.put("icon" , false);
        _flag.put("actionLink.name" , false);
        _flag.put("actionLink.url" , false);
        _flag.put("activityId" , false);

    

    
  }

  boolean CheckUrl(String url) {
	  if(url.isEmpty()){
		return true;
	  }
	  Pattern p = Pattern
		  .compile("^http://[^#]+$");
	  Matcher m = p.matcher(url);
	  if (m.find()) {
		  return true;
	  }
	  System.err.println("URL格式不正确 url:"+url);
	  return false;
  }

   

  
  /**
   *@param appId comment:发送此新鲜事的app_id
   */
  public void SetKey_appId( long  appId){
    
    _data.put("appId", String.valueOf( appId ) );
    _flag.put("appId",true);
  }
  
  /**
   *@param from_id comment:触发者ID
   */
  public void SetKey_from_id( long  from_id){
    
    _data.put("from.id", String.valueOf( from_id ) );
    _flag.put("from.id",true);
  }
  
  /**
   *@param from_name comment:触发者名字
   */
  public void SetKey_from_name( String  from_name){
    
    _data.put("from.name", String.valueOf( from_name ) );
    _flag.put("from.name",true);
  }
  
  /**
   *@param from_tinyimg comment:触发者头像
   */
  public void SetKey_from_tinyimg( String  from_tinyimg){
    
    if(!CheckUrl(from_tinyimg )){
    	_flag.put("from.tinyimg",false);
    	return;
    }
    
    _data.put("from.tinyimg", String.valueOf( from_tinyimg ) );
    _flag.put("from.tinyimg",true);
  }
  
  /**
   *@param from_profileUrl comment:触发者个人主页地址
   */
  public void SetKey_from_profileUrl( String  from_profileUrl){
    
    if(!CheckUrl(from_profileUrl )){
    	_flag.put("from.profileUrl",false);
    	return;
    }
    
    _data.put("from.profileUrl", String.valueOf( from_profileUrl ) );
    _flag.put("from.profileUrl",true);
  }
  
  /**
   *@param title comment:标题，支持a标签
   */
  public void SetKey_title( String  title){
    
    _data.put("title", String.valueOf( title ) );
    _flag.put("title",true);
  }
  
  /**
   *@param musicUrl comment:mp3音乐的url
   */
  public void SetKey_musicUrl( String  musicUrl){
    
    if(!CheckUrl(musicUrl )){
    	_flag.put("musicUrl",false);
    	return;
    }
    
    _data.put("musicUrl", String.valueOf( musicUrl ) );
    _flag.put("musicUrl",true);
  }
  
  /**
   *@param time comment:新鲜事产生的时间
   */
  public void SetKey_time( long  time){
    
    _data.put("time", String.valueOf( time ) );
    _flag.put("time",true);
  }
  
  /**
   *@param icon comment:图标的地址
   */
  public void SetKey_icon( String  icon){
    
    if(!CheckUrl(icon )){
    	_flag.put("icon",false);
    	return;
    }
    
    _data.put("icon", String.valueOf( icon ) );
    _flag.put("icon",true);
  }
  
  /**
   *@param actionLink_name comment:名字
   */
  public void SetKey_actionLink_name( String  actionLink_name){
    
    _data.put("actionLink.name", String.valueOf( actionLink_name ) );
    _flag.put("actionLink.name",true);
  }
  
  /**
   *@param actionLink_url comment:链接
   */
  public void SetKey_actionLink_url( String  actionLink_url){
    
    if(!CheckUrl(actionLink_url )){
    	_flag.put("actionLink.url",false);
    	return;
    }
    
    _data.put("actionLink.url", String.valueOf( actionLink_url ) );
    _flag.put("actionLink.url",true);
  }
  
  /**
   *@param activityId comment:活动ID，用于去重
   */
  public void SetKey_activityId( long  activityId){
    
    _data.put("activityId", String.valueOf( activityId ) );
    _flag.put("activityId",true);
  }
  

  
  

  

  /**
   *@param isPublishNews comment: “1”-发送newsfeed，“0”-不发送newsfeed
   */
  public void SetConfig_publish_news(String isPublishNews){
    _config.put("publish_news", isPublishNews);
  }

  /**
   *@param isPublishNews comment: “1”-发送minifeed，“0”-不发送minifeed
   */
  public void SetConfig_publish_mini(String isPublishMini){
    _config.put("publish_mini", isPublishMini);
  }

	  /**
	   *调用此方法触发产生新鲜事，用于产生带回复的新鲜事，所以需要传FeedReply参数
	   */
	  public void DispatchFeed(FeedReply reply) {
		  StringBuffer buf = new StringBuffer();

		  Iterator it = _flag.entrySet().iterator();
		  while(it.hasNext()){
			  Map.Entry<String, Boolean> entry = (Map.Entry<String, Boolean>)it.next(); 
			  if(!entry.getValue()){
				  if(buf.length() == 0){
					  buf.append("Any SetKey function not set, include keys:").append(entry.getKey());
				  }else{
					  buf.append(",").append(entry.getKey());
				  }

			  }
		  }
		  if(buf.length() > 0){
			  System.err.println(buf.toString());
			  return;
		  }
  	
		  try {
			if(reply == null){
                          if(_config.size() > 0){
                            FeedCreatorAdapter.getInstance().CreateWithConfig(stype, version, _data, _config);
                          }else{
			    FeedCreatorAdapter.getInstance().Create(stype, version, _data);
                          }
			}else{
			  if(_config.size() > 0){
                            FeedCreatorAdapter.getInstance().CreateWithReplyAndConfig(stype, version, _data, reply, _config);
                          }else{
                            FeedCreatorAdapter.getInstance().CreateWithReply(stype, version, _data, reply);
                          }
			}
		  } catch (FeedTypeConfigNotFoundException e) {
			  e.printStackTrace();
		  } catch (NotAllowedToSendException e) {
			  // TODO Auto-generated catch block
			  e.printStackTrace();
		  } catch (MceException e) {
			  // TODO Auto-generated catch block
			  e.printStackTrace();
		  }
	  }
	/**
	* 调用此方法触发产生新鲜事
	*/
	public void DispatchFeed(){
		DispatchFeed(null);
	}
}
