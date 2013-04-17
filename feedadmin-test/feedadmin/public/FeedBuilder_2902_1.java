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
 * 此FeedBuilder_2902_1用于构建发送stype为2902，数据版本为1的新鲜事
 * 新鲜事说明：评论照片发送给照片主人好友
 * @author antonio
 *
 */

class FeedBuilder_2902_1 {
	/**新鲜事的类型*/
	public final static int stype = 2902;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  public FeedBuilder_2902_1 () {
    
        _flag.put("comment.id" , false);
        _flag.put("comment.time" , false);
        _flag.put("comment.body" , false);
        _flag.put("comment.im.body" , false);
        _flag.put("comment.origin.url" , false);
        _flag.put("comment.origin.title" , false);
        _flag.put("comment.from.id" , false);
        _flag.put("comment.from.name" , false);
        _flag.put("comment.from.tinyimg" , false);
        _flag.put("comment.raw" , false);

    

    
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
   *@param comment_id comment:评论id
   */
  public void SetKey_comment_id( long  comment_id){
    
    _data.put("comment.id", String.valueOf( comment_id ) );
    _flag.put("comment.id",true);
  }
  
  /**
   *@param comment_time comment:评论时间
   */
  public void SetKey_comment_time( String  comment_time){
    
    _data.put("comment.time", String.valueOf( comment_time ) );
    _flag.put("comment.time",true);
  }
  
  /**
   *@param comment_body comment:评论内容
   */
  public void SetKey_comment_body( String  comment_body){
    
    _data.put("comment.body", String.valueOf( comment_body ) );
    _flag.put("comment.body",true);
  }
  
  /**
   *@param comment_im_body comment:im body
   */
  public void SetKey_comment_im_body( String  comment_im_body){
    
    _data.put("comment.im.body", String.valueOf( comment_im_body ) );
    _flag.put("comment.im.body",true);
  }
  
  /**
   *@param comment_origin_url comment:源url
   */
  public void SetKey_comment_origin_url( String  comment_origin_url){
    
    _data.put("comment.origin.url", String.valueOf( comment_origin_url ) );
    _flag.put("comment.origin.url",true);
  }
  
  /**
   *@param comment_origin_title comment:源title
   */
  public void SetKey_comment_origin_title( String  comment_origin_title){
    
    _data.put("comment.origin.title", String.valueOf( comment_origin_title ) );
    _flag.put("comment.origin.title",true);
  }
  
  /**
   *@param comment_from_id comment:回复人id
   */
  public void SetKey_comment_from_id( long  comment_from_id){
    
    _data.put("comment.from.id", String.valueOf( comment_from_id ) );
    _flag.put("comment.from.id",true);
  }
  
  /**
   *@param comment_from_name comment:回复人name
   */
  public void SetKey_comment_from_name( String  comment_from_name){
    
    _data.put("comment.from.name", String.valueOf( comment_from_name ) );
    _flag.put("comment.from.name",true);
  }
  
  /**
   *@param comment_from_tinyimg comment:回复人小头像
   */
  public void SetKey_comment_from_tinyimg( String  comment_from_tinyimg){
    
    _data.put("comment.from.tinyimg", String.valueOf( comment_from_tinyimg ) );
    _flag.put("comment.from.tinyimg",true);
  }
  
  /**
   *@param comment_raw comment:最原始的评论内容
   */
  public void SetKey_comment_raw( String  comment_raw){
    
    _data.put("comment.raw", String.valueOf( comment_raw ) );
    _flag.put("comment.raw",true);
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
