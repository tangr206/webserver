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
 * 此FeedBuilder_8601_1用于构建发送stype为8601，数据版本为1的新鲜事
 * 新鲜事说明：人人爱听，用户正在收听某首歌产生的新鲜事
 * @author antonio
 *
 */

class FeedBuilder_8601_1 {
	/**新鲜事的类型*/
	public final static int stype = 8601;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
    private List< Map<String,String> > listener_list = new ArrayList< Map<String,String> >();
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  public FeedBuilder_8601_1 () {
    
        _flag.put("time" , false);
        _flag.put("from.id" , false);
        _flag.put("from.name" , false);
        _flag.put("from.tinyimg" , false);
        _flag.put("from.icon" , false);
        _flag.put("music.name" , false);
        _flag.put("music.url" , false);
        _flag.put("music.desc" , false);
        _flag.put("music.id" , false);
        _flag.put("music.img" , false);
        _flag.put("music.singer" , false);
        _flag.put("box.url" , false);
        _flag.put("button.url" , false);

    
        _flag.put("listener" , false);

    
  }

  boolean CheckUrl(String url) {
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
   *@param from_id comment:触发者id
   */
  public void SetKey_from_id( long  from_id){
    
    _data.put("from.id", String.valueOf( from_id ) );
    _flag.put("from.id",true);
  }
  
  /**
   *@param from_name comment:触发者name
   */
  public void SetKey_from_name( String  from_name){
    
    _data.put("from.name", String.valueOf( from_name ) );
    _flag.put("from.name",true);
  }
  
  /**
   *@param from_tinyimg comment:触发者头像
   */
  public void SetKey_from_tinyimg( String  from_tinyimg){
    
    _data.put("from.tinyimg", String.valueOf( from_tinyimg ) );
    _flag.put("from.tinyimg",true);
  }
  
  /**
   *@param from_icon comment:触发者图标
   */
  public void SetKey_from_icon( String  from_icon){
    
    _data.put("from.icon", String.valueOf( from_icon ) );
    _flag.put("from.icon",true);
  }
  
  /**
   *@param music_name comment:音乐名称
   */
  public void SetKey_music_name( String  music_name){
    
    _data.put("music.name", String.valueOf( music_name ) );
    _flag.put("music.name",true);
  }
  
  /**
   *@param music_url comment:音乐url地址
   */
  public void SetKey_music_url( String  music_url){
    
    if(!CheckUrl(music_url )){
    	return;
    }
    
    _data.put("music.url", String.valueOf( music_url ) );
    _flag.put("music.url",true);
  }
  
  /**
   *@param music_desc comment:描述信息
   */
  public void SetKey_music_desc( String  music_desc){
    
    _data.put("music.desc", String.valueOf( music_desc ) );
    _flag.put("music.desc",true);
  }
  
  /**
   *@param music_id comment:音乐id
   */
  public void SetKey_music_id( long  music_id){
    
    _data.put("music.id", String.valueOf( music_id ) );
    _flag.put("music.id",true);
  }
  
  /**
   *@param music_img comment:图片
   */
  public void SetKey_music_img( String  music_img){
    
    _data.put("music.img", String.valueOf( music_img ) );
    _flag.put("music.img",true);
  }
  
  /**
   *@param music_singer comment:歌手名称
   */
  public void SetKey_music_singer( String  music_singer){
    
    _data.put("music.singer", String.valueOf( music_singer ) );
    _flag.put("music.singer",true);
  }
  
  /**
   *@param box_url comment:音乐盒url
   */
  public void SetKey_box_url( String  box_url){
    
    if(!CheckUrl(box_url )){
    	return;
    }
    
    _data.put("box.url", String.valueOf( box_url ) );
    _flag.put("box.url",true);
  }
  
  /**
   *@param button_url comment:按钮url
   */
  public void SetKey_button_url( String  button_url){
    
    if(!CheckUrl(button_url )){
    	return;
    }
    
    _data.put("button.url", String.valueOf( button_url ) );
    _flag.put("button.url",true);
  }
  

  
  /**
   *@param listener comment:收听人
   */
  public void AddRepeat_listener(
    
	
	
		
          		
			 
			 String 
			  
			name
		
	
		
	
		
	
		
          		, 
			 long   
			id
		
	
		
          		, 
			 String 
			  
			url
		
	
    
  ){
    
        
                
                        
                
        
                
        
                
        
                
                        
                
        
                
                         if(!CheckUrl(url)){return;}
                        
                
        
         



      int count = listener_list.size();
      Map<String,String> obj = new HashMap<String,String>();
     
      
          obj.put("listener."+String.valueOf(count)+".name", String.valueOf(name ));
          obj.put("listener."+String.valueOf(count)+".id", String.valueOf(id ));
          obj.put("listener."+String.valueOf(count)+".url", String.valueOf(url ));
     
      listener_list.add(obj);
     _flag.put("listener",true);
  }
  
  

  
  void MergeData(){
    
      for(int i = 0; i < listener_list.size(); ++i){
        _data.putAll(listener_list.get(i));
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
