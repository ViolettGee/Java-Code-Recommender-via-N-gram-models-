package com.zs.service;

import java.util.List;

import com.zs.po.FeeData;

public interface CustomerService {

	//会员体检信息返回
	public String acquireCusphyExam(String cardId,String startDate,String endDate,String pageNum,String pagesize);
	//会员消费信息返回
	public String acquireCusFee(String cardId,String startDate,String endDate,String pageNum,String pagesize);
	//测试
	public String test();
	
}
