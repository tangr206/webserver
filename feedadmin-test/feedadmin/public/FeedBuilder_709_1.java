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
 * 此FeedBuilder_709_1用于构建发送stype为709，数据版本为1的新鲜事
 * 新鲜事说明：上传多张照片
 * @author antonio
 *
 */

class FeedBuilder_709_1 {
	/**新鲜事的类型*/
	public final static int stype = 709;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
    private List< Map<String,String> > album_photo_list = new ArrayList< Map<String,String> >();
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  public FeedBuilder_709_1 () {
    
        _flag.put("origin.url" , false);
        _flag.put("origin.title" , false);
        _flag.put("time" , false);
        _flag.put("from.id" , false);
        _flag.put("from.name" , false);
        _flag.put("from.tinyimg" , false);
        _flag.put("from.certify" , false);
        _flag.put("from.certifyIcon" , false);
        _flag.put("from.certifyTitle" , false);
        _flag.put("from.url" , false);
        _flag.put("album.id" , false);
        _flag.put("album.title" , false);
        _flag.put("album.digest" , false);
        _flag.put("album.url" , false);
        _flag.put("album.count" , false);
        _flag.put("minigroup.name" , false);
        _flag.put("minigroup.url" , false);

    
        _flag.put("album.photo" , false);

    
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
   *@param time comment:时间戳(毫秒数)
   */
  public void SetKey_time( long  time){
    
    _data.put("time", String.valueOf( time ) );
    _flag.put("time",true);
  }
  
  /**
   *@param from_id comment:照片上传者id
   */
  public void SetKey_from_id( long  from_id){
    
    _data.put("from.id", String.valueOf( from_id ) );
    _flag.put("from.id",true);
  }
  
  /**
   *@param from_name comment:照片上传者name
   */
  public void SetKey_from_name( String  from_name){
    
    _data.put("from.name", String.valueOf( from_name ) );
    _flag.put("from.name",true);
  }
  
  /**
   *@param from_tinyimg comment:照片上传者小头像
   */
  public void SetKey_from_tinyimg( String  from_tinyimg){
    
    _data.put("from.tinyimg", String.valueOf( from_tinyimg ) );
    _flag.put("from.tinyimg",true);
  }
  
  /**
   *@param from_certify comment:照片上传者认证
   */
  public void SetKey_from_certify( String  from_certify){
    
    _data.put("from.certify", String.valueOf( from_certify ) );
    _flag.put("from.certify",true);
  }
  
  /**
   *@param from_certifyIcon comment:照片上传者图标
   */
  public void SetKey_from_certifyIcon( String  from_certifyIcon){
    
    _data.put("from.certifyIcon", String.valueOf( from_certifyIcon ) );
    _flag.put("from.certifyIcon",true);
  }
  
  /**
   *@param from_certifyTitle comment:照片上传者标题
   */
  public void SetKey_from_certifyTitle( String  from_certifyTitle){
    
    _data.put("from.certifyTitle", String.valueOf( from_certifyTitle ) );
    _flag.put("from.certifyTitle",true);
  }
  
  /**
   *@param from_url comment:照片上传者主页url
   */
  public void SetKey_from_url( String  from_url){
    
    if(!CheckUrl(from_url )){
    	return;
    }
    
    _data.put("from.url", String.valueOf( from_url ) );
    _flag.put("from.url",true);
  }
  
  /**
   *@param album_id comment:相册id
   */
  public void SetKey_album_id( long  album_id){
    
    _data.put("album.id", String.valueOf( album_id ) );
    _flag.put("album.id",true);
  }
  
  /**
   *@param album_title comment:相册标题
   */
  public void SetKey_album_title( String  album_title){
    
    _data.put("album.title", String.valueOf( album_title ) );
    _flag.put("album.title",true);
  }
  
  /**
   *@param album_digest comment:相册摘要描述
   */
  public void SetKey_album_digest( String  album_digest){
    
    _data.put("album.digest", String.valueOf( album_digest ) );
    _flag.put("album.digest",true);
  }
  
  /**
   *@param album_url comment:相册url
   */
  public void SetKey_album_url( String  album_url){
    
    if(!CheckUrl(album_url )){
    	return;
    }
    
    _data.put("album.url", String.valueOf( album_url ) );
    _flag.put("album.url",true);
  }
  
  /**
   *@param album_count comment:照片数
   */
  public void SetKey_album_count( long  album_count){
    
    _data.put("album.count", String.valueOf( album_count ) );
    _flag.put("album.count",true);
  }
  
  /**
   *@param minigroup_name comment:小群组名称
   */
  public void SetKey_minigroup_name( String  minigroup_name){
    
    _data.put("minigroup.name", String.valueOf( minigroup_name ) );
    _flag.put("minigroup.name",true);
  }
  
  /**
   *@param minigroup_url comment:小群组url
   */
  public void SetKey_minigroup_url( String  minigroup_url){
    
    if(!CheckUrl(minigroup_url )){
    	return;
    }
    
    _data.put("minigroup.url", String.valueOf( minigroup_url ) );
    _flag.put("minigroup.url",true);
  }
  

  
  /**
   *@param album_photo comment:照片信息
   */
  public void AddRepeat_album_photo(
    
	
	
		
	
		
	
		
	
		
          		
			 
			 long   
			id
		
	
		
          		, 
			 String 
			  
			image
		
	
		
          		, 
			 String 
			  
			bigImage
		
	
		
          		, 
			 String 
			  
			url
		
	
		
          		, 
			 String 
			  
			desc
		
	
		
          		, 
			 String 
			  
			descfull
		
	
    
  ){
    
        
                
        
                
        
                
        
                
                        
                
        
                
                         if(!CheckUrl(image)){return;}
                        
                
        
                
                         if(!CheckUrl(bigImage)){return;}
                        
                
        
                
                         if(!CheckUrl(url)){return;}
                        
                
        
                
                        
                
        
                
                        
                
        
         



      int count = album_photo_list.size();
      Map<String,String> obj = new HashMap<String,String>();
     
      
          obj.put("album.photo."+String.valueOf(count)+".id", String.valueOf(id ));
          obj.put("album.photo."+String.valueOf(count)+".image", String.valueOf(image ));
          obj.put("album.photo."+String.valueOf(count)+".bigImage", String.valueOf(bigImage ));
          obj.put("album.photo."+String.valueOf(count)+".url", String.valueOf(url ));
          obj.put("album.photo."+String.valueOf(count)+".desc", String.valueOf(desc ));
          obj.put("album.photo."+String.valueOf(count)+".descfull", String.valueOf(descfull ));
     
      album_photo_list.add(obj);
     _flag.put("album.photo",true);
  }
  
  

  
  void MergeData(){
    
      for(int i = 0; i < album_photo_list.size(); ++i){
        _data.putAll(album_photo_list.get(i));
      }
    
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
