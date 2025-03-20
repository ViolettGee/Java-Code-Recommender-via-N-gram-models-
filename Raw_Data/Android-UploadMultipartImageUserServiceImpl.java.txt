package com.zs.service.impl;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.zs.dao.IBaseDao;
import com.zs.po.User;
import com.zs.service.IUserService;

@Service("UserServiceImpl")
public class UserServiceImpl implements  IUserService{

	@Autowired
	private IBaseDao baseDao;
	
	public User findUserForID(String email) throws Exception {
		String hql = "from User where email = ?";
		Object[] param= new Object[1];
		param[0]= email;
		List<User> users = baseDao.findByHql(hql,param);
		if(users!=null &&users.size()>0){
			return users.get(0);
		}
		return null;
	}

	public boolean saveUser(User user) throws Exception {
		baseDao.save(user);
		return true;
	}

	public User findUserForUserNameOrEmail(String username) throws Exception {
		String hql = "from User where email = ? or username = ?";
		Object[] param= new Object[2];
		param[0]= username;
		param[1]= username;
		List<User> users = baseDao.findByHql(hql,param);
		if(users!=null &&users.size()>0){
			return users.get(0);
		}
		return null;
	}
    
}
