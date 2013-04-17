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
 * 此FeedBuilder_9902_1用于构建发送stype为9902，数据版本为1的新鲜事
 * 新鲜事说明：新鲜事模板测试
 * @author antonio
 *
 */

class FeedBuilder_9902_1 {
	/**新鲜事的类型*/
	public final static int stype = 9902;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
    private List< Map<String,String> > entity_img_list = new ArrayList< Map<String,String> >();
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  private Map<String,String> _config = new HashMap<String, String>();
  public FeedBuilder_9902_1 () {
    
        _flag.put("time" , false);
        _flag.put("from.id" , false);
        _flag.put("from.name" , false);
        _flag.put("from.tinyimg" , false);
        _flag.put("from.url" , true);
        _flag.put("origin.title" , true);
        _flag.put("origin.url" , true);
        _flag.put("origin.image" , true);
        _flag.put("lbs.content" , true);
        _flag.put("lbs.url" , true);
        _flag.put("entity.id" , false);
        _flag.put("entity.title" , false);
        _flag.put("entity.body" , false);
        _flag.put("entity.url" , false);
        _flag.put("custom" , true);

    
        _flag.put("entity.img" , true);

    
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
   *@param time comment:新鲜事触发时间
   */
  public void SetKey_time( long  time){
    
    _data.put("time", String.valueOf( time ) );
    _flag.put("time",true);
  }
  
  /**
   *@param from_id comment:发起人的ID
   */
  public void SetKey_from_id( long  from_id){
    
    _data.put("from.id", String.valueOf( from_id ) );
    _flag.put("from.id",true);
  }
  
  /**
   *@param from_name comment:发起人的名字
   */
  public void SetKey_from_name( String  from_name){
    
    _data.put("from.name", String.valueOf( from_name ) );
    _flag.put("from.name",true);
  }
  
  /**
   *@param from_tinyimg comment:发起人的头像图片链接（绝对路径）
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
   *@param from_url comment:发起人的个人主页链接
   */
  public void SetKey_from_url( String  from_url){
    
    _data.put("from.url", String.valueOf( from_url ) );
    _flag.put("from.url",true);
  }
  
  /**
   *@param origin_title comment:来源名称
   */
  public void SetKey_origin_title( String  origin_title){
    
    _data.put("origin.title", String.valueOf( origin_title ) );
    _flag.put("origin.title",true);
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
   *@param origin_image comment:图片链接
   */
  public void SetKey_origin_image( String  origin_image){
    
    if(!CheckUrl(origin_image )){
    	_flag.put("origin.image",false);
    	return;
    }
    
    _data.put("origin.image", String.valueOf( origin_image ) );
    _flag.put("origin.image",true);
  }
  
  /**
   *@param lbs_content comment:lbs名称
   */
  public void SetKey_lbs_content( String  lbs_content){
    
    _data.put("lbs.content", String.valueOf( lbs_content ) );
    _flag.put("lbs.content",true);
  }
  
  /**
   *@param lbs_url comment:lbs跳转链接
   */
  public void SetKey_lbs_url( String  lbs_url){
    
    if(!CheckUrl(lbs_url )){
    	_flag.put("lbs.url",false);
    	return;
    }
    
    _data.put("lbs.url", String.valueOf( lbs_url ) );
    _flag.put("lbs.url",true);
  }
  
  /**
   *@param entity_id comment:业务id
   */
  public void SetKey_entity_id( long  entity_id){
    
    _data.put("entity.id", String.valueOf( entity_id ) );
    _flag.put("entity.id",true);
  }
  
  /**
   *@param entity_title comment:业务标题
   */
  public void SetKey_entity_title( String  entity_title){
    
    _data.put("entity.title", String.valueOf( entity_title ) );
    _flag.put("entity.title",true);
  }
  
  /**
   *@param entity_body comment:业务内容
   */
  public void SetKey_entity_body( String  entity_body){
    
    _data.put("entity.body", String.valueOf( entity_body ) );
    _flag.put("entity.body",true);
  }
  
  /**
   *@param entity_url comment:业务终端页链接
   */
  public void SetKey_entity_url( String  entity_url){
    
    if(!CheckUrl(entity_url )){
    	_flag.put("entity.url",false);
    	return;
    }
    
    _data.put("entity.url", String.valueOf( entity_url ) );
    _flag.put("entity.url",true);
  }
  
  /**
   *@param custom comment:业务自定义信息，请在此节点下定义
   */
  public void SetKey_custom( String  custom){
    
    _data.put("custom", String.valueOf( custom ) );
    _flag.put("custom",true);
  }
  

  
  /**
   *@param entity_img comment:业务图片信息
   */
  public void AddRepeat_entity_img(
    
	
	
		
	
		
	
		
	
		
	
		
          		
			 
			 String 
			  
			src
		
	
		
          		, 
			 String 
			  
			url
		
	
		
          		, 
			 long   
			id
		
	
    
  ){
    _flag.put("entity.img",false);
    
        
                
        
                
        
                
        
                
        
                
                         if(!CheckUrl(src)){return;}
                        
                
        
                
                         if(!CheckUrl(url)){return;}
                        
                
        
                
                        
                
        
         



      int count = entity_img_list.size();
      Map<String,String> obj = new HashMap<String,String>();
     
      
          obj.put("entity.img."+String.valueOf(count)+".src", String.valueOf(src ));
          obj.put("entity.img."+String.valueOf(count)+".url", String.valueOf(url ));
          obj.put("entity.img."+String.valueOf(count)+".id", String.valueOf(id ));
     
      entity_img_list.add(obj);
     _flag.put("entity.img",true);
  }
  
  

  
  void MergeData(){
    
      for(int i = 0; i < entity_img_list.size(); ++i){
        _data.putAll(entity_img_list.get(i));
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
