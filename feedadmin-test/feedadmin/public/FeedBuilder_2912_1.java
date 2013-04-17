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
 * 此FeedBuilder_2912_1用于构建发送stype为2912，数据版本为1的新鲜事
 * 新鲜事说明：评论相册发送给评论人好友（回复人）
 * @author antonio
 *
 */

class FeedBuilder_2912_1 {
	/**新鲜事的类型*/
	public final static int stype = 2912;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
    private List< Map<String,String> > site_tag_list = new ArrayList< Map<String,String> >();
  
    private List< Map<String,String> > album_photo_list = new ArrayList< Map<String,String> >();
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  public FeedBuilder_2912_1 () {
    
        _flag.put("time" , false);
        _flag.put("from.id" , false);
        _flag.put("from.name" , false);
        _flag.put("from.tinyimg" , false);
        _flag.put("from.url" , false);
        _flag.put("from.icon" , false);
        _flag.put("from.title" , false);
        _flag.put("origin.url" , false);
        _flag.put("origin.title" , false);
        _flag.put("comment.id" , false);
        _flag.put("comment.body" , false);
        _flag.put("comment.im.body" , false);
        _flag.put("comment.raw" , false);
        _flag.put("minigroup.name" , false);
        _flag.put("minigroup.url" , false);
        _flag.put("minigroup.id" , false);
        _flag.put("site.id" , false);
        _flag.put("site.url" , false);
        _flag.put("site.src" , false);
        _flag.put("site.mag.url" , false);
        _flag.put("site.mag.name" , false);
        _flag.put("site.mag.src" , false);
        _flag.put("album.id" , false);
        _flag.put("album.title" , false);
        _flag.put("album.digest" , false);
        _flag.put("album.url" , false);
        _flag.put("album.count" , false);
        _flag.put("album.owner.id" , false);
        _flag.put("album.owner.name" , false);
        _flag.put("album.owner.tinyimg" , false);

    
        _flag.put("site.tag" , false);
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
   *@param time comment:time
   */
  public void SetKey_time( String  time){
    
    _data.put("time", String.valueOf( time ) );
    _flag.put("time",true);
  }
  
  /**
   *@param from_id comment:id
   */
  public void SetKey_from_id( long  from_id){
    
    _data.put("from.id", String.valueOf( from_id ) );
    _flag.put("from.id",true);
  }
  
  /**
   *@param from_name comment:name
   */
  public void SetKey_from_name( String  from_name){
    
    _data.put("from.name", String.valueOf( from_name ) );
    _flag.put("from.name",true);
  }
  
  /**
   *@param from_tinyimg comment:tinyimg
   */
  public void SetKey_from_tinyimg( String  from_tinyimg){
    
    _data.put("from.tinyimg", String.valueOf( from_tinyimg ) );
    _flag.put("from.tinyimg",true);
  }
  
  /**
   *@param from_url comment:url
   */
  public void SetKey_from_url( String  from_url){
    
    if(!CheckUrl(from_url )){
    	return;
    }
    
    _data.put("from.url", String.valueOf( from_url ) );
    _flag.put("from.url",true);
  }
  
  /**
   *@param from_icon comment:certify_icon
   */
  public void SetKey_from_icon( String  from_icon){
    
    _data.put("from.icon", String.valueOf( from_icon ) );
    _flag.put("from.icon",true);
  }
  
  /**
   *@param from_title comment:certify_title
   */
  public void SetKey_from_title( String  from_title){
    
    _data.put("from.title", String.valueOf( from_title ) );
    _flag.put("from.title",true);
  }
  
  /**
   *@param origin_url comment:url
   */
  public void SetKey_origin_url( String  origin_url){
    
    if(!CheckUrl(origin_url )){
    	return;
    }
    
    _data.put("origin.url", String.valueOf( origin_url ) );
    _flag.put("origin.url",true);
  }
  
  /**
   *@param origin_title comment:title
   */
  public void SetKey_origin_title( String  origin_title){
    
    _data.put("origin.title", String.valueOf( origin_title ) );
    _flag.put("origin.title",true);
  }
  
  /**
   *@param comment_id comment:id
   */
  public void SetKey_comment_id( long  comment_id){
    
    _data.put("comment.id", String.valueOf( comment_id ) );
    _flag.put("comment.id",true);
  }
  
  /**
   *@param comment_body comment:body
   */
  public void SetKey_comment_body( String  comment_body){
    
    _data.put("comment.body", String.valueOf( comment_body ) );
    _flag.put("comment.body",true);
  }
  
  /**
   *@param comment_im_body comment:body
   */
  public void SetKey_comment_im_body( String  comment_im_body){
    
    _data.put("comment.im.body", String.valueOf( comment_im_body ) );
    _flag.put("comment.im.body",true);
  }
  
  /**
   *@param comment_raw comment:raw
   */
  public void SetKey_comment_raw( String  comment_raw){
    
    _data.put("comment.raw", String.valueOf( comment_raw ) );
    _flag.put("comment.raw",true);
  }
  
  /**
   *@param minigroup_name comment:name
   */
  public void SetKey_minigroup_name( String  minigroup_name){
    
    _data.put("minigroup.name", String.valueOf( minigroup_name ) );
    _flag.put("minigroup.name",true);
  }
  
  /**
   *@param minigroup_url comment:url
   */
  public void SetKey_minigroup_url( String  minigroup_url){
    
    if(!CheckUrl(minigroup_url )){
    	return;
    }
    
    _data.put("minigroup.url", String.valueOf( minigroup_url ) );
    _flag.put("minigroup.url",true);
  }
  
  /**
   *@param minigroup_id comment:id
   */
  public void SetKey_minigroup_id( String  minigroup_id){
    
    _data.put("minigroup.id", String.valueOf( minigroup_id ) );
    _flag.put("minigroup.id",true);
  }
  
  /**
   *@param site_id comment:id
   */
  public void SetKey_site_id( long  site_id){
    
    _data.put("site.id", String.valueOf( site_id ) );
    _flag.put("site.id",true);
  }
  
  /**
   *@param site_url comment:url
   */
  public void SetKey_site_url( String  site_url){
    
    if(!CheckUrl(site_url )){
    	return;
    }
    
    _data.put("site.url", String.valueOf( site_url ) );
    _flag.put("site.url",true);
  }
  
  /**
   *@param site_src comment:src
   */
  public void SetKey_site_src( String  site_src){
    
    _data.put("site.src", String.valueOf( site_src ) );
    _flag.put("site.src",true);
  }
  
  /**
   *@param site_mag_url comment:url
   */
  public void SetKey_site_mag_url( String  site_mag_url){
    
    if(!CheckUrl(site_mag_url )){
    	return;
    }
    
    _data.put("site.mag.url", String.valueOf( site_mag_url ) );
    _flag.put("site.mag.url",true);
  }
  
  /**
   *@param site_mag_name comment:name
   */
  public void SetKey_site_mag_name( String  site_mag_name){
    
    _data.put("site.mag.name", String.valueOf( site_mag_name ) );
    _flag.put("site.mag.name",true);
  }
  
  /**
   *@param site_mag_src comment:src
   */
  public void SetKey_site_mag_src( String  site_mag_src){
    
    _data.put("site.mag.src", String.valueOf( site_mag_src ) );
    _flag.put("site.mag.src",true);
  }
  
  /**
   *@param album_id comment:id
   */
  public void SetKey_album_id( String  album_id){
    
    _data.put("album.id", String.valueOf( album_id ) );
    _flag.put("album.id",true);
  }
  
  /**
   *@param album_title comment:title
   */
  public void SetKey_album_title( String  album_title){
    
    _data.put("album.title", String.valueOf( album_title ) );
    _flag.put("album.title",true);
  }
  
  /**
   *@param album_digest comment:digest
   */
  public void SetKey_album_digest( String  album_digest){
    
    _data.put("album.digest", String.valueOf( album_digest ) );
    _flag.put("album.digest",true);
  }
  
  /**
   *@param album_url comment:url
   */
  public void SetKey_album_url( String  album_url){
    
    _data.put("album.url", String.valueOf( album_url ) );
    _flag.put("album.url",true);
  }
  
  /**
   *@param album_count comment:count
   */
  public void SetKey_album_count( String  album_count){
    
    _data.put("album.count", String.valueOf( album_count ) );
    _flag.put("album.count",true);
  }
  
  /**
   *@param album_owner_id comment:id
   */
  public void SetKey_album_owner_id( long  album_owner_id){
    
    _data.put("album.owner.id", String.valueOf( album_owner_id ) );
    _flag.put("album.owner.id",true);
  }
  
  /**
   *@param album_owner_name comment:name
   */
  public void SetKey_album_owner_name( String  album_owner_name){
    
    _data.put("album.owner.name", String.valueOf( album_owner_name ) );
    _flag.put("album.owner.name",true);
  }
  
  /**
   *@param album_owner_tinyimg comment:tinyimg
   */
  public void SetKey_album_owner_tinyimg( String  album_owner_tinyimg){
    
    _data.put("album.owner.tinyimg", String.valueOf( album_owner_tinyimg ) );
    _flag.put("album.owner.tinyimg",true);
  }
  

  
  /**
   *@param site_tag comment:tag
   */
  public void AddRepeat_site_tag(
    
	
	
		
          		
			 
			 String 
			  
			name
		
	
		
	
		
	
		
          		, 
			 String 
			  
			url
		
	
    
  ){
    
        
                
                        
                
        
                
        
                
        
                
                         if(!CheckUrl(url)){return;}
                        
                
        
         



      int count = site_tag_list.size();
      Map<String,String> obj = new HashMap<String,String>();
     
      
          obj.put("site.tag."+String.valueOf(count)+".name", String.valueOf(name ));
          obj.put("site.tag."+String.valueOf(count)+".url", String.valueOf(url ));
     
      site_tag_list.add(obj);
     _flag.put("site.tag",true);
  }
  
  /**
   *@param album_photo comment:photo
   */
  public void AddRepeat_album_photo(
    
	
	
		
	
		
	
		
	
		
          		
			 
			 String 
			  
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
    
      for(int i = 0; i < site_tag_list.size(); ++i){
        _data.putAll(site_tag_list.get(i));
      }
    
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
