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
 * 此FeedBuilder_2907_1用于构建发送stype为2907，数据版本为1的新鲜事
 * 新鲜事说明：评论日志发送给评论人好友(直接回复UGC)
 * @author antonio
 *
 */

class FeedBuilder_2907_1 {
	/**新鲜事的类型*/
	public final static int stype = 2907;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
    private List< Map<String,String> > from_list = new ArrayList< Map<String,String> >();
  
    private List< Map<String,String> > comment_list = new ArrayList< Map<String,String> >();
  
    private List< Map<String,String> > site_tag_list = new ArrayList< Map<String,String> >();
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  public FeedBuilder_2907_1 () {
    
        _flag.put("time" , false);
        _flag.put("origin.url" , false);
        _flag.put("origin.title" , false);
        _flag.put("blog.id" , false);
        _flag.put("blog.title" , false);
        _flag.put("blog.digest" , false);
        _flag.put("blog.url" , false);
        _flag.put("blog.video.image" , false);
        _flag.put("blog.photo.image" , false);
        _flag.put("blog.music" , false);
        _flag.put("blog.type" , false);
        _flag.put("blog.owner.id" , false);
        _flag.put("blog.owner.name" , false);
        _flag.put("blog.owner.tinyimg" , false);
        _flag.put("action" , false);
        _flag.put("minigroup.name" , false);
        _flag.put("minigroup.url" , false);
        _flag.put("minigroup.id" , false);
        _flag.put("site.id" , false);
        _flag.put("site.url" , false);
        _flag.put("site.src" , false);
        _flag.put("site.mag.url" , false);
        _flag.put("site.mag.name" , false);
        _flag.put("site.mag.src" , false);
        _flag.put("sender" , false);

    
        _flag.put("from" , false);
        _flag.put("comment" , false);
        _flag.put("site.tag" , false);

    
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
   *@param blog_id comment:id
   */
  public void SetKey_blog_id( long  blog_id){
    
    _data.put("blog.id", String.valueOf( blog_id ) );
    _flag.put("blog.id",true);
  }
  
  /**
   *@param blog_title comment:title
   */
  public void SetKey_blog_title( String  blog_title){
    
    _data.put("blog.title", String.valueOf( blog_title ) );
    _flag.put("blog.title",true);
  }
  
  /**
   *@param blog_digest comment:digest
   */
  public void SetKey_blog_digest( String  blog_digest){
    
    _data.put("blog.digest", String.valueOf( blog_digest ) );
    _flag.put("blog.digest",true);
  }
  
  /**
   *@param blog_url comment:url
   */
  public void SetKey_blog_url( String  blog_url){
    
    _data.put("blog.url", String.valueOf( blog_url ) );
    _flag.put("blog.url",true);
  }
  
  /**
   *@param blog_video_image comment:image
   */
  public void SetKey_blog_video_image( String  blog_video_image){
    
    _data.put("blog.video.image", String.valueOf( blog_video_image ) );
    _flag.put("blog.video.image",true);
  }
  
  /**
   *@param blog_photo_image comment:image
   */
  public void SetKey_blog_photo_image( String  blog_photo_image){
    
    _data.put("blog.photo.image", String.valueOf( blog_photo_image ) );
    _flag.put("blog.photo.image",true);
  }
  
  /**
   *@param blog_music comment:music
   */
  public void SetKey_blog_music( String  blog_music){
    
    _data.put("blog.music", String.valueOf( blog_music ) );
    _flag.put("blog.music",true);
  }
  
  /**
   *@param blog_type comment:blogtype
   */
  public void SetKey_blog_type( String  blog_type){
    
    _data.put("blog.type", String.valueOf( blog_type ) );
    _flag.put("blog.type",true);
  }
  
  /**
   *@param blog_owner_id comment:id
   */
  public void SetKey_blog_owner_id( long  blog_owner_id){
    
    _data.put("blog.owner.id", String.valueOf( blog_owner_id ) );
    _flag.put("blog.owner.id",true);
  }
  
  /**
   *@param blog_owner_name comment:name
   */
  public void SetKey_blog_owner_name( String  blog_owner_name){
    
    _data.put("blog.owner.name", String.valueOf( blog_owner_name ) );
    _flag.put("blog.owner.name",true);
  }
  
  /**
   *@param blog_owner_tinyimg comment:tinyimg
   */
  public void SetKey_blog_owner_tinyimg( String  blog_owner_tinyimg){
    
    _data.put("blog.owner.tinyimg", String.valueOf( blog_owner_tinyimg ) );
    _flag.put("blog.owner.tinyimg",true);
  }
  
  /**
   *@param action comment:action
   */
  public void SetKey_action( String  action){
    
    _data.put("action", String.valueOf( action ) );
    _flag.put("action",true);
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
   *@param sender comment:sender
   */
  public void SetKey_sender( long  sender){
    
    _data.put("sender", String.valueOf( sender ) );
    _flag.put("sender",true);
  }
  

  
  /**
   *@param from comment:from
   */
  public void AddRepeat_from(
    
	
	
		
          		
			 
			 String 
			  
			name
		
	
		
	
		
	
		
          		, 
			 long   
			id
		
	
		
          		, 
			 String 
			  
			tinyimg
		
	
		
          		, 
			 String 
			  
			url
		
	
		
          		, 
			 String 
			  
			icon
		
	
		
          		, 
			 String 
			  
			title
		
	
    
  ){
    
        
                
                        
                
        
                
        
                
        
                
                        
                
        
                
                        
                
        
                
                         if(!CheckUrl(url)){return;}
                        
                
        
                
                        
                
        
                
                        
                
        
         



      int count = from_list.size();
      Map<String,String> obj = new HashMap<String,String>();
     
      
          obj.put("from."+String.valueOf(count)+".name", String.valueOf(name ));
          obj.put("from."+String.valueOf(count)+".id", String.valueOf(id ));
          obj.put("from."+String.valueOf(count)+".tinyimg", String.valueOf(tinyimg ));
          obj.put("from."+String.valueOf(count)+".url", String.valueOf(url ));
          obj.put("from."+String.valueOf(count)+".icon", String.valueOf(icon ));
          obj.put("from."+String.valueOf(count)+".title", String.valueOf(title ));
     
      from_list.add(obj);
     _flag.put("from",true);
  }
  
  /**
   *@param comment comment:comment
   */
  public void AddRepeat_comment(
    
	
	
		
	
		
	
		
	
		
          		
			 
			 long   
			id
		
	
		
          		, 
			 String 
			  
			body
		
	
		
          		, 
			 String 
			  
			im_body
		
	
		
          		, 
			 String 
			  
			raw
		
	
		
          		, 
			 long   
			cCount
		
	
		
          		, 
			 String 
			  
			time
		
	
    
  ){
    
        
                
        
                
        
                
        
                
                        
                
        
                
                        
                
        
                
                        
                
        
                
                        
                
        
                
                        
                
        
                
                        
                
        
         



      int count = comment_list.size();
      Map<String,String> obj = new HashMap<String,String>();
     
      
          obj.put("comment."+String.valueOf(count)+".id", String.valueOf(id ));
          obj.put("comment."+String.valueOf(count)+".body", String.valueOf(body ));
          obj.put("comment."+String.valueOf(count)+".im.body", String.valueOf(im_body ));
          obj.put("comment."+String.valueOf(count)+".raw", String.valueOf(raw ));
          obj.put("comment."+String.valueOf(count)+".cCount", String.valueOf(cCount ));
          obj.put("comment."+String.valueOf(count)+".time", String.valueOf(time ));
     
      comment_list.add(obj);
     _flag.put("comment",true);
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
  
  

  
  void MergeData(){
    
      for(int i = 0; i < from_list.size(); ++i){
        _data.putAll(from_list.get(i));
      }
    
      for(int i = 0; i < comment_list.size(); ++i){
        _data.putAll(comment_list.get(i));
      }
    
      for(int i = 0; i < site_tag_list.size(); ++i){
        _data.putAll(site_tag_list.get(i));
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
