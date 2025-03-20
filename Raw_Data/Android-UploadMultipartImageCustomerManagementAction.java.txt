package com.zs.action;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;

import javax.servlet.http.HttpServletResponse;

import net.sf.json.JSONObject;

import org.apache.struts2.ServletActionContext;
import org.omg.CORBA.Request;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import org.apache.struts2.convention.annotation.Action;
import org.apache.struts2.convention.annotation.Result;
import org.apache.struts2.convention.annotation.Results;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;

import com.opensymphony.xwork2.ActionContext;
import com.opensymphony.xwork2.ActionSupport;
import com.zs.service.CustomerService;
@Controller
@Results({  
	  @Result(name="input", location="login/Login.jsp"),
	  @Result(name="succ", location="login/Welcome.jsp")
	}) 
	
public class CustomerManagementAction extends ActionSupport{

	@Resource(name="CustomerServiceImple")
	private CustomerService customerService;
	
	@Action("/cusFee")
	public void cusFee() throws IOException{
	HttpServletRequest request=ServletActionContext.getRequest();
	request.setCharacterEncoding("UTF-8");
	String data= request.getParameter("data");
	
	JSONObject  dataJson=new JSONObject();
	String cardId = dataJson.fromObject(data).get("cardId").toString();
	//String cardId =request.getParameter("cardId");
	String startDate=dataJson.fromObject(data).get("startDate").toString();
	String endDate=dataJson.fromObject(data).get("endDate").toString();
	String pageNum=dataJson.fromObject(data).get("pageNum").toString();
	String pageSize=dataJson.fromObject(data).get("pageSize").toString();
	
	String result=customerService.acquireCusFee(cardId, startDate, endDate, pageNum, pageSize);
	HttpServletResponse response = ServletActionContext.getResponse(); 
	//response.setContentType("text/html"); //火狐浏览器必须加上这句  
	response.setContentType("text/json");
    response.setCharacterEncoding("UTF-8");        
    response.getWriter().write(result);   
	}
	@Action("/cusPhyexam")
	public void cusPhyexam() throws IOException{
		HttpServletRequest request=ServletActionContext.getRequest();
		request.setCharacterEncoding("UTF-8");
		String data= request.getParameter("data");
		
		JSONObject  dataJson=new JSONObject();
		String cardId = dataJson.fromObject(data).get("cardId").toString();
		//String cardId =request.getParameter("cardId");
		String startDate=dataJson.fromObject(data).get("examStartDate").toString();
		String endDate=dataJson.fromObject(data).get("examEndDate").toString();
		String pageNum=dataJson.fromObject(data).get("pageNum").toString();
		String pageSize=dataJson.fromObject(data).get("pageSize").toString();
      /**			
		String cardId =request.getParameter("cardId");
		String startDate=request.getParameter("examStartDate");
		String endDate=request.getParameter("examEndDate");
		String pageNum=request.getParameter("pageNum");
		String pageSize=request.getParameter("pageSize");
		*/
		
		String result=customerService.acquireCusphyExam(cardId, startDate, endDate, pageNum, pageSize);
		HttpServletResponse response = ServletActionContext.getResponse(); 
		//response.setContentType("text/html"); //火狐浏览器必须加上这句  
		response.setContentType("text/json");
	    response.setCharacterEncoding("UTF-8");        
	    response.getWriter().write(result);   
		}
	@Action("/cusnew")
	public void cusnew() throws IOException{
	
		//HttpServletRequest request=ServletActionContext.getRequest();
		//request.setCharacterEncoding("UTF-8");
		HttpServletResponse response = ServletActionContext.getResponse(); 
		//response.setContentType("text/html"); //火狐浏览器必须加上这句  
		response.setContentType("text/json");
	    response.setCharacterEncoding("UTF-8");        
	    response.getWriter().write(customerService.test());   
		
	}
}