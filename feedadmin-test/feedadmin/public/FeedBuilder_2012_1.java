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
 * 此FeedBuilder_2012_1用于构建发送stype为2012，数据版本为1的新鲜事
 * 新鲜事说明：Page发表日志
 * @author antonio
 *
 */

class FeedBuilder_2012_1 {
	/**新鲜事的类型*/
	public final static int stype = 2012;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
    private List< Map<String,String> > blog_deny_id_list = new ArrayList< Map<String,String> >();
  
    private List< Map<String,String> > blog_allow_id_list = new ArrayList< Map<String,String> >();
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  private Map<String,String> _config = new HashMap<String, String>();
  public FeedBuilder_2012_1 () {
    
        _flag.put("time" , false);
        _flag.put("from.id" , false);
        _flag.put("from.name" , false);
        _flag.put("from.tinyimg" , false);
        _flag.put("from.certify" , true);
        _flag.put("from.certifyIcon" , true);
        _flag.put("from.certifyTitle" , true);
        _flag.put("from.url" , true);
        _flag.put("origin.type" , true);
        _flag.put("origin.url" , true);
        _flag.put("origin.title" , true);
        _flag.put("blog.id" , false);
        _flag.put("blog.type" , true);
        _flag.put("blog.title" , false);
        _flag.put("blog.digest" , true);
        _flag.put("blog.url" , false);
        _flag.put("blog.video.image" , true);
        _flag.put("blog.photo.image" , true);
        _flag.put("blog.music" , true);
        _flag.put("blog.tags" , true);
        _flag.put("action" , true);
        _flag.put("stat.id" , true);
        _flag.put("stat.level" , true);

    
        _flag.put("blog.deny.id" , true);
        _flag.put("blog.allow.id" , true);

    
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
   *@param from_id comment:日志发布者的Id
   */
  public void SetKey_from_id( long  from_id){
    
    _data.put("from.id", String.valueOf( from_id ) );
    _flag.put("from.id",true);
  }
  
  /**
   *@param from_name comment:日志发布者的Name
   */
  public void SetKey_from_name( String  from_name){
    
    _data.put("from.name", String.valueOf( from_name ) );
    _flag.put("from.name",true);
  }
  
  /**
   *@param from_tinyimg comment:日志发布者的小图像
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
   *@param from_certify comment:日志发布者的认证
   */
  public void SetKey_from_certify( String  from_certify){
    
    _data.put("from.certify", String.valueOf( from_certify ) );
    _flag.put("from.certify",true);
  }
  
  /**
   *@param from_certifyIcon comment:日志发布者的认证图标
   */
  public void SetKey_from_certifyIcon( String  from_certifyIcon){
    
    if(!CheckUrl(from_certifyIcon )){
    	_flag.put("from.certifyIcon",false);
    	return;
    }
    
    _data.put("from.certifyIcon", String.valueOf( from_certifyIcon ) );
    _flag.put("from.certifyIcon",true);
  }
  
  /**
   *@param from_certifyTitle comment:日志发布者的认证头衔
   */
  public void SetKey_from_certifyTitle( String  from_certifyTitle){
    
    _data.put("from.certifyTitle", String.valueOf( from_certifyTitle ) );
    _flag.put("from.certifyTitle",true);
  }
  
  /**
   *@param from_url comment:日志发布者的主页
   */
  public void SetKey_from_url( String  from_url){
    
    _data.put("from.url", String.valueOf( from_url ) );
    _flag.put("from.url",true);
  }
  
  /**
   *@param origin_type comment:来源类型
   */
  public void SetKey_origin_type( String  origin_type){
    
    _data.put("origin.type", String.valueOf( origin_type ) );
    _flag.put("origin.type",true);
  }
  
  /**
   *@param origin_url comment:来源链接
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
   *@param origin_title comment:来源标题
   */
  public void SetKey_origin_title( String  origin_title){
    
    _data.put("origin.title", String.valueOf( origin_title ) );
    _flag.put("origin.title",true);
  }
  
  /**
   *@param blog_id comment:日志id
   */
  public void SetKey_blog_id( long  blog_id){
    
    _data.put("blog.id", String.valueOf( blog_id ) );
    _flag.put("blog.id",true);
  }
  
  /**
   *@param blog_type comment:日志类型
   */
  public void SetKey_blog_type( String  blog_type){
    
    _data.put("blog.type", String.valueOf( blog_type ) );
    _flag.put("blog.type",true);
  }
  
  /**
   *@param blog_title comment:日志标题
   */
  public void SetKey_blog_title( String  blog_title){
    
    _data.put("blog.title", String.valueOf( blog_title ) );
    _flag.put("blog.title",true);
  }
  
  /**
   *@param blog_digest comment:日志描述
   */
  public void SetKey_blog_digest( String  blog_digest){
    
    _data.put("blog.digest", String.valueOf( blog_digest ) );
    _flag.put("blog.digest",true);
  }
  
  /**
   *@param blog_url comment:日志地址
   */
  public void SetKey_blog_url( String  blog_url){
    
    _data.put("blog.url", String.valueOf( blog_url ) );
    _flag.put("blog.url",true);
  }
  
  /**
   *@param blog_video_image comment:视频截图
   */
  public void SetKey_blog_video_image( String  blog_video_image){
    
    _data.put("blog.video.image", String.valueOf( blog_video_image ) );
    _flag.put("blog.video.image",true);
  }
  
  /**
   *@param blog_photo_image comment:照片地址
   */
  public void SetKey_blog_photo_image( String  blog_photo_image){
    
    _data.put("blog.photo.image", String.valueOf( blog_photo_image ) );
    _flag.put("blog.photo.image",true);
  }
  
  /**
   *@param blog_music comment:音乐地址
   */
  public void SetKey_blog_music( String  blog_music){
    
    if(!CheckUrl(blog_music )){
    	_flag.put("blog.music",false);
    	return;
    }
    
    _data.put("blog.music", String.valueOf( blog_music ) );
    _flag.put("blog.music",true);
  }
  
  /**
   *@param blog_tags comment:tags
   */
  public void SetKey_blog_tags( String  blog_tags){
    
    _data.put("blog.tags", String.valueOf( blog_tags ) );
    _flag.put("blog.tags",true);
  }
  
  /**
   *@param action comment:action
   */
  public void SetKey_action( String  action){
    
    _data.put("action", String.valueOf( action ) );
    _flag.put("action",true);
  }
  
  /**
   *@param stat_id comment:传播id
   */
  public void SetKey_stat_id( String  stat_id){
    
    _data.put("stat.id", String.valueOf( stat_id ) );
    _flag.put("stat.id",true);
  }
  
  /**
   *@param stat_level comment:传播等级
   */
  public void SetKey_stat_level( long  stat_level){
    
    _data.put("stat.level", String.valueOf( stat_level ) );
    _flag.put("stat.level",true);
  }
  

  
  /**
   *@param blog_deny_id comment:?
   */
  public void AddRepeat_blog_deny_id(
    
	 long  
	blog_deny_id
    
  ){
    _flag.put("blog.deny.id",false);
    
        
         



      int count = blog_deny_id_list.size();
      Map<String,String> obj = new HashMap<String,String>();
     
      obj.put("blog.deny.id."+ String.valueOf(count),String.valueOf(blog_deny_id));
      blog_deny_id_list.add(obj);
     _flag.put("blog.deny.id",true);
  }
  
  /**
   *@param blog_allow_id comment:?
   */
  public void AddRepeat_blog_allow_id(
    
	 long  
	blog_allow_id
    
  ){
    _flag.put("blog.allow.id",false);
    
        
         



      int count = blog_allow_id_list.size();
      Map<String,String> obj = new HashMap<String,String>();
     
      obj.put("blog.allow.id."+ String.valueOf(count),String.valueOf(blog_allow_id));
      blog_allow_id_list.add(obj);
     _flag.put("blog.allow.id",true);
  }
  
  

  
  void MergeData(){
    
      for(int i = 0; i < blog_deny_id_list.size(); ++i){
        _data.putAll(blog_deny_id_list.get(i));
      }
    
      for(int i = 0; i < blog_allow_id_list.size(); ++i){
        _data.putAll(blog_allow_id_list.get(i));
      }
    
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
  	
		MergeData();
	
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
