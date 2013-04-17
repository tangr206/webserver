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
 * 此FeedBuilder_137_1用于构建发送stype为137，数据版本为1的新鲜事
 * 新鲜事说明：分享站内原创视频
 * @author antonio
 *
 */

class FeedBuilder_137_1 {
	/**新鲜事的类型*/
	public final static int stype = 137;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  private Map<String,String> _config = new HashMap<String, String>();
  public FeedBuilder_137_1 () {
    
        _flag.put("time" , false);
        _flag.put("from.id" , false);
        _flag.put("from.name" , false);
        _flag.put("from.tinyimg" , false);
        _flag.put("from.url" , false);
        _flag.put("origin.id" , false);
        _flag.put("origin.url" , false);
        _flag.put("origin.name" , false);
        _flag.put("video.id" , false);
        _flag.put("video.description" , false);
        _flag.put("video.picurl" , false);
        _flag.put("video.url" , false);
        _flag.put("video.title" , false);
        _flag.put("share.id" , false);

    

    
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
   *@param time comment:时间戳
   */
  public void SetKey_time( long  time){
    
    _data.put("time", String.valueOf( time ) );
    _flag.put("time",true);
  }
  
  /**
   *@param from_id comment:分享者id
   */
  public void SetKey_from_id( long  from_id){
    
    _data.put("from.id", String.valueOf( from_id ) );
    _flag.put("from.id",true);
  }
  
  /**
   *@param from_name comment:分享者name
   */
  public void SetKey_from_name( String  from_name){
    
    _data.put("from.name", String.valueOf( from_name ) );
    _flag.put("from.name",true);
  }
  
  /**
   *@param from_tinyimg comment:分享者小头像
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
   *@param from_url comment:分享者主页
   */
  public void SetKey_from_url( String  from_url){
    
    _data.put("from.url", String.valueOf( from_url ) );
    _flag.put("from.url",true);
  }
  
  /**
   *@param origin_id comment:源作者id
   */
  public void SetKey_origin_id( long  origin_id){
    
    _data.put("origin.id", String.valueOf( origin_id ) );
    _flag.put("origin.id",true);
  }
  
  /**
   *@param origin_url comment:源作者主页
   */
  public void SetKey_origin_url( String  origin_url){
    
    if(!CheckUrl(origin_url )){
    	_flag.put("origin.url",false);
    	return;
    }
    
    _data.put("origin.url", String.valueOf( origin_url ) );
    _flag.put("origin.url",true);
  }
  
  /**
   *@param origin_name comment:源作者name
   */
  public void SetKey_origin_name( String  origin_name){
    
    _data.put("origin.name", String.valueOf( origin_name ) );
    _flag.put("origin.name",true);
  }
  
  /**
   *@param video_id comment:电影id
   */
  public void SetKey_video_id( long  video_id){
    
    _data.put("video.id", String.valueOf( video_id ) );
    _flag.put("video.id",true);
  }
  
  /**
   *@param video_description comment:电影简介
   */
  public void SetKey_video_description( String  video_description){
    
    _data.put("video.description", String.valueOf( video_description ) );
    _flag.put("video.description",true);
  }
  
  /**
   *@param video_picurl comment:电影图片
   */
  public void SetKey_video_picurl( String  video_picurl){
    
    if(!CheckUrl(video_picurl )){
    	_flag.put("video.picurl",false);
    	return;
    }
    
    _data.put("video.picurl", String.valueOf( video_picurl ) );
    _flag.put("video.picurl",true);
  }
  
  /**
   *@param video_url comment:电影url
   */
  public void SetKey_video_url( String  video_url){
    
    if(!CheckUrl(video_url )){
    	_flag.put("video.url",false);
    	return;
    }
    
    _data.put("video.url", String.valueOf( video_url ) );
    _flag.put("video.url",true);
  }
  
  /**
   *@param video_title comment:电影标题
   */
  public void SetKey_video_title( String  video_title){
    
    _data.put("video.title", String.valueOf( video_title ) );
    _flag.put("video.title",true);
  }
  
  /**
   *@param share_id comment:分享的业务id
   */
  public void SetKey_share_id( long  share_id){
    
    _data.put("share.id", String.valueOf( share_id ) );
    _flag.put("share.id",true);
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
                            FeedCreatorAdapter.getInstance().CreateWithConfig(stype, version, _data, _config);
			}else{
                            FeedCreatorAdapter.getInstance().CreateWithReplyAndConfig(stype, version, _data, reply, _config);
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
