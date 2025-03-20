package com.zs.dao;

import java.sql.SQLException;
import java.util.List;

import javax.ejb.FinderException;

import com.zs.po.ExamData;
import com.zs.po.FeeData;
import com.zs.po.PhysysCustomer;

public interface CustomerManageDao {

	//查询会员消费记录
	public List<FeeData> feeDatas(String cardId,String startDate,String endDate,String pageNum,String pagesize);
	//查询会员体检记录
	public List<ExamData> examDatas (String cardId,String startDate,String endDate,String pageNum,String pagesize);
	//查询体检系统里面是否产生新会员
	public List<PhysysCustomer> newPhysysCustomer(String createtime);
	
}
