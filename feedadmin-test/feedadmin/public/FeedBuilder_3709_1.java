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
 * 此FeedBuilder_3709_1用于构建发送stype为3709，数据版本为1的新鲜事
 * 新鲜事说明：小站转载日志
 * @author antonio
 *
 */

class FeedBuilder_3709_1 {
	/**新鲜事的类型*/
	public final static int stype = 3709;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
    private List< Map<String,String> > tag_list = new ArrayList< Map<String,String> >();
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  public FeedBuilder_3709_1 () {
    
        _flag.put("site.id" , false);
        _flag.put("site.url" , false);
        _flag.put("site.name" , false);
        _flag.put("site.tinyHeadSource" , false);
        _flag.put("site.profileUrl" , false);
        _flag.put("poster.id" , false);
        _flag.put("poster.name" , false);
        _flag.put("poster.tinyHeadSource" , false);
        _flag.put("poster.profileUrl" , false);
        _flag.put("preSite.id" , false);
        _flag.put("preSite.name" , false);
        _flag.put("preSite.url" , false);
        _flag.put("preSite.tinyHeadSource" , false);
        _flag.put("preSite.profileUrl" , false);
        _flag.put("entry.id" , false);
        _flag.put("entry.title" , false);
        _flag.put("entry.summary" , false);
        _flag.put("entry.thumbType" , false);
        _flag.put("entry.thumbSrc" , false);
        _flag.put("entry.url" , false);
        _flag.put("entry.time" , false);

    
        _flag.put("tag" , false);

    
	_flag.put("expr",false);
    
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

   
   public boolean AddExpr(String expr) {
		Pattern p = Pattern
				.compile("^[ufaApsvgzx]{1}\\([1-9]+[0-9]*\\)([\\+\\-\\&]{1}[ufaApsvgzx]{1}\\([1-9]+[0-9]*\\))*$");
		Matcher m = p.matcher(expr);
		if (m.find()) {
			_data.put("expr", expr);
			_flag.put("expr", true);
			return true;
		}
		System.err.println("分发表达式 expr="+expr+",设置的值无效");
		return false;
   }
   

  
  /**
   *@param site_id comment:id
   */
  public void SetKey_site_id( long  site_id){
    
    _data.put("site.id", String.valueOf( site_id ) );
    _flag.put("site.id",true);
  }
  
  /**
   *@param site_url comment:个性url
   */
  public void SetKey_site_url( String  site_url){
    
    _data.put("site.url", String.valueOf( site_url ) );
    _flag.put("site.url",true);
  }
  
  /**
   *@param site_name comment:名字
   */
  public void SetKey_site_name( String  site_name){
    
    _data.put("site.name", String.valueOf( site_name ) );
    _flag.put("site.name",true);
  }
  
  /**
   *@param site_tinyHeadSource comment:小头像地址
   */
  public void SetKey_site_tinyHeadSource( String  site_tinyHeadSource){
    
    if(!CheckUrl(site_tinyHeadSource )){
    	_flag.put("site.tinyHeadSource",false);
    	return;
    }
    
    _data.put("site.tinyHeadSource", String.valueOf( site_tinyHeadSource ) );
    _flag.put("site.tinyHeadSource",true);
  }
  
  /**
   *@param site_profileUrl comment:主页地址
   */
  public void SetKey_site_profileUrl( String  site_profileUrl){
    
    if(!CheckUrl(site_profileUrl )){
    	_flag.put("site.profileUrl",false);
    	return;
    }
    
    _data.put("site.profileUrl", String.valueOf( site_profileUrl ) );
    _flag.put("site.profileUrl",true);
  }
  
  /**
   *@param poster_id comment:id
   */
  public void SetKey_poster_id( long  poster_id){
    
    _data.put("poster.id", String.valueOf( poster_id ) );
    _flag.put("poster.id",true);
  }
  
  /**
   *@param poster_name comment:名字
   */
  public void SetKey_poster_name( String  poster_name){
    
    _data.put("poster.name", String.valueOf( poster_name ) );
    _flag.put("poster.name",true);
  }
  
  /**
   *@param poster_tinyHeadSource comment:小头像地址
   */
  public void SetKey_poster_tinyHeadSource( String  poster_tinyHeadSource){
    
    if(!CheckUrl(poster_tinyHeadSource )){
    	_flag.put("poster.tinyHeadSource",false);
    	return;
    }
    
    _data.put("poster.tinyHeadSource", String.valueOf( poster_tinyHeadSource ) );
    _flag.put("poster.tinyHeadSource",true);
  }
  
  /**
   *@param poster_profileUrl comment:主页地址
   */
  public void SetKey_poster_profileUrl( String  poster_profileUrl){
    
    if(!CheckUrl(poster_profileUrl )){
    	_flag.put("poster.profileUrl",false);
    	return;
    }
    
    _data.put("poster.profileUrl", String.valueOf( poster_profileUrl ) );
    _flag.put("poster.profileUrl",true);
  }
  
  /**
   *@param preSite_id comment:id
   */
  public void SetKey_preSite_id( long  preSite_id){
    
    _data.put("preSite.id", String.valueOf( preSite_id ) );
    _flag.put("preSite.id",true);
  }
  
  /**
   *@param preSite_name comment:名字
   */
  public void SetKey_preSite_name( String  preSite_name){
    
    _data.put("preSite.name", String.valueOf( preSite_name ) );
    _flag.put("preSite.name",true);
  }
  
  /**
   *@param preSite_url comment:个性url
   */
  public void SetKey_preSite_url( String  preSite_url){
    
    _data.put("preSite.url", String.valueOf( preSite_url ) );
    _flag.put("preSite.url",true);
  }
  
  /**
   *@param preSite_tinyHeadSource comment:小头像地址
   */
  public void SetKey_preSite_tinyHeadSource( String  preSite_tinyHeadSource){
    
    if(!CheckUrl(preSite_tinyHeadSource )){
    	_flag.put("preSite.tinyHeadSource",false);
    	return;
    }
    
    _data.put("preSite.tinyHeadSource", String.valueOf( preSite_tinyHeadSource ) );
    _flag.put("preSite.tinyHeadSource",true);
  }
  
  /**
   *@param preSite_profileUrl comment:主页地址
   */
  public void SetKey_preSite_profileUrl( String  preSite_profileUrl){
    
    _data.put("preSite.profileUrl", String.valueOf( preSite_profileUrl ) );
    _flag.put("preSite.profileUrl",true);
  }
  
  /**
   *@param entry_id comment:id
   */
  public void SetKey_entry_id( long  entry_id){
    
    _data.put("entry.id", String.valueOf( entry_id ) );
    _flag.put("entry.id",true);
  }
  
  /**
   *@param entry_title comment:标题
   */
  public void SetKey_entry_title( String  entry_title){
    
    _data.put("entry.title", String.valueOf( entry_title ) );
    _flag.put("entry.title",true);
  }
  
  /**
   *@param entry_summary comment:概览
   */
  public void SetKey_entry_summary( String  entry_summary){
    
    _data.put("entry.summary", String.valueOf( entry_summary ) );
    _flag.put("entry.summary",true);
  }
  
  /**
   *@param entry_thumbType comment:附加信息类型
   */
  public void SetKey_entry_thumbType( String  entry_thumbType){
    
    _data.put("entry.thumbType", String.valueOf( entry_thumbType ) );
    _flag.put("entry.thumbType",true);
  }
  
  /**
   *@param entry_thumbSrc comment:附加信息源地址
   */
  public void SetKey_entry_thumbSrc( String  entry_thumbSrc){
    
    if(!CheckUrl(entry_thumbSrc )){
    	_flag.put("entry.thumbSrc",false);
    	return;
    }
    
    _data.put("entry.thumbSrc", String.valueOf( entry_thumbSrc ) );
    _flag.put("entry.thumbSrc",true);
  }
  
  /**
   *@param entry_url comment:查看地址
   */
  public void SetKey_entry_url( String  entry_url){
    
    if(!CheckUrl(entry_url )){
    	_flag.put("entry.url",false);
    	return;
    }
    
    _data.put("entry.url", String.valueOf( entry_url ) );
    _flag.put("entry.url",true);
  }
  
  /**
   *@param entry_time comment:时间
   */
  public void SetKey_entry_time( long  entry_time){
    
    _data.put("entry.time", String.valueOf( entry_time ) );
    _flag.put("entry.time",true);
  }
  

  
  /**
   *@param tag comment:feed上的标签
   */
  public void AddRepeat_tag(
    
	
	
		
	
		
	
		
	
		
	
		
          		
			 
			 long   
			id
		
	
		
          		, 
			 String 
			  
			value
		
	
		
          		, 
			 String 
			  
			profileUrl
		
	
    
  ){
    _flag.put("tag",false);
    
        
                
        
                
        
                
        
                
        
                
                        
                
        
                
                        
                
        
                
                         if(!CheckUrl(profileUrl)){return;}
                        
                
        
         



      int count = tag_list.size();
      Map<String,String> obj = new HashMap<String,String>();
     
      
          obj.put("tag."+String.valueOf(count)+".id", String.valueOf(id ));
          obj.put("tag."+String.valueOf(count)+".value", String.valueOf(value ));
          obj.put("tag."+String.valueOf(count)+".profileUrl", String.valueOf(profileUrl ));
     
      tag_list.add(obj);
     _flag.put("tag",true);
  }
  
  

  
  void MergeData(){
    
      for(int i = 0; i < tag_list.size(); ++i){
        _data.putAll(tag_list.get(i));
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
