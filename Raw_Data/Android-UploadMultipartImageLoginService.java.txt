package com.zs.service.impl;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.zs.dao.IBaseDao;
import com.zs.po.Login;
import com.zs.service.ILoginService;


@Service("LoginService")
public class LoginService implements ILoginService{
	@Autowired
	private IBaseDao baseDao;
	
	public Login getByID(String username)
	{
		return baseDao.get(Login.class,username);
	}
    public boolean login(String username,String password)
    {
    	Login lg = baseDao.get(Login.class,username);
    	if(lg != null)
    		return true;
        else
            return false;
    }
}
