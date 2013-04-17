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
 * 此FeedBuilder_805_1用于构建发送stype为805，数据版本为1的新鲜事
 * 新鲜事说明：人人桌面连续登录7天赠送vip
 * @author antonio
 *
 */

class FeedBuilder_805_1 {
	/**新鲜事的类型*/
	public final static int stype = 805;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  private Map<String,Long> _config = new HashMap<String, Long>();
  public FeedBuilder_805_1 () {
    
        _flag.put("title" , false);
        _flag.put("msg" , false);
        _flag.put("legend" , false);
        _flag.put("vipIcon" , false);
        _flag.put("vipIconLink" , false);
        _flag.put("imgLink" , false);
        _flag.put("imgSrc" , false);
        _flag.put("from.id" , false);
        _flag.put("from.name" , false);
        _flag.put("from.tinyimg" , false);
        _flag.put("time" , false);

    

    
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
   *@param title comment:新鲜事的title
   */
  public void SetKey_title( String  title){
    
    _data.put("title", String.valueOf( title ) );
    _flag.put("title",true);
  }
  
  /**
   *@param msg comment:新鲜事中的具体描述文字
   */
  public void SetKey_msg( String  msg){
    
    _data.put("msg", String.valueOf( msg ) );
    _flag.put("msg",true);
  }
  
  /**
   *@param legend comment:下方的detail相当于footer的部分
   */
  public void SetKey_legend( String  legend){
    
    _data.put("legend", String.valueOf( legend ) );
    _flag.put("legend",true);
  }
  
  /**
   *@param vipIcon comment:vip标识的图片
   */
  public void SetKey_vipIcon( String  vipIcon){
    
    _data.put("vipIcon", String.valueOf( vipIcon ) );
    _flag.put("vipIcon",true);
  }
  
  /**
   *@param vipIconLink comment:vip标的链接
   */
  public void SetKey_vipIconLink( String  vipIconLink){
    
    _data.put("vipIconLink", String.valueOf( vipIconLink ) );
    _flag.put("vipIconLink",true);
  }
  
  /**
   *@param imgLink comment:新鲜事内部图片的链接
   */
  public void SetKey_imgLink( String  imgLink){
    
    _data.put("imgLink", String.valueOf( imgLink ) );
    _flag.put("imgLink",true);
  }
  
  /**
   *@param imgSrc comment:新鲜事内部的图片
   */
  public void SetKey_imgSrc( String  imgSrc){
    
    _data.put("imgSrc", String.valueOf( imgSrc ) );
    _flag.put("imgSrc",true);
  }
  
  /**
   *@param from_id comment:触发者id
   */
  public void SetKey_from_id( long  from_id){
    
    _data.put("from.id", String.valueOf( from_id ) );
    _flag.put("from.id",true);
  }
  
  /**
   *@param from_name comment:触发者的名字
   */
  public void SetKey_from_name( String  from_name){
    
    _data.put("from.name", String.valueOf( from_name ) );
    _flag.put("from.name",true);
  }
  
  /**
   *@param from_tinyimg comment:触发者的头像
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
   *@param time comment:时间戳
   */
  public void SetKey_time( long  time){
    
    _data.put("time", String.valueOf( time ) );
    _flag.put("time",true);
  }
  

  
  

  

  /**
   *@param push_flag comment:推送策略, 0x01-NewsFeed 0x02-MiniFeed 0x04-IM 0x08-CLASS 0x10-MiniGroup
   */
  public void SetConfig_push_flag(long push_flag){
    _config.put("push_flag", push_flag);
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
