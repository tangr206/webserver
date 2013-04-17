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
 * 此FeedBuilder_102_1用于构建发送stype为102，数据版本为1的新鲜事
 * 新鲜事说明：分享日志
 * @author antonio
 *
 */

class FeedBuilder_102_1 {
	/**新鲜事的类型*/
	public final static int stype = 102;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  public FeedBuilder_102_1 () {
    
        _flag.put("time" , false);
        _flag.put("origin.orignType" , false);
        _flag.put("origin.url" , false);
        _flag.put("origin.title" , false);
        _flag.put("origin.image" , false);
        _flag.put("from.id" , false);
        _flag.put("from.name" , false);
        _flag.put("from.tinyimg" , false);
        _flag.put("from.certifyIcon" , false);
        _flag.put("from.certifyTitle" , false);
        _flag.put("share.id" , false);
        _flag.put("share.comment" , false);
        _flag.put("share.blog.owner.id" , false);
        _flag.put("share.blog.owner.name" , false);
        _flag.put("share.blog.owner.certify" , false);
        _flag.put("share.blog.id" , false);
        _flag.put("share.blog.title" , false);
        _flag.put("share.blog.digest" , false);
        _flag.put("share.blog.url" , false);
        _flag.put("site.id" , false);
        _flag.put("site.name" , false);
        _flag.put("site.url" , false);
        _flag.put("site.blog.title" , false);
        _flag.put("site.blog.url" , false);

    

    
  }

  boolean CheckUrl(String url) {
	  Pattern p = Pattern
		  .compile("^http://.+$");
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
   *@param origin_orignType comment:源类型
   */
  public void SetKey_origin_orignType( String  origin_orignType){
    
    _data.put("origin.orignType", String.valueOf( origin_orignType ) );
    _flag.put("origin.orignType",true);
  }
  
  /**
   *@param origin_url comment:源url
   */
  public void SetKey_origin_url( String  origin_url){
    
    if(!CheckUrl(origin_url )){
    	return;
    }
    
    _data.put("origin.url", String.valueOf( origin_url ) );
    _flag.put("origin.url",true);
  }
  
  /**
   *@param origin_title comment:源标题
   */
  public void SetKey_origin_title( String  origin_title){
    
    _data.put("origin.title", String.valueOf( origin_title ) );
    _flag.put("origin.title",true);
  }
  
  /**
   *@param origin_image comment:源图片
   */
  public void SetKey_origin_image( String  origin_image){
    
    _data.put("origin.image", String.valueOf( origin_image ) );
    _flag.put("origin.image",true);
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
    
    _data.put("from.tinyimg", String.valueOf( from_tinyimg ) );
    _flag.put("from.tinyimg",true);
  }
  
  /**
   *@param from_certifyIcon comment:认证头像
   */
  public void SetKey_from_certifyIcon( String  from_certifyIcon){
    
    _data.put("from.certifyIcon", String.valueOf( from_certifyIcon ) );
    _flag.put("from.certifyIcon",true);
  }
  
  /**
   *@param from_certifyTitle comment:认证标题
   */
  public void SetKey_from_certifyTitle( String  from_certifyTitle){
    
    _data.put("from.certifyTitle", String.valueOf( from_certifyTitle ) );
    _flag.put("from.certifyTitle",true);
  }
  
  /**
   *@param share_id comment:分享id
   */
  public void SetKey_share_id( long  share_id){
    
    _data.put("share.id", String.valueOf( share_id ) );
    _flag.put("share.id",true);
  }
  
  /**
   *@param share_comment comment:分享评论
   */
  public void SetKey_share_comment( String  share_comment){
    
    _data.put("share.comment", String.valueOf( share_comment ) );
    _flag.put("share.comment",true);
  }
  
  /**
   *@param share_blog_owner_id comment:日志owner id
   */
  public void SetKey_share_blog_owner_id( long  share_blog_owner_id){
    
    _data.put("share.blog.owner.id", String.valueOf( share_blog_owner_id ) );
    _flag.put("share.blog.owner.id",true);
  }
  
  /**
   *@param share_blog_owner_name comment:日志owner名字
   */
  public void SetKey_share_blog_owner_name( String  share_blog_owner_name){
    
    _data.put("share.blog.owner.name", String.valueOf( share_blog_owner_name ) );
    _flag.put("share.blog.owner.name",true);
  }
  
  /**
   *@param share_blog_owner_certify comment:日志owner的认证
   */
  public void SetKey_share_blog_owner_certify( String  share_blog_owner_certify){
    
    _data.put("share.blog.owner.certify", String.valueOf( share_blog_owner_certify ) );
    _flag.put("share.blog.owner.certify",true);
  }
  
  /**
   *@param share_blog_id comment:日志id
   */
  public void SetKey_share_blog_id( long  share_blog_id){
    
    _data.put("share.blog.id", String.valueOf( share_blog_id ) );
    _flag.put("share.blog.id",true);
  }
  
  /**
   *@param share_blog_title comment:日志标题
   */
  public void SetKey_share_blog_title( String  share_blog_title){
    
    _data.put("share.blog.title", String.valueOf( share_blog_title ) );
    _flag.put("share.blog.title",true);
  }
  
  /**
   *@param share_blog_digest comment:日志描述摘要
   */
  public void SetKey_share_blog_digest( String  share_blog_digest){
    
    _data.put("share.blog.digest", String.valueOf( share_blog_digest ) );
    _flag.put("share.blog.digest",true);
  }
  
  /**
   *@param share_blog_url comment:日志url
   */
  public void SetKey_share_blog_url( String  share_blog_url){
    
    if(!CheckUrl(share_blog_url )){
    	return;
    }
    
    _data.put("share.blog.url", String.valueOf( share_blog_url ) );
    _flag.put("share.blog.url",true);
  }
  
  /**
   *@param site_id comment:小站的id
   */
  public void SetKey_site_id( long  site_id){
    
    _data.put("site.id", String.valueOf( site_id ) );
    _flag.put("site.id",true);
  }
  
  /**
   *@param site_name comment:小站的name
   */
  public void SetKey_site_name( String  site_name){
    
    _data.put("site.name", String.valueOf( site_name ) );
    _flag.put("site.name",true);
  }
  
  /**
   *@param site_url comment:小站的url
   */
  public void SetKey_site_url( String  site_url){
    
    if(!CheckUrl(site_url )){
    	return;
    }
    
    _data.put("site.url", String.valueOf( site_url ) );
    _flag.put("site.url",true);
  }
  
  /**
   *@param site_blog_title comment:日志标题
   */
  public void SetKey_site_blog_title( String  site_blog_title){
    
    _data.put("site.blog.title", String.valueOf( site_blog_title ) );
    _flag.put("site.blog.title",true);
  }
  
  /**
   *@param site_blog_url comment:日志url
   */
  public void SetKey_site_blog_url( String  site_blog_url){
    
    if(!CheckUrl(site_blog_url )){
    	return;
    }
    
    _data.put("site.blog.url", String.valueOf( site_blog_url ) );
    _flag.put("site.blog.url",true);
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
			  FeedCreatorAdapter.getInstance().Create(stype, version, _data);
			}else{
			  FeedCreatorAdapter.getInstance().CreateWithReply(stype, version, _data, reply);
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
