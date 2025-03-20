package com.zs.dao.impl;

import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.util.List;
import com.mysql.jdbc.MySQLConnection;
import com.zs.dao.CustomerManageDao;
import com.zs.po.ExamData;
import com.zs.po.FeeData;
import com.zs.po.PhysysCustomer;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import org.springframework.stereotype.Repository;


@Repository
public class CustomerManageDaoImple implements CustomerManageDao{

	/*public List<ExamData> examDatas(String cardId, String startDate,String endDate, String pageNum, String pagesize) {
		
		List<ExamData> list=new ArrayList<ExamData>();
		Connection conn=null;
		PreparedStatement st=null;
		ResultSet rs=null;
		try{
		conn = getconnertion();
		//查询一共多少条
        String hqlString="select count(*) as count from exam where cardId='"+cardId+"'";
        //查询具体结果
        String sql ="select examId,examName,examDate,content,fee from exam where cardId='"+cardId+"'";
        if(startDate!=null&&!"".equals(startDate)){
        	hqlString=hqlString+" and examDate >= '"+startDate+"'";
        	sql+=" and examDate >= '"+startDate+"'";
        }
        if(endDate!=null&&!"".equals(endDate)){
        	hqlString=hqlString+" and examDate <='"+endDate+"'";
        	sql=sql+" and examDate <= '"+endDate+"'";
        }
       
        st = conn.prepareStatement(hqlString);
        rs = st.executeQuery();
       
        int totalnum=0;
        while(rs.next()){
        	totalnum=rs.getInt(1);
        }
        System.out.print(totalnum+"abjkshdfhsalkjfhaslk");
        int totalpageNum=0;
        //pageNum,pageSize 转化为整数
        int i=0;
        int j=0;
        j=Integer.parseInt(pageNum);
        i=Integer.parseInt(pagesize);
        //判断页数是否合法
        //一共分多少页
        if (totalnum % i != 0) {
        	totalpageNum= totalnum  / i + 1;
		} else {
			totalpageNum= totalnum  / i;
		}
       
        if(j<=0||j>totalpageNum){
        	
   		return list;
        }
        else{
        	
        	 sql= sql+" order by examDate desc ";
        	 st=null;
        	 rs=null;
        	 st = conn.prepareStatement(sql);
             rs = st.executeQuery();
    
        	 int k=0;
             while (rs.next()){
             	if(k>=(j-1)*i&&k<j*i){
             	 ExamData data=new ExamData();
             	 data.setExamId(rs.getString(1));
             	 data.setExamName(rs.getString(2));
             	 data.setExamDate(rs.getString(3));
             	 data.setContent(rs.getString(4));
             	 data.setFee(rs.getString(5));
             	 list.add(data);
             	}
             	k++;
              }
        }
       
		}catch (Exception e) {
			 
			e.printStackTrace();
		}finally{
         try {
			 rs.close();
			 st.close();
	         conn.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        
		}
		return list;
		
	}
     */
	/*public List<FeeData> feeDatas(String cardId, String startDate,String endDate, String pageNum, String pagesize) {
		List<FeeData> list=new ArrayList<FeeData>();
		Connection conn=null;
		PreparedStatement st=null;
		ResultSet rs=null;
		try{
		conn = getconnertion();
		//查询一共多少条
        String hqlString="select count(*) as count from fee where cardId='"+cardId+"'";
        //查询具体结果
        String sql ="select feeId,feenName,feeDate,fee from fee where cardId='"+cardId+"'";
        if(startDate!=null&&!"".equals(startDate)){
        	hqlString=hqlString+" and feeDate >= '"+startDate+"'";
        	sql+=" and feeDate >= '"+startDate+"'";
        }
        if(endDate!=null&&!"".equals(endDate)){
        	hqlString=hqlString+" and feeDate <='"+endDate+"'";
        	sql=sql+" and feeDate <= '"+endDate+"'";
        }
       
        st = conn.prepareStatement(hqlString);
        rs = st.executeQuery();
       
        int totalnum=0;
        while(rs.next()){
        	totalnum=rs.getInt(1);
        }
        System.out.print(totalnum+"abjkshdfhsalkjfhaslk");
        int totalpageNum=0;
        //pageNum,pageSize 转化为整数
        int i=0;
        int j=0;
        j=Integer.parseInt(pageNum);
        i=Integer.parseInt(pagesize);
        //判断页数是否合法
        //一共分多少页
        if (totalnum % i != 0) {
        	totalpageNum= totalnum  / i + 1;
		} else {
			totalpageNum= totalnum  / i;
		}
       
        if(j<=0||j>totalpageNum){
        	
        	try {
   			 rs.close();
   			 st.close();
   	         conn.close();
   		} catch (SQLException e) {
   			// TODO Auto-generated catch block
   			e.printStackTrace();
   		}
   		return list;
        }
        else{
        	
        	 sql= sql+" order by feeDate desc ";
        	 st=null;
        	 rs=null;
        	 st = conn.prepareStatement(sql);
             rs = st.executeQuery();
    
        	 int k=0;
             while (rs.next()){
             	if(k>=(j-1)*i&&k<j*i){
             	 FeeData data=new FeeData();
             	 data.setFeeId(rs.getString(1));
             	 data.setFeeName(rs.getString(2));
             	 data.setFeeDate(rs.getString(3));
             	 data.setFee(rs.getString(4));
             	 list.add(data);
             	}
             	k++;
              }
        }
       
		}catch (Exception e) {
			 
			e.printStackTrace();
		}finally{
         try {
			 rs.close();
			 st.close();
	         conn.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        
		}
		return list;
		
	}*/

	public static Connection getConnection() {

        try {

            Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
            String url = "jdbc:sqlserver://10.37.48.182:1433;DatabaseName=HerPeisXYSMJKGLZX";
            String username = "sa";
            String password = "abcd-123";
            Connection conn = DriverManager.getConnection(url, username,password);
            return conn;

        } catch (Exception e) {
            throw new IllegalArgumentException(e);
        }
    }
	public static Connection getconnertion(){
		 try {

	            Class.forName("com.mysql.jdbc.Driver");
	            String url = "jdbc:mysql://10.37.48.181:3306/graduate_system";
	            String username = "root";
	            String password = "xin20140708";
	            Connection conn = DriverManager.getConnection(url, username,password);
	            return conn;

	        } catch (Exception e) {
	            throw new IllegalArgumentException(e);
	        }
	}
	public List<ExamData> examDatas(String cardId, String startDate,String endDate, String pageNum, String pagesize){
		
		List<ExamData> list=new ArrayList<ExamData>();
		Connection conn=null;
		PreparedStatement st=null;
		ResultSet rs=null;
		try{
		conn = getConnection();
		//查询一共多少条
        String hqlString="select count(*) as count from LeagMemberCardOperForXinYi where LeagMemberCardNo='"+cardId+"'";
        //查询具体结果
        
        String sql=" ID_ExamFeeItem,ExamFeeItem_Name,FeeChargeTime,UnitPrice from LeagMemberCardOperForXinYi where LeagMemberCardNo='"+cardId+"'";
        if(startDate!=null&&!"".equals(startDate)){
        	hqlString=hqlString+" and FeeChargeTime >= '"+startDate+"'";
        	sql+=" and FeeChargeTime >= '"+startDate+"'";
        }
        if(endDate!=null&&!"".equals(endDate)){
        	hqlString=hqlString+" and FeeChargeTime <='"+endDate+"'";
        	sql=sql+" and FeeChargeTime <= '"+endDate+"'";
        }
       
        st = conn.prepareStatement(hqlString);
        rs = st.executeQuery();
       
        int totalnum=0;
        while(rs.next()){
        	totalnum=rs.getInt(1);
        }
        System.out.print(totalnum+"abjkshdfhsalkjfhaslk");
        int totalpageNum=0;
        //pageNum,pageSize 转化为整数
        int i=0;
        int j=0;
        j=Integer.parseInt(pageNum);
        i=Integer.parseInt(pagesize);
        //判断页数是否合法
        //一共分多少页
        if (totalnum % i != 0) {
        	totalpageNum= totalnum  / i + 1;
		} else {
			totalpageNum= totalnum  / i;
		}
       
        if(j<=0||j>totalpageNum){
        	
   		return list;
        }
        else{
        	
        	 sql= sql+" order by FeeChargeTime desc ) as t order by t.FeeChargeTime ";
        	 
        	 st=null;
        	 rs=null;
        	 //占位符判断
        	 int ps=i;
        	 int pn=j*i;
        	 if(j==totalpageNum){
        		 ps=totalnum-i*(j-1);    
        		 pn=totalnum;
        	 }
        		 
        	 
        	 /*st.setString(1,String.valueOf(ps) );
        	 st.setString(2, String.valueOf(pn));
             rs = st.executeQuery();*/
        	 //拼接sql 语句
             String sqll="select top "+ps+" * from";
             String sqlll=" ( select top "+pn+" ";
             sql=sqll+sqlll+sql;
             st = conn.prepareStatement(sql);
             rs = st.executeQuery();
        	 int k=0;
             while (rs.next()){
            	 
             	/*if(k>=(j-1)*i&&k<j*i){
             	 ExamData data=new ExamData();
             	 data.setExamId(rs.getString(1));
             	 data.setExamName(rs.getString(2));
             	 data.setExamDate(rs.getString(3));
             	 data.setContent(rs.getString(2));
             	 data.setFee(rs.getString(4));
             	 list.add(data);
             	}
             	k++;*/
            	 ExamData data=new ExamData();
             	 data.setExamId(rs.getString(1));
             	 data.setExamName(rs.getString(2));
             	 data.setExamDate(rs.getString(3).trim().substring(0, 10));
             	 data.setContent(rs.getString(2));
             	 data.setFee(rs.getString(4));
             	 list.add(data);
              }
        }
       
		}catch (Exception e) {
			 
			e.printStackTrace();
		}finally{
         try {
			 rs.close();
			 st.close();
	         conn.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        
		}
		return list;
	}
	public List<FeeData> feeDatas(String cardId, String startDate,String endDate, String pageNum, String pagesize) {
		List<FeeData> list=new ArrayList<FeeData>();
		Connection conn=null;
		PreparedStatement st=null;
		ResultSet rs=null;
		try{
		conn = getConnection();
		//查询一共多少条
        String hqlString="select count(*) as count from LeagMemberCardOperForXinYi where LeagMemberCardNo='"+cardId+"'";
        //查询具体结果
        
        String sql=" ID_ExamFeeItem,ExamFeeItem_Name,FeeChargeTime,UnitPrice from LeagMemberCardOperForXinYi where LeagMemberCardNo='"+cardId+"'";
        if(startDate!=null&&!"".equals(startDate)){
        	hqlString=hqlString+" and FeeChargeTime >= '"+startDate+"'";
        	sql+=" and FeeChargeTime >= '"+startDate+"'";
        }
        if(endDate!=null&&!"".equals(endDate)){
        	hqlString=hqlString+" and FeeChargeTime <='"+endDate+"'";
        	sql=sql+" and FeeChargeTime <= '"+endDate+"'";
        }
       
        st = conn.prepareStatement(hqlString);
        rs = st.executeQuery();
       
        int totalnum=0;
        while(rs.next()){
        	totalnum=rs.getInt(1);
        }
        System.out.print(totalnum+"abjkshdfhsalkjfhaslk");
        int totalpageNum=0;
        //pageNum,pageSize 转化为整数
        int i=0;
        int j=0;
        j=Integer.parseInt(pageNum);
        i=Integer.parseInt(pagesize);
        //判断页数是否合法
        //一共分多少页
        if (totalnum % i != 0) {
        	totalpageNum= totalnum  / i + 1;
		} else {
			totalpageNum= totalnum  / i;
		}
       
        if(j<=0||j>totalpageNum){
        	
   		return list;
        }
        else{
        	
        	 sql= sql+" order by FeeChargeTime desc ) as t order by t.FeeChargeTime ";
        	 
        	 st=null;
        	 rs=null;
        	 //占位符判断
        	 int ps=i;
        	 int pn=j*i;
        	 if(j==totalpageNum){
        		 ps=totalnum-i*(j-1);    
        		 pn=totalnum;
        	 }
        		 
        	 
        	 /*st.setString(1,String.valueOf(ps) );
        	 st.setString(2, String.valueOf(pn));
             rs = st.executeQuery();*/
        	 //拼接sql 语句
             String sqll="select top "+ps+" * from";
             String sqlll=" ( select top "+pn+" ";
             sql=sqll+sqlll+sql;
             st = conn.prepareStatement(sql);
             rs = st.executeQuery();
        	 int k=0;
             while (rs.next()){
             	/*if(k>=(j-1)*i&&k<j*i){
             	 ExamData data=new ExamData();
             	 data.setExamId(rs.getString(1));
             	 data.setExamName(rs.getString(2));
             	 data.setExamDate(rs.getString(3));
             	 data.setContent(rs.getString(2));
             	 data.setFee(rs.getString(4));
             	 list.add(data);
             	}
             	k++;*/
            	 FeeData data=new FeeData();
             	 data.setFeeId(rs.getString(1));
             	 data.setFeeName(rs.getString(2));
             	 data.setFeeDate(rs.getString(3).trim().substring(0, 10));
             	 data.setFee(rs.getString(4));
             	 list.add(data);
              }
        }
       
		}catch (Exception e) {
			 
			e.printStackTrace();
		}finally{
         try {
			 rs.close();
			 st.close();
	         conn.close();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
        
		}
		return list;
	}
	//将体检系统新生成的会员信息导入到健管库
	public void phyTohealth(){
		
	}
	//查询体检系统里面是否产生新会员
	public List<PhysysCustomer> newPhysysCustomer(String createtime){
		
		List<PhysysCustomer> physcus= new ArrayList<PhysysCustomer>();
		Connection conn=null;
		PreparedStatement st=null;
		ResultSet rs=null;
		String sql=null;
		
		try{
			conn=getConnection();
			
			sql="select LeagMemberName,MemberCardName,LeagMemberCardNo,LeagMemberCardMoneyBalance,LeagMemberIDCardNo,LeagMemberBirthDate,DateValid,LeagMemberSex,LeagMemberAddress from LeagMemberCardForXinYi where DateValid > ? and F_Issued = 1 ";
			
			st = conn.prepareStatement(sql);
			st.setString(1,createtime);
			
	        rs = st.executeQuery();
	        while(rs.next()){
	        	
	        	String reString="";
	        	PhysysCustomer physysCustomer =new PhysysCustomer();
	        	
	        	reString=rs.getString(1);
	        	if(reString==null||reString.trim().equals("")){
	        		reString=" ";
	        	}	
	        	physysCustomer.setName(reString);
	        	
	        	reString=rs.getString(2);
	        	if(reString==null||reString.trim().equals("")){
	        		reString=" ";
	        	}	
	        	physysCustomer.setDegree(reString);
	        	
	        	reString=rs.getString(3);
	        	if(reString==null||reString.trim().equals("")){
	        		reString=" ";
	        	}	
	        	physysCustomer.setCardNo(reString);
	        	
	        	reString=rs.getString(4);
	        	if(reString==null||reString.trim().equals("")){
	        		reString=" ";
	        	}	
	        	physysCustomer.setBalance(reString);
	        	
	        	reString=rs.getString(5);
	        	if(reString==null||reString.trim().equals("")){
	        		reString=" ";
	        	}	
	        	physysCustomer.setIdNo(reString);
	        	
	        	reString=rs.getString(6);
	        	if(reString==null||reString.trim().equals("")){
	        		reString=" ";
	        	}	
	        	physysCustomer.setBirthday(reString);
	        	
	        	reString=rs.getString(7);
	        	if(reString==null||reString.trim().equals("")){
	        		reString=" ";
	        	}	
	        	physysCustomer.setCreateDate(reString);
	        	
	        	reString=rs.getString(8);
	        	if(reString==null||reString.trim().equals("")){
	        		reString=" ";
	        	}	
	        	physysCustomer.setSex(reString);
	        	
	        	reString=rs.getString(9);
	        	if(reString==null||reString.trim().equals("")){
	        		reString=" ";
	        	}	
	        	physysCustomer.setAddress(reString);
	        	
	        	physcus.add(physysCustomer);
	        	
	        }
		}catch (Exception e) {
			e.printStackTrace();
		}finally{
			try {
				 rs.close();
				 st.close();
		         conn.close();
			} catch (SQLException e) {
				
				e.printStackTrace();
			}
			
		}
		
		
		return physcus;
		
	}
	//将产生的新会员添加进健管数据库
	
	//查询健管系统里面最新的会员注册时间
	public String newHeailthTime(){
		
		String sql="select MAX(createtime) from cus_customer";
		
		String result="";
		Connection conn=null;
		PreparedStatement st=null;
		ResultSet rs=null;
		
		
		try{
			
			conn=getconnertion();
			st = conn.prepareStatement(sql);
	        rs = st.executeQuery();
	        
	        while(rs.next()){
	        	result=rs.getString(1);
	        }
			
		}catch(Exception e){
			
			e.printStackTrace();
		}finally{
			try {
				 rs.close();
				 st.close();
		         conn.close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
		}
		return result;
	}
	

}
