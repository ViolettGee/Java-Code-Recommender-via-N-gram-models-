package com.zs.service.impl;


import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.zs.dao.CustomerManageDao;
import com.zs.po.ExamData;
import com.zs.po.ExamManagement;
import com.zs.po.FeeData;
import com.zs.po.FeeManagement;
import com.zs.po.PhysysCustomer;
import com.zs.service.CustomerService;
import com.zs.util.JsonBinder;
@Service("CustomerServiceImple")
public class CustomerServiceImple implements CustomerService{

   @Autowired  
	private CustomerManageDao customerManageDao;
	public String acquireCusFee(String cardId, String startDate,String endDate, String pageNum, String pagesize) {
		JsonBinder binder = JsonBinder.buildNonDefaultBinder(); 
		FeeManagement feeManagement=new FeeManagement();
		feeManagement=feeManagementdata(cardId, startDate, endDate, pageNum, pagesize);
		return binder.toJson(feeManagement);
	}

	public String acquireCusphyExam(String cardId, String startDate,String endDate, String pageNum, String pagesize) {
		JsonBinder binder = JsonBinder.buildNonDefaultBinder(); 
		ExamManagement examManagement=new ExamManagement();
		examManagement=examManagementdata(cardId, startDate, endDate, pageNum, pagesize);
		return binder.toJson(examManagement);
	}

	public FeeManagement feeManagementdata(String cardId, String startDate,String endDate, String pageNum, String pagesize){
		String success="false";
		String errMsg="";
		FeeManagement feeManagement=new FeeManagement();
		List<FeeData> list=customerManageDao.feeDatas(cardId, startDate, endDate, pageNum, pagesize);
		if(list.size()>0){
			success="true";
			errMsg="会员消费记录获取成功";
			feeManagement.setData(list);
		}
		else {
			errMsg="会员消费记录获取失败";
			feeManagement.setData(list);
		}
		feeManagement.setErrMsg(errMsg);
		feeManagement.setSuccess(success);
		return feeManagement;
	}
	public ExamManagement examManagementdata(String cardId, String startDate,String endDate, String pageNum, String pagesize){
	
		String success="false";
		String errMsg="";
		ExamManagement feeManagement=new ExamManagement();
		List<ExamData> list=customerManageDao.examDatas(cardId, startDate, endDate, pageNum, pagesize);
		if(list.size()>0){
			success="true";
			errMsg="会员体检记录获取成功";
			feeManagement.setData(list);
		}	
		else {
			errMsg="会员体检记录获取失败";
			feeManagement.setData(list);
		}
		feeManagement.setErrMsg(errMsg);
		feeManagement.setSuccess(success);
		return feeManagement;
	}
	//测试

	public String test(){
		
		JsonBinder binder = JsonBinder.buildNonDefaultBinder();
		return binder.toJson(binder.toJson(customerManageDao.newPhysysCustomer("2013-11-22 10:10:10").get(2)));
		
	}
	

}
