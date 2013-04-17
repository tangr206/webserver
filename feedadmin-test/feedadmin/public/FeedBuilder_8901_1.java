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
 * 此FeedBuilder_8901_1用于构建发送stype为8901，数据版本为1的新鲜事
 * 新鲜事说明：车问提问新鲜事
 * @author antonio
 *
 */

class FeedBuilder_8901_1 {
	/**新鲜事的类型*/
	public final static int stype = 8901;
	/**新鲜事的版本号*/
	public final static int version = 1;

	
  
  private Map<String,String> _data = new HashMap<String,String>();
  private Map<String,Boolean> _flag = new HashMap<String, Boolean>();
  public FeedBuilder_8901_1 () {
    
        _flag.put("time" , false);
        _flag.put("from.id" , false);
        _flag.put("from.name" , false);
        _flag.put("from.url" , false);
        _flag.put("from.tinyimg" , false);
        _flag.put("question.id" , false);
        _flag.put("question.title" , false);
        _flag.put("question.desc" , false);
        _flag.put("question.img" , false);
        _flag.put("question.url" , false);

    

    
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
   *@param time comment:发送时间
   */
  public void SetKey_time( long  time){
    
    _data.put("time", String.valueOf( time ) );
    _flag.put("time",true);
  }
  
  /**
   *@param from_id comment:新鲜事触发者id
   */
  public void SetKey_from_id( long  from_id){
    
    _data.put("from.id", String.valueOf( from_id ) );
    _flag.put("from.id",true);
  }
  
  /**
   *@param from_name comment:新鲜事触发者姓名
   */
  public void SetKey_from_name( String  from_name){
    
    _data.put("from.name", String.valueOf( from_name ) );
    _flag.put("from.name",true);
  }
  
  /**
   *@param from_url comment:新鲜事触发者链接
   */
  public void SetKey_from_url( String  from_url){
    
    if(!CheckUrl(from_url )){
    	_flag.put("from.url",false);
    	return;
    }
    
    _data.put("from.url", String.valueOf( from_url ) );
    _flag.put("from.url",true);
  }
  
  /**
   *@param from_tinyimg comment:新鲜事触发者头像相对路径
   */
  public void SetKey_from_tinyimg( String  from_tinyimg){
    
    _data.put("from.tinyimg", String.valueOf( from_tinyimg ) );
    _flag.put("from.tinyimg",true);
  }
  
  /**
   *@param question_id comment:问题id
   */
  public void SetKey_question_id( long  question_id){
    
    _data.put("question.id", String.valueOf( question_id ) );
    _flag.put("question.id",true);
  }
  
  /**
   *@param question_title comment:问题标题
   */
  public void SetKey_question_title( String  question_title){
    
    _data.put("question.title", String.valueOf( question_title ) );
    _flag.put("question.title",true);
  }
  
  /**
   *@param question_desc comment:问题描述
   */
  public void SetKey_question_desc( String  question_desc){
    
    _data.put("question.desc", String.valueOf( question_desc ) );
    _flag.put("question.desc",true);
  }
  
  /**
   *@param question_img comment:问题所属类型图片
   */
  public void SetKey_question_img( String  question_img){
    
    _data.put("question.img", String.valueOf( question_img ) );
    _flag.put("question.img",true);
  }
  
  /**
   *@param question_url comment:问题的链接
   */
  public void SetKey_question_url( String  question_url){
    
    if(!CheckUrl(question_url )){
    	_flag.put("question.url",false);
    	return;
    }
    
    _data.put("question.url", String.valueOf( question_url ) );
    _flag.put("question.url",true);
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
